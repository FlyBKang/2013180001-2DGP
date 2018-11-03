from Object import *
import random
from pico2d import*

class GLOBAL:
    # stage = title, main, level, stage, end
    stage = "level"
    prev_stage = "main"

    # level menu
    g_Level = -1
    g_Hard = 0
    g_Type = 0
    g_ATT = False

    # in game stage
    g_StageTime = 0
    stageback = 1

    # main menu
    WindowX = 800
    WindowY = 800
    GameX = WindowX / 8 * 5
    MyMouse = [WindowX / 2, WindowY / 2]
    g_Time = 0
    g_TimeCheck = False
    g_Player = Player(WindowX / 8 * 2.5, WindowY / 8 * 1, 5, 8, 8)
    g_MonsterPool = [Monster(-1, -1, 0, 0) for i in range(0, 100)]



    # effect
    Star_EffectPool = [Effect(0, 0, 50, 0, 0, random.randint(7, 12), random.randint(7, 12)) for i in
                       range(0, 300)]
    for i in range(0, 100):
        Star_EffectPool[i].RandomSetting(random.randint(50, 100), WindowX, WindowY)
    MouseStar = [Effect(0, 0, 15, 0, 0, random.randint(22, 33), random.randint(22, 33)) for i in range(0, 50)]
    ClickStar = [Effect(0, 0, 5, 0, 0, random.randint(7, 10), random.randint(7, 10)) for i in range(0, 50)]
    ClickCnt = 0
    for i in range(0, 50):
        MouseStar[i].live = False

    # serve menu
    serve = False

    # Bullet
    g_BulletArr = [PlayerBullet(i) for i in range(0, 500)]
    g_BulletCnt = 0
    g_BulletDelay = 30

    g_MonsterBulletArr = [MonsterBullet() for i in range(0,300)]
    g_MonsterBulletCnt = 0

    def SetMonsterBullet(self,x,y,Dx,Dy,speed,w,h):
        for i in range(0,len(self.g_MonsterBulletArr)):
            if(self.g_MonsterBulletArr[i].Live == True):
                continue
            else:
                self.g_MonsterBulletArr[i].Set(x,y,Dx,Dy,speed,w,h)
                self.g_MonsterBulletArr[i].Live = True
                break




    def MonsterAttack(self):
        for Monster in self.g_MonsterPool:
            if Monster.live == True:
                if(Monster.Attack() >= 0):#basic attack
                    Monster.AttackDelay = 0.0
                    #if(self.g_Player.Y < Monster.Y):
                    if(self.g_Player.Y -150< Monster.Y < self.g_Player.Y +150 ):
                        self.SetMonsterBullet(Monster.X,Monster.Y,(self.g_Player.X-Monster.X)//20,(self.g_Player.Y-Monster.Y)//20,5,20,20)
                    else:
                        self.SetMonsterBullet(Monster.X,Monster.Y,(self.g_Player.X-Monster.X)//40,(self.g_Player.Y-Monster.Y)//40,5,20,20)








    def MonsterSet(self):
        if(self.g_Level == 0):
            for i in range(0,3):
                self.g_MonsterPool[i].Set(450,820,20+20*self.g_Hard,(i)*0.5+5,0,9-Global.g_Hard)
                self.g_MonsterPool[i].SetDir(-1,-1)
                self.g_MonsterPool[i+3].Set(50,820,20+20*self.g_Hard,(i)*0.5+5,0,9-Global.g_Hard)
                self.g_MonsterPool[i+3].SetDir(1,-1)

            for i in range(20,23):
                self.g_MonsterPool[i].Set(50 + 50*(i-20),820,20+20*self.g_Hard,2,0,9-Global.g_Hard)
                self.g_MonsterPool[i].SetDir(0,-1)

            for i in range(23,26):
                self.g_MonsterPool[i].Set(450 - 50*(i-23),820,20+20*self.g_Hard,2,0,9-Global.g_Hard)
                self.g_MonsterPool[i].SetDir(0,-1)

    def MonsterActive(self):
        global Timer
        for Monster in self.g_MonsterPool:
            if(Monster.life > 0 and Monster.SetTime != 0):
                if Monster.SetTime < get_time()-Timer.Time_Start:
                    Monster.live = True
                else:
                    break

    def MonsterMove(self):
        global Timer
        for Monster in self.g_MonsterPool:
            if(Monster.live == True):
                Monster.Move()



Global =GLOBAL()

open_canvas(Global.WindowX,Global.WindowY )