# -*- encoding=utf8 -*-
__author__ = "bytx"
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
from airtest.core.api import *
from airtest.core.android.rotation import XYTransformer
from airtest.core.settings import Settings as ST
ST.OPDELAY = 1
auto_setup(__file__,devices=["Android://127.0.0.1:5037/77c1acdb"])

# 解锁手机
def WakePhone():
    # 唤醒屏幕
    keyevent("26")
    dev = device()
    dev.swipe_along([[500, 1800],[500, 400]])
    touch([842, 1334])
    touch([842, 1334])
    touch([532, 1744])
    touch([842, 1334])
    
# 打开明日方舟
def OpenArknights():
    start_app("com.hypergryph.arknights.bilibili")
    touch(wait(Template(r"tpl1633531650208.png", record_pos=(0.0, 0.21), resolution=(2280, 1080)),timeout=60))
    
    sleep(60)

# 关闭明日方舟
def EndArknights():
    stop_app("com.hypergryph.arknights.bilibili")

def Action(use):
    touch(wait(Template(r"tpl1633533394792.png", record_pos=(0.391, 0.195), resolution=(2280, 1080))))
    if exists(Template(r"tpl1633570116555.png", record_pos=(-0.335, -0.063), resolution=(2280, 1080))):
        if(use==True):
            touch(Template(r"tpl1633570140546.png", record_pos=(0.296, 0.14), resolution=(2280, 1080)))
            touch(wait(Template(r"tpl1633533394792.png", record_pos=(0.391, 0.195), resolution=(2280, 1080))))
        else:
            return

    touch(wait(Template(r"tpl1633533411729.png", record_pos=(0.304, 0.095), resolution=(2280, 1080))))
    end=wait(Template(r"tpl1633533704765.png", record_pos=(-0.324, 0.179), resolution=(2280, 1080)),timeout=200)
    sleep(2)
    touch(end)
    sleep(3)

def Repeat(times,use):
    touch(Template(r"tpl1633533213073.png", record_pos=(0.247, -0.135), resolution=(2280, 1080)))
    touch([1851, 844])
    for i in range(times):
        Action(use)

Repeat(10,True)

# keyevent("26") 
        