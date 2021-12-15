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


def ReturnHomePage():
    touch(Template(r"tpl1638960233681.png", record_pos=(-0.376, -0.148), resolution=(1820, 600)))
    touch(Template(r"tpl1638960243072.png", record_pos=(-0.252, -0.059), resolution=(1820, 600)))
    wait(Template(r"终端.png", record_pos=(0.256, -0.158), resolution=(1440, 810)))

def Action(use):
    touch(wait(Template(r"tpl1633533394792.png", record_pos=(0.391, 0.195), resolution=(2280, 1080)),timeout=60))
    sleep(3)
    if exists(Template(r"理智.png", record_pos=(-0.335, -0.063), resolution=(2280, 1080))):
        if(use==True):
            touch(Template(r"确定.png", record_pos=(0.296, 0.14), resolution=(2280, 1080)))
            touch(wait(Template(r"tpl1633533394792.png", record_pos=(0.391, 0.195), resolution=(2280, 1080)),timeout=60))
        else:
            touch(Template(r"取消.png", record_pos=(0.104, 0.169), resolution=(1120, 700)))
            return False

    touch(wait(Template(r"tpl1633533411729.png", record_pos=(0.304, 0.095), resolution=(2280, 1080)),timeout=60))
    end=wait(Template(r"行动结束.png", record_pos=(-0.324, 0.179), resolution=(2280, 1080)),timeout=300)
    sleep(5)
    touch(end)
    sleep(5)

def Repeat(times,use=False):
    touch(Template(r"终端.png", record_pos=(0.256, -0.158), resolution=(1440, 810)))
    wait(Template(r"tpl1638501370368.png", record_pos=(0.043, -0.086), resolution=(1820, 600)))
    touch(Template(r"tpl1638501358125.png", record_pos=(0.182, 0.082), resolution=(1820, 600)))
    if(exists(Template(r"tpl1638961572782.png", record_pos=(0.341, 0.137), resolution=(1820, 600)))):
        sleep()
    else :
        touch(Template(r"tpl1638960812625.png", record_pos=(0.44, 0.105), resolution=(1820, 600)))

    for i in range(times):
        if(Action(use)==False):
            ReturnHomePage()
            return
        else:
            continue
    ReturnHomePage()
# 进入基建
def EnterHome():
    touch(Template(r"tpl1636514671517.png", record_pos=(0.262, 0.203), resolution=(1120, 700)))
    wait(Template(r"控制中枢.png", record_pos=(0.159, -0.167), resolution=(1440, 810)),timeout=120)
def GetSource():
    if(exists(Template(r"tpl1636514869182.png", record_pos=(0.438, -0.244), resolution=(1120, 700)))):
        touch(Template(r"tpl1636514869182.png", record_pos=(0.438, -0.244), resolution=(1120, 700)))
        
        if exists(Template(r"tpl1637157182699.png", record_pos=(-0.045, 0.262), resolution=(1440, 810))):
            touch(Template(r"tpl1637157182699.png", record_pos=(-0.045, 0.262), resolution=(1440, 810)))
            sleep(2)

            
# 贸易站
def MYZ():
    w,h = device().get_current_resolution()

    WorkStationTemplate([0.24*w, 0.43*h],Template(r"tpl1638326045393.png", record_pos=(-0.25, 0.24), resolution=(1120, 700)),Template(r"tpl1638524154860.png", record_pos=(-0.354, 0.121), resolution=(1820, 600)),[Template(r"拉普兰德.png", record_pos=(-0.124, -0.149), resolution=(1120, 700)),Template(r"tpl1638328488170.png", record_pos=(-0.123, 0.066), resolution=(1120, 700)),Template(r"tpl1638328519346.png", record_pos=(-0.013, 0.062), resolution=(1120, 700))],[Template(r"tpl1638524180317.png", record_pos=(-0.214, -0.092), resolution=(1820, 600)),Template(r"tpl1638524008250.png", record_pos=(-0.214, 0.043), resolution=(1820, 600)),Template(r"tpl1638524116880.png", record_pos=(-0.148, 0.044), resolution=(1820, 600))])

    WorkStationTemplate([0.18*w, 0.56*h],Template(r"tpl1638351832224.png", record_pos=(-0.252, 0.208), resolution=(1440, 810)),Template(r"tpl1638352042874.png", record_pos=(-0.251, 0.21), resolution=(1440, 810)),[Template(r"tpl1638352082377.png", record_pos=(0.101, -0.153), resolution=(1440, 810)),Template(r"tpl1638352093412.png", record_pos=(0.1, 0.062), resolution=(1440, 810)),Template(r"tpl1638352101870.png", record_pos=(0.215, -0.156), resolution=(1440, 810))],[Template(r"tpl1638351907888.png", record_pos=(0.215, 0.065), resolution=(1440, 810)),Template(r"tpl1638351935738.png", record_pos=(0.328, -0.156), resolution=(1440, 810)),Template(r"tpl1638351958442.png", record_pos=(0.328, 0.062), resolution=(1440, 810))])

    
    
def BGS():
    w,h = device().get_current_resolution()
    WorkStationTemplate([0.803*w, 0.56*h],Template(r"tpl1638522278226.png", record_pos=(0.334, -0.1), resolution=(1820, 600)),Template(r"tpl1638522340339.png", record_pos=(0.332, -0.103), resolution=(1820, 600)),[Template(r"tpl1638355380449.png", record_pos=(-0.438, 0.202), resolution=(1440, 810))],[Template(r"tpl1638355479044.png", record_pos=(0.102, 0.067), resolution=(1440, 810))])
  

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

def ManufacturingStation():
    w,h = device().get_current_resolution()
    # 点击01制造站
    # 01 断罪 白雪 霜叶   食铁兽 小车 红豆        

    WorkStationTemplate([0.326*w, 0.383*h],Template(r"tpl1638516260751.png", record_pos=(0.334, -0.101), resolution=(1820, 600)),Template(r"tpl1638359017024.png", record_pos=(-0.24, 0.208), resolution=(1440, 810)),[Template(r"tpl1638359138517.png", record_pos=(-0.122, 0.062), resolution=(1440, 810)),Template(r"tpl1638359150673.png", record_pos=(0.101, -0.156), resolution=(1440, 810)),Template(r"tpl1638359159726.png", record_pos=(0.101, 0.063), resolution=(1440, 810))],[Template(r"tpl1638359243459.png", record_pos=(-0.123, -0.152), resolution=(1440, 810)),Template(r"tpl1638359251987.png", record_pos=(-0.011, -0.154), resolution=(1440, 810)),Template(r"tpl1638359261282.png", record_pos=(-0.01, 0.061), resolution=(1440, 810))])
    
    # 02 制造站 白面 杰西卡 赫默  调香 香草 适度
    WorkStationTemplate([0.28*w, 0.57*h],Template(r"tpl1638516313997.png", record_pos=(0.335, -0.036), resolution=(1820, 600)),Template(r"tpl1639097716826.png", record_pos=(0.114, 0.123), resolution=(1820, 600)),[Template(r"tpl1638359981989.png", rgb=False, record_pos=(0.144, -0.153), resolution=(1440, 810)),Template(r"tpl1638359990184.png", record_pos=(0.144, 0.065), resolution=(1440, 810)),Template(r"tpl1638363040237.png", record_pos=(0.279, -0.15), resolution=(1440, 810))],[Template(r"tpl1638359877843.png", rgb=True, record_pos=(0.061, 0.065), resolution=(1440, 810)),Template(r"tpl1638359888741.png", record_pos=(0.174, 0.065), resolution=(1440, 810)),Template(r"tpl1639097692487.png", record_pos=(0.118, -0.086), resolution=(1820, 600))])
    WorkStationTemplate([0.24*w, 0.7*h],Template(r"tpl1638516420142.png", record_pos=(0.334, -0.101), resolution=(1820, 600)),Template(r"tpl1638360746864.png", record_pos=(-0.24, 0.207), scale_max=820, resolution=(1440, 810)),[Template(r"tpl1638360790313.png", record_pos=(0.215, 0.066), resolution=(1440, 810)),Template(r"tpl1638360780564.png", record_pos=(0.328, -0.153), resolution=(1440, 810)),Template(r"tpl1638360771736.png", record_pos=(0.214, -0.16), resolution=(1440, 810))],[Template(r"tpl1638360463715.png", record_pos=(0.438, -0.156), resolution=(1440, 810)),Template(r"tpl1638360446950.png", record_pos=(0.438, 0.063), resolution=(1440, 810)),Template(r"tpl1638360434193.png", record_pos=(0.326, 0.065), resolution=(1440, 810))])
    WorkStationTemplate([0.31*w, 0.71*h],Template(r"tpl1638516494564.png", record_pos=(0.067, 0.123), resolution=(1820, 600)),Template(r"tpl1638360935534.png", record_pos=(-0.242, 0.208), resolution=(1440, 810)),[Template(r"tpl1638452756308.png", record_pos=(0.314, 0.038), resolution=(1820, 600)),Template(r"tpl1638579913772.png", record_pos=(0.116, -0.09), resolution=(1820, 600)),Template(r"tpl1639097798376.png", record_pos=(0.379, 0.038), resolution=(1820, 600))],[Template(r"tpl1638361288846.png", record_pos=(-0.011, 0.071), resolution=(1440, 810)),Template(r"tpl1638361277995.png", record_pos=(0.101, -0.15), resolution=(1440, 810)),Template(r"tpl1638361300535.png", record_pos=(0.44, 0.075), resolution=(1440, 810))])

def PowerStation():
    w,h = device().get_current_resolution()
    WorkStationTemplate([0.43*w, 0.41*h],Template(r"tpl1638457316260.png", record_pos=(0.334, -0.103), resolution=(1820, 600)),Template(r"tpl1638518398188.png", record_pos=(0.334, -0.101), resolution=(1820, 600)),[Template(r"tpl1638518364598.png", record_pos=(0.116, 0.038), resolution=(1820, 600))],[Template(r"tpl1638457528373.png", record_pos=(-0.28, 0.042), resolution=(1820, 600))])
    WorkStationTemplate([0.43*w, 0.71*h],Template(r"tpl1638457938950.png", record_pos=(0.336, -0.101), resolution=(1820, 600)),Template(r"tpl1638519075876.png", record_pos=(0.332, -0.099), resolution=(1820, 600)),[Template(r"tpl1638457993535.png", record_pos=(-0.28, -0.091), resolution=(1820, 600))],[Template(r"tpl1638457977542.png", record_pos=(0.117, 0.042), resolution=(1820, 600))])
    WorkStationTemplate([0.38*w, 0.56*h],Template(r"tpl1638457819792.png", record_pos=(0.334, -0.101), resolution=(1820, 600)),Template(r"tpl1638519117258.png", record_pos=(0.334, -0.103), resolution=(1820, 600)),[Template(r"tpl1638457860838.png", record_pos=(-0.281, -0.093), resolution=(1820, 600))],[Template(r"tpl1638457843443.png", record_pos=(-0.213, 0.04), resolution=(1820, 600))])

# 收取信用
def GetCredit():
    touch(Template(r"tpl1636980586071.png", record_pos=(-0.219, 0.167), resolution=(1440, 810)))
    touch(wait(Template(r"tpl1636980675099.png", record_pos=(-0.41, -0.108), resolution=(1440, 810)),timeout=30))
    touch(wait(Template(r"tpl1638959996840.png", record_pos=(-0.045, 0.042), resolution=(1820, 600)),timeout=30))
    
    for i in range(1,10):
        touch(wait(Template(r"tpl1636980803925.png", record_pos=(0.426, 0.214), resolution=(1440, 810)),timeout=40))
        sleep(8)
    touch(Template(r"tpl1637033246085.png", record_pos=(-0.294, -0.253), resolution=(1440, 810)))
    touch(wait(Template(r"tpl1637033265400.png", record_pos=(0.438, -0.075), resolution=(1440, 810)),timeout=30))
    touch(wait(Template(r"tpl1637033299969.png", record_pos=(0.417, -0.2), resolution=(1440, 810)),timeout=30))
    if exists(Template(r"tpl1637033327471.png", record_pos=(0.297, -0.253), resolution=(1440, 810))):
        touch(wait(Template(r"tpl1637033327471.png", record_pos=(0.297, -0.253), resolution=(1440, 810))))
        touch(wait(Template(r"tpl1637033352019.png", record_pos=(-0.002, 0.215), resolution=(1440, 810))))
    # 购买物资
    w,h = device().get_current_resolution()
    Pos = [[0.062, 0.378],[0.17, 0.347], [0.293, 0.335],[0.4, 0.355],[0.526, 0.367],[0.064, 0.717],[0.178, 0.698],[0.29, 0.705],[0.4, 0.705],[0.518, 0.722]]

    for i in range(0,10):
        Pos[i][0]=Pos[i][0]*w
        Pos[i][1]=Pos[i][1]*h
        touch(Pos[i])
        if exists(Template(r"tpl1637111152101.png", record_pos=(0.217, 0.171), resolution=(1440, 810))):
            touch(wait(Template(r"tpl1637111152101.png", record_pos=(0.217, 0.171), resolution=(1440, 810))))
            if exists(Template(r"tpl1637286184389.png", record_pos=(0.359, -0.194), resolution=(1440, 810))):
                ReturnHomePage()
                return

            if exists(Template(r"tpl1637033352019.png", record_pos=(-0.002, 0.215), resolution=(1440, 810))):
                touch(Template(r"tpl1637033352019.png", record_pos=(-0.002, 0.215), resolution=(1440, 810)))
            else :
                touch([0.907*w, 0.82*h])
         
            sleep(2)
 
    ReturnHomePage()

def GetTask():
    touch(Template(r"tpl1637154739133.png", record_pos=(0.091, 0.175), resolution=(1440, 810)))
    if exists(Template(r"tpl1637154793647.png", record_pos=(0.374, -0.176), resolution=(1440, 810))):
        sleep(10)
        touch(Template(r"tpl1637154793647.png", record_pos=(0.374, -0.176), resolution=(1440, 810)))
        touch(wait(Template(r"tpl1637033352019.png", record_pos=(-0.002, 0.215), resolution=(1440, 810))))
        sleep(2)
    
    touch(Template(r"tpl1637154958456.png", record_pos=(0.175, -0.253), resolution=(1440, 810)))
    if exists(Template(r"tpl1637154793647.png", record_pos=(0.374, -0.176), resolution=(1440, 810))):
        touch(Template(r"tpl1637154793647.png", record_pos=(0.374, -0.176), resolution=(1440, 810)))
        touch(wait(Template(r"tpl1637033352019.png", record_pos=(-0.002, 0.215), resolution=(1440, 810))))
        sleep(2)
    
    ReturnHomePage()

def Daily():
    if exists(Template(r"tpl1638493272887.png", record_pos=(0.001, -0.115), resolution=(1820, 600))):
        touch(wait(Template(r"tpl1638493283567.png", record_pos=(-0.002, 0.126), resolution=(1820, 600))))
        touch(wait(Template(r"tpl1638493304833.png", record_pos=(0.257, -0.13), resolution=(1820, 600))))

def SS():
    w,h = device().get_current_resolution()
    
    status = 1
    
    def SST(RelativeCoordinates):
        nonlocal status
        touch(RelativeCoordinates)
        wait(Template(r"tpl1638582538751.png", record_pos=(-0.471, -0.096), resolution=(1820, 600)))
        if exists(Template(r"tpl1638582552778.png", record_pos=(0.437, 0.149), resolution=(1820, 600))):
            sleep()
        else :
            touch(Template(r"tpl1638582570949.png", record_pos=(-0.47, -0.037), resolution=(1820, 600)))
        
        touch(wait(Template(r"tpl1638582586950.png", record_pos=(0.463, -0.152), resolution=(1820, 600))))
        touch(wait(Template(r"tpl1638582609832.png", record_pos=(0.397, -0.029), resolution=(1820, 600))))
        wait(Template(r"tpl1638582623753.png", record_pos=(-0.407, -0.07), resolution=(1820, 600)))
        if status ==1 :
            touch(wait(Template(r"tpl1638582720389.png", record_pos=(0.453, -0.147), resolution=(1820, 600))))
            touch(Template(r"tpl1638585785852.png", record_pos=(-0.093, -0.001), resolution=(1820, 600)))
            touch(Template(r"tpl1638582734332.png", record_pos=(-0.094, -0.055), resolution=(1820, 600)))
            touch(Template(r"tpl1638582747456.png", record_pos=(-0.018, -0.088), resolution=(1820, 600)))
            touch(Template(r"tpl1638582758123.png", rgb=False, record_pos=(-0.015, -0.087), resolution=(1820, 600)))
            sleep()
        
            touch(Template(r"tpl1638582782705.png", record_pos=(0.14, 0.087), resolution=(1820, 600)))
            status = 0
        Pos=[[0.215, 0.287],[0.276, 0.27],[0.355, 0.287],[0.219, 0.668],[0.275, 0.632]]
        
        for i in range(len(Pos)):
            Pos[i][0] *= w 
            Pos[i][1] *= h 
            touch(Pos[i])
        touch(Template(r"tpl1638582965516.png", record_pos=(0.453, 0.146), resolution=(1820, 600)))
        wait(Template(r"tpl1638583296065.png", record_pos=(-0.471, -0.095), resolution=(1820, 600)))
        touch(Template(r"tpl1638583302637.png", record_pos=(-0.458, -0.147), resolution=(1820, 600)))
        wait(Template(r"tpl1638583310771.png", record_pos=(-0.441, -0.11), resolution=(1820, 600)))

    SST([0.584*w, 0.418*h])
    SST([0.616*w, 0.57*h])
    SST([0.573*w, 0.727*h])
    SST([0.624*w, 0.835*h])

# EnterHome()
# MYZ()
# ManufacturingStation()
# PowerStation()
# BGS()
# SS()
# 
Repeat(90)