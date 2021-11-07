# -*- encoding=utf8 -*-
__author__ = "zhouyan"

from airtest.core.api import *

# 设置全局的匹配阈值
ST.THRESHOLD = 0.85
# 图片exists匹配超时
ST.FIND_TIMEOUT_TMP = 0.2
# 设定匹配算法
ST.CVSTRATEGY = ['tpl']

# 五个战斗卡牌位置，相对于resolution=(1664, 1040)
slot_pos = [
    (500, 950),    # 伙伴卡
    (700, 950),    # 技能卡1
    (880, 950),    # 技能卡2
    (1060, 950),   # 技能卡3
    (1240, 950),   # 技能卡4
]

def main():
    auto_setup(__file__)
    print(">>>>>> start...")
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
        else:
            # 不知道在哪里，点击技能卡的位置试图过场
            do_simple_click(slot_pos[1])
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
    if try_find("battle_star.png") or try_find("move_card.png"):
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
    for pos in slot_pos:
        do_simple_click(pos)

def auto_move():
    pass

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
    return find_and_touch_with_cond("back_arrow.png", "go_to_community.png")

main()
