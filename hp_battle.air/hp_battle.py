# -*- encoding=utf8 -*-
__author__ = "cc"

from airtest.core.api import *

auto_setup(__file__)
# -*- encoding=utf8 -*-
__author__ = "cc"

from airtest.core.api import *
import random
auto_setup(__file__)
# exists(Template(r"tpl1633197454285.png", record_pos=(-0.426, -0.236), resolution=(1664, 936)))

def checkend():
    sleep(0.5);

    if(exists(Template(r"tpl1633492461058.png", record_pos=(0.265, -0.078), resolution=(2960, 1440))) or exists(Template(r"tpl1633494997003.png", record_pos=(0.312, 0.223), resolution=(2960, 1440)))):
        touch((2095, 1215));
        return True;
    if(exists(Template(r"tpl1633197314093.png", record_pos=(-0.007, -0.203), resolution=(1664, 936)))):

        touch(Template(r"tpl1633190657081.png", record_pos=(0.007, 0.225), resolution=(1664, 936)))
        sleep(5);

        return True;
    if(exists(Template(r"tpl1633185678000.png", record_pos=(0.349, 0.23), resolution=(1664, 936)))):
        return True;
    sleep(0.5);

    return False;

def notfound():
    print("maybe end");
    sleep(1);

center = (328, 391);
offset = 150;

move_pos = [
    (952, 300), 
    (952, 800), 
    (2095, 300), 
    (2095, 800), 
];

slot_pos = [
    (952, 1229), 
    (1274, 1214),
    (1553, 1215),
    (1819, 1203),
    (2095, 1215),
]
dict_switch = {
    1: Template(r"tpl1633441142940.png", record_pos=(0.116, 0.165), resolution=(2960, 1440)),
    2: Template(r"tpl1633441158720.png", record_pos=(0.208, 0.168), resolution=(2960, 1440)),

    3: Template(r"tpl1633356997023.png", record_pos=(-0.066, -0.011), resolution=(1664, 936)),
    4: Template(r"tpl1633357006032.png", record_pos=(0.103, -0.016), resolution=(1664, 936)),
    5: Template(r"tpl1633357018216.png", record_pos=(0.192, -0.017), resolution=(1664, 936)),
    6: Template(r"tpl1633441035885.png", record_pos=(-0.069, 0.168), resolution=(2960, 1440)),

    7: Template(r"tpl1633441118624.png", record_pos=(0.025, 0.167), resolution=(2960, 1440)),
    8: Template(r"tpl1633357064749.png", record_pos=(-0.148, -0.001), resolution=(1664, 936)),
    9: Template(r"tpl1633441174174.png", record_pos=(-0.181, 0.171), resolution=(2960, 1440)),

};
# dict_switch = {
#     1: Template(r"tpl1633325515649.png", record_pos=(-0.004, 0.148), resolution=(1664, 936)),
#     2: Template(r"tpl1633325529811.png", record_pos=(0.207, 0.152), resolution=(1664, 936)),
#     3: Template(r"tpl1633325473311.png", record_pos=(-0.116, 0.152), resolution=(1664, 936)),
#     4: Template(r"tpl1633325542543.png", record_pos=(0.207, 0.148), resolution=(1664, 936)) ,
#     5: Template(r"tpl1633325487049.png", record_pos=(-0.005, 0.148), resolution=(1664, 936)),
#     6: Template(r"tpl1633325580790.png", record_pos=(0.104, 0.147), resolution=(1664, 936)) ,
#     7: Template(r"tpl1633325600844.png", record_pos=(-0.002, 0.147), resolution=(1664, 936)),
#     8: Template(r"tpl1633325619130.png", record_pos=(-0.111, 0.152), resolution=(1664, 936))
# }

def auto_magic():
#     choosen = random.randint(0,4);
    for pos in slot_pos:
        swipe(pos, random.choice(move_pos), duration=1, steps=6);
        auto_move();
        sleep(1);
        if(not exists(Template(r"tpl1633443031866.png", record_pos=(-0.025, -0.217), resolution=(2960, 1440)))):
            break;
def auto_move():
    rand = random.randint(0, len(move_pos)-1);
    touch(move_pos[rand]);

def do_class():
    if(exists(Template(r"tpl1633185678000.png", record_pos=(0.349, 0.23), resolution=(1664, 936)))):

        touch(Template(r"tpl1633185678000.png", record_pos=(0.349, 0.23), resolution=(1664, 936)));
    while(exists(Template(r"tpl1633443031866.png", record_pos=(-0.025, -0.217), resolution=(2960, 1440))) or (not checkend())):
        auto_magic();
for x in range(1500):
    print("第" + str(x + 1) + "上课");
    do_class();
# auto_magic()
# for pos in slot_pos:
#     if(pos):
#         swipe(pos, center, duration=0.5, steps=6);
    
