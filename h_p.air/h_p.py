# -*- encoding=utf8 -*-
__author__ = "cc"

from airtest.core.api import *
import random
auto_setup(__file__)
# exists(Template(r"tpl1633197454285.png", record_pos=(-0.426, -0.236), resolution=(1664, 936)))
def checkend():
    sleep(0.5);
    if(exists(Template(r"tpl1633191723815.png", record_pos=(0.236, -0.036), resolution=(1664, 936)))):
        touch(wait(Template(r"tpl1633191723815.png", record_pos=(0.236, -0.036), resolution=(1664, 936))));
        print("成功");
        return True;
    if(exists(Template(r"tpl1633197314093.png", record_pos=(-0.007, -0.203), resolution=(1664, 936)))):

        touch(Template(r"tpl1633190657081.png", record_pos=(0.007, 0.225), resolution=(1664, 936)))
        print("失败");
        sleep(5);

        return True;
    if(exists(Template(r"tpl1633185678000.png", record_pos=(0.349, 0.23), resolution=(1664, 936)))):
        print("异常重开");
        return True;
        
    sleep(0.5);

    return False;

    
def notfound():
    print("maybe end");
    sleep(1);
def chosA():
    return exists(Template(r"tpl1633185721013.png", record_pos=(-0.45, 0.179), resolution=(1664, 936)))
def chosB():
    return exists(Template(r"tpl1633185728197.png", record_pos=(0.053, 0.167), resolution=(1664, 936)));
def chosC():
    return exists(Template(r"tpl1633185738554.png", record_pos=(-0.448, 0.243), resolution=(1664, 936)));
def chosD():    
    return exists(Template(r"tpl1633185747133.png", record_pos=(0.049, 0.239), resolution=(1664, 936)));
# from poco.drivers.unity3d import UnityPoco
dict_switch = {
    1: chosA,
    2: chosB,
    3: chosC,
    4: chosD
}

def do_class():
    if(exists(Template(r"tpl1633185678000.png", record_pos=(0.349, 0.23), resolution=(1664, 936)))):
        touch(Template(r"tpl1633185678000.png", record_pos=(0.349, 0.23), resolution=(1664, 936)));
    while(not checkend()):
        choosen = random.randint(1,4);
        fun = dict_switch.get(choosen);
        ret = fun();
        if ret:
            touch(ret);
        
for x in range(100):
    print("第" + str(x+1) + "上课");
    do_class();
    
# touch(wait(Template(r"tpl1633187086171.png", record_pos=(0.29, 0.257), resolution=(1664, 936))))
# wait(Template(r"tpl1633186880228.png", record_pos=(-0.124, -0.028), resolution=(1664, 936)))
# wait(Template(r"tpl1633186912321.png", record_pos=(-0.126, -0.022), resolution=(1664, 936)))
# wait(Template(r"tpl1633186983632.png", record_pos=(-0.124, -0.024), resolution=(1664, 936)))


# wait(Template(r"tpl1633187043819.png", record_pos=(-0.124, -0.018), resolution=(1664, 936)))
