# -*- encoding=utf8 -*-
__author__ = "bytx"

from airtest.core.api import *

auto_setup(__file__)
# -*- encoding=utf8 -*-
__author__ = "bytx"
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
from airtest.core.api import *
from airtest.core.android.rotation import XYTransformer
from airtest.core.settings import Settings as ST
ST.OPDELAY = 1
auto_setup(__file__,devices=["android://127.0.0.1:5037/127.0.0.1:7555"])
   
# 贸易站
def MYZ():
    w,h = device().get_current_resolution()
    WorkStationTemplate([0.24*w, 0.43*h],Template(r"tpl1638326045393.png", record_pos=(-0.25, 0.24), resolution=(1120, 700)),Template(r"tpl1638524154860.png", record_pos=(-0.354, 0.121), resolution=(1820, 600)),[Template(r"拉普兰德.png", record_pos=(-0.124, -0.149), resolution=(1120, 700)),Template(r"tpl1638328488170.png", record_pos=(-0.123, 0.066), resolution=(1120, 700)),Template(r"tpl1638328519346.png", record_pos=(-0.013, 0.062), resolution=(1120, 700))],[Template(r"tpl1638524180317.png", record_pos=(-0.214, -0.092), resolution=(1820, 600)),Template(r"tpl1638524008250.png", record_pos=(-0.214, 0.043), resolution=(1820, 600)),Template(r"tpl1638524116880.png", record_pos=(-0.148, 0.044), resolution=(1820, 600))])

    WorkStationTemplate([0.18*w, 0.56*h],Template(r"tpl1638351832224.png", record_pos=(-0.252, 0.208), resolution=(1440, 810)),Template(r"tpl1638352042874.png", record_pos=(-0.251, 0.21), resolution=(1440, 810)),[Template(r"tpl1638352082377.png", record_pos=(0.101, -0.153), resolution=(1440, 810)),Template(r"tpl1638352093412.png", record_pos=(0.1, 0.062), resolution=(1440, 810)),Template(r"tpl1638352101870.png", record_pos=(0.215, -0.156), resolution=(1440, 810))],[Template(r"tpl1638351907888.png", record_pos=(0.215, 0.065), resolution=(1440, 810)),Template(r"tpl1638351935738.png", record_pos=(0.328, -0.156), resolution=(1440, 810)),Template(r"tpl1638351958442.png", record_pos=(0.328, 0.062), resolution=(1440, 810))])

# 根据技能排序
# SortOrder : 默认0 降序 1 升序
def SortByTechnicalAbility(SortOrder=0):
    sleep(1)
    touch(wait(Template(r"tpl1638498986847.png", record_pos=(0.463, -0.152), resolution=(1820, 600))))
    sleep(2)
    if exists(Template(r"tpl1638499000735.png", record_pos=(0.196, 0.063), resolution=(1820, 600))):
        touch(wait(Template(r"tpl1638499000735.png", record_pos=(0.196, 0.063), resolution=(1820, 600))))
    touch(wait(Template(r"tpl1638499018471.png", record_pos=(0.395, -0.095), resolution=(1820, 600))))
    wait(Template(r"tpl1638499032797.png", record_pos=(-0.406, -0.066), resolution=(1820, 600)))
    touch(Template(r"tpl1638359077606.png", record_pos=(0.319, -0.252), resolution=(1440, 810)))
    touch(Template(r"tpl1638359087666.png", record_pos=(0.254, -0.251), resolution=(1440, 810)))
    if SortOrder==1:
        touch(wait(Template(r"tpl1638499124081.png", record_pos=(0.356, -0.146), resolution=(1820, 600))))
    sleep(1)


# 模板函数 
# 参数：
#   Relative coordinates ：制造站绝对坐标 （相对坐标乘分辨率获得）
#   Team1Representative : 队伍1 代表人物
#   Team2Representative ：队伍2 代表人物
#   Team1Member1,Team1Member2,Team1Member3 替换队伍1 成员
#   Team2Member1,Team2Member2,Team2Member3 替换队伍2 成员
def WorkStationTemplate(RelativeCoordinates,Team1Representative,Team2Representative,Team1Members,Team2Members):

    while True:
        if exists(Template(r"tpl1638517516222.png", record_pos=(-0.469, -0.09), resolution=(1820, 600))):
            break
        else:
            touch(RelativeCoordinates)
            sleep(3)
        
    # 进入进驻信息页面
    if exists(Template(r"tpl1638518015464.png", record_pos=(0.441, 0.148), resolution=(1820, 600))):
        sleep()
    else :
        touch(Template(r"tpl1638497093146.png", record_pos=(-0.468, -0.033), resolution=(1820, 600)))
    
    # 判定当前队伍与下一队伍
    NextTeam = -1
    if exists(Team1Representative):
        NextTeam=2
    else :
        NextTeam=1
    
    
    Members = [0,0,0]
    if NextTeam==1:
        SortByTechnicalAbility()
        for i in range(0,len(Team1Members)):
            if Members[i]==0 and exists(Team1Members[i]) :
                touch(Team1Members[i])
                Members[i]=1
        touch(Template(r"tpl1638503192602.png", record_pos=(0.355, -0.146), resolution=(1820, 600)))

        for i in range(0,len(Team1Members)):
            if Members[i]==0 and exists(Team1Members[i]) :
                touch(Team1Members[i])
                Members[i]=1
    else :
        SortByTechnicalAbility()
        for i in range(0,len(Team2Members)):
            if Members[i]==0 and exists(Team2Members[i]) :
                touch(Team2Members[i])
                Members[i]=1
        touch(Template(r"tpl1638503192602.png", record_pos=(0.355, -0.146), resolution=(1820, 600)))
        for i in range(0,len(Team2Members)):
            if Members[i]==0 and exists(Team2Members[i]) :
                touch(Team2Members[i])
                Members[i]=1
    
    touch(Template(r"tpl1638500238808.png", record_pos=(0.453, 0.145), resolution=(1820, 600)))
    wait(Template(r"tpl1638503402785.png", record_pos=(-0.468, -0.089), resolution=(1820, 600)))
    
    for i in range(len(Team2Members)):
        if NextTeam==1 :
            assert_exists(Team1Representative, "结束界面")
        else :
            assert_exists(Team2Representative, "结束界面")

    touch(Template(r"tpl1638361344007.png", record_pos=(-0.43, -0.249), resolution=(1440, 810)))
    wait(Template(r"tpl1638355933768.png", record_pos=(-0.4, -0.189), resolution=(1440, 810)))
S