# -*- encoding=utf8 -*-
__author__ = "zhouyan"
Version = "v1.1-20211109"

from airtest.core.api import *
from airtest.core.android.android import *
import random

# 设置全局的匹配阈值
ST.THRESHOLD = 0.75
# 图片exists匹配超时
ST.FIND_TIMEOUT_TMP = 0.2
# 设定匹配算法
ST.CVSTRATEGY = ['sift']
ST.SAVE_IMAGE = False;
# 强制战斗模式
ForceBattle = False

# 禁林模式
# FFMode = False
FFMode = True

# 五个战斗卡牌位置，相对于resolution=(1664, 1040)
slot_pos = [
    (500, 850),    # 伙伴卡
    (700, 850),    # 技能卡1
    (880, 850),    # 技能卡2
    (1060, 850),   # 技能卡3
    (1240, 850),   # 技能卡4
]

# 禁林选择星级时需要的滑动
ff_swipe = [
    (1240, 500),
    (1240, 300),
]

# 战斗移动点
if FFMode:
    # 禁林战斗位置
    move_pos = [
        (200, 700),
        (600, 700),
        (1000, 700),
        (1400, 700),
    ]
else:
    # 对战战斗位置
    move_pos = [
        (200, 700),
        (200, 500),
        (200, 300),
    ]

# 不知道卡在哪里的时候尝试点击解套
safe_pos = [
    (700, 980),
    (10, 900),
    (10, 900),
]

def main():
    # 默认初始化
    auto_setup(__file__)
    print(">>>>>> start " + Version)
    # 自适应分辨率调整坐标值
    (width, height) = Android().get_current_resolution()
    for i in range(len(slot_pos)):
        slot_pos[i] = (slot_pos[i][0] * width / 1664, slot_pos[i][1] * height / 1040)
    for i in range(len(ff_swipe)):
        ff_swipe[i] = (ff_swipe[i][0] * width / 1664, ff_swipe[i][1] * height / 1040)
    # 开始主循环
    do_main_loop()

def do_main_loop():
    wander_count = 0
    while True:
        if fast_check_battle():
            # 确定在战斗中
            do_battle()
            wander_count = 0
        elif check_and_proceed_current_status(wander_count):
            # 确定完成了过场点击
            sleep(0.5)
            wander_count = 0
        elif FFMode and (try_find("social.png") or try_find("new_mail.png")) and try_find("world_map.png"):
            # 开始禁林选择流程
            do_ff_mode()
            wander_count = 0
        else:
            # 不知道在哪里，点击技能卡的位置试图过场
            do_simple_click(safe_pos[1])
            wander_count += 1

def try_find(image):
    try:
        return exists(Template(image))
    except TargetNotFoundError:
        return False

def try_touch(image):
    try:
        touch(Template(image))
        return True
    except TargetNotFoundError:
        return False

def fast_check_battle():
    if ForceBattle or try_find("battle_star.png") or try_find("move_card.png"):
        print(">>>>>>>>>>>> fast battle check: true\n")
        return True
    else:
        print(">>>>>>>>>>>> fast battle check: false\n")
        return False

def do_simple_click(pos):
    touch(pos)
    sleep(0.5)
    double_click(pos)
    sleep(0.5)

def do_battle():
    auto_magic()
    auto_move()

def auto_magic():
    for i in range(len(slot_pos)):
        if FFMode and i == 0:    # 禁林中不使用伙伴卡
            continue
        elif not fast_check_battle(): #增大间隔
            return;
        else:
            do_simple_click(slot_pos[i])

move_threshold = 0
def auto_move():
    global move_threshold
    move_threshold += 1
    if move_threshold >= 2:
        if fast_check_battle():
            rand = random.randint(0, len(move_pos) - 1)
            touch(move_pos[rand])
            move_threshold = 0

def check_and_proceed_current_status(wander_count):
    if try_start() or try_end():
        return True
    elif wander_count >= 5:    # 为提升匹配效率，连续5次不知道在哪里的点击之后才触发错误修复匹配
        return try_fix_error()
    else:
        return False

def find_and_touch(image):
    if try_find(image):
        return try_touch(image)
    else:
        return False

def find_and_touch_with_cond(image, *conds):
    exist = try_find(image)
    if exist:
        for cond in conds:
            exist = (exist and try_find(cond))
            if not exist:
                break
    if exist:
        return try_touch(image)
    else:
        return False

def try_start():
    return find_and_touch("start_match.png") or find_and_touch("start_lesson.png")

def try_end():
    return find_and_touch("back.png")

def try_fix_error():
    # 修复误入聊天界面
    if find_and_touch_with_cond("back_arrow.png", "go_to_community.png"):
        return True
    # 修复卡在选取禁林星级界面
    if find_and_touch_with_cond("back_arrow.png", "choose_star.png"):
        return True
    # 修复卡在使用回响界面
    if find_and_touch_with_cond("back_arrow.png", "use.png"):
        return True
    # 修复意外弹窗导致主界面卡住
    for pos in safe_pos:
        touch(pos)
        sleep(1.0)
    return False

def try_touch_series(image_list):
    for image in image_list:
        success = False
        # 重试40秒时间以跳过邀请弹框
        for i in range(40):
            if try_touch(image):
                success = True
                break
            else:
                sleep(1.0)
        if not success:
            return False
        sleep(0.5)
    return True

def do_ff_mode():
    if not try_touch_series(["social.png", "wizard_help.png", "forbidden_forest.png", "blue_clue.png", "star_level.png"]):
        try_touch("back_arrow.png")
        return
    swipe(ff_swipe[0], ff_swipe[1], duration = 0.5)
    sleep(1.0)
    if not try_touch_series(["star_level_10.png", "confirm.png", "fast_join.png"]):
        try_touch("back_arrow.png")
        return
    # 这里要有充足时间否则容易选不中线索
    sleep(8.0)
    if try_find("select.png"):
        try_touch("select.png")
    else:
        # 没有合适的房间加入则退出重来
        try_touch("back_arrow.png")
    sleep(1.0)

main()
