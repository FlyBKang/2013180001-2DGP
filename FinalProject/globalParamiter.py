import pico2dtest as container
import random

#stage = title, main, level, stage, end
stage = "level"
prev_stage = "main"

#level menu
g_Level = -1
g_Hard = 0
g_Type = 0


#in game stage
g_StageTime = 0
stageback = 1

#main menu
WindowX = 800
WindowY = 800
GameX = WindowX/8*5
MyMouse = (WindowX/2,WindowY/2)
g_Time = 0
g_TimeCheck = False
g_Player = container.Player(WindowX/8*2.5,WindowY/8*1,5,8,8)
g_MonsterPool = [container.Monster(-1,-1,0,0)for i in range(0,100)]


#effect
Star_EffectPool = [container.Effect(0,0,50,0,0,random.randint(7,12),random.randint(7,12)) for i in range(0,300)]
for i in range(0,100):
    Star_EffectPool[i].RandomSetting(random.randint(50,100),WindowX,WindowY)
MouseStar = [container.Effect(0,0,15,0,0,random.randint(22,33),random.randint(22,33)) for i in range(0,50)]
ClickStar = [container.Effect(0,0,5,0,0,random.randint(7,10),random.randint(7,10)) for i in range(0,50)]
ClickCnt = 0
for i in range(0,50):
    MouseStar[i].live = False

#serve menu
serve = False
