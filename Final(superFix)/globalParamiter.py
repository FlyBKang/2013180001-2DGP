from Object import *
import random
from Item import*


class GLOBAL:
    #sfx
    #item
    Itemshow = -1
    MyItem = inventory()
    Gift = [None,None,None]
    GiftCheck1 = 0
    GiftCheck2 = 1

    # stage = title, main, level, stage, end
    stage = "main"
    prev_stage = "main"

    # level menu
    g_Level = -1
    g_Hard = 0
    g_Type = 0
    g_Clear = False
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
    g_Player = Player(WindowX / 8 * 2.5, WindowY / 8 * 1, 5, 7, 8)

    #monster
    g_MonsterPool = [Monster(-1, -1, 0, 0) for i in range(0, 100)]
    g_Boss = Boss()


    # effect
    BossFX = [BossEff() for i in range(0,3)]
    BossFX[1].Degree = 120
    BossFX[2].Degree = 240
    Star_EffectPool = [Effect(0, 0, 50, 0, 0, random.randint(7, 12), random.randint(7, 12)) for i in
                       range(0, 300)]
    for i in range(0, 100):
        Star_EffectPool[i].RandomSetting(random.randint(50, 100), WindowX, WindowY)
    MouseStar = [Effect(0, 0, 15, 0, 0, random.randint(22, 33), random.randint(22, 33)) for i in range(0, 50)]
    ClickStar = [Effect(0, 0, 5, 0, 0, random.randint(7, 10), random.randint(7, 10)) for i in range(0, 50)]
    ClickCnt = 0
    for i in range(0, 50):
        MouseStar[i].live = False

    elec = [Elec() for i in range(0,100)]
    eleccnt = 0

    # serve menu
    pause = False

    # Bullet
    g_BulletArr = [PlayerBullet(i) for i in range(0, 500)]
    g_BulletCnt = 0
    g_BulletDelay = 30

    g_MonsterBulletArr = [MonsterBullet() for i in range(0,1000)]
    g_MonsterBulletCnt = 0

    def SetItem(self):
        if(self.g_Hard == 0):
            MyPercent = [60, 95, 100, 100]
        elif(self.g_Hard == 1):
            MyPercent = [40, 80, 95, 100]
        elif(self.g_Hard == 2):
            MyPercent = [0, 25, 75, 100]


        for j in range(0,3):
            num = random.randint(0,99)
            if(0 <= num <MyPercent[0]):
                ItemLevel = 0
            if(MyPercent[0]<= num <MyPercent[1]):
                ItemLevel = 1
            if(MyPercent[1]<= num <MyPercent[2]):
                ItemLevel = 2
            if(MyPercent[2]<= num <MyPercent[3]):
                ItemLevel = 3
            Itemlist = []
            for ITEM in ItemIndex:
                if( ITEM.Level == ItemLevel):
                    for MyITEM in self.MyItem.inven:
                        if MyITEM != ITEM:
                            Itemlist.append(ITEM)
            if(len(Itemlist) == 0):
                Itemlist.append(ItemIndex[0])
            self.Gift[j]= Itemlist[random.randint(0,len(Itemlist)-1)]

    def SetMonsterBullet(self,x,y,Dx,Dy,speed,w,h,type):
        for i in range(0,len(self.g_MonsterBulletArr)):
            if(self.g_MonsterBulletArr[i].Live == True):
                continue
            else:
                self.g_MonsterBulletArr[i].Set(x,y,Dx,Dy,speed,w,h)
                self.g_MonsterBulletArr[i].Type = type
                self.g_MonsterBulletArr[i].Live = True
                break


    def MonsterAttack(self):
        for Monster in self.g_MonsterPool:
            if Monster.live == True:
                if(Monster.Attack() >= 0):#basic attack
                    Monster.AttackDelay = 0.0
                    #if(self.g_Player.Y < Monster.Y):
                    if(Monster.AttackType == 0):
                        if(abs(self.g_Player.X-Monster.X)>abs(self.g_Player.Y-Monster.Y)):
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X - Monster.X) / abs(self.g_Player.X - Monster.X),
                                                  (self.g_Player.Y - Monster.Y) / abs(self.g_Player.X - Monster.X), 10,
                                                  20, 20,0)
                        else:
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                 (self.g_Player.X - Monster.X) / abs(self.g_Player.Y - Monster.Y),
                                                 (self.g_Player.Y - Monster.Y) / abs(self.g_Player.Y - Monster.Y), 10,
                                                 20, 20,0)

                    elif(Monster.AttackType == 1):
                        if (abs(self.g_Player.X - Monster.X) > abs(self.g_Player.Y - Monster.Y)):
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X+25 - Monster.X) / abs(self.g_Player.X - Monster.X),
                                                  (self.g_Player.Y+25 - Monster.Y) / abs(self.g_Player.X - Monster.X), 8+Global.g_Hard,
                                                  20, 20,1)
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X-25 - Monster.X) / abs(self.g_Player.X - Monster.X),
                                                  (self.g_Player.Y+25 - Monster.Y) / abs(self.g_Player.X - Monster.X), 8+Global.g_Hard,
                                                  20, 20,1)
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X - Monster.X) / abs(self.g_Player.X - Monster.X),
                                                  (self.g_Player.Y - Monster.Y) / abs(self.g_Player.X - Monster.X), 8+Global.g_Hard,
                                                  20, 20,1)
                        else:
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X+25 - Monster.X) / abs(self.g_Player.Y - Monster.Y),
                                                  (self.g_Player.Y+25 - Monster.Y) / abs(self.g_Player.Y - Monster.Y), 8+Global.g_Hard,
                                                  20, 20,1)
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X-25 - Monster.X) / abs(self.g_Player.Y - Monster.Y),
                                                  (self.g_Player.Y+25 - Monster.Y) / abs(self.g_Player.Y - Monster.Y), 8+Global.g_Hard,
                                                  20, 20,1)
                            self.SetMonsterBullet(Monster.X, Monster.Y,
                                                  (self.g_Player.X - Monster.X) / abs(self.g_Player.Y - Monster.Y),
                                                  (self.g_Player.Y - Monster.Y) / abs(self.g_Player.Y - Monster.Y), 8+Global.g_Hard,
                                                  20, 20,1)
                    elif (Monster.AttackType == 2):
                        if(random.randint(0,2)==0):
                            for j in range(0,40):
                                self.SetMonsterBullet(Monster.X, Monster.Y, 5*math.sin(math.radians(j*360//40)),-5*math.cos(math.radians(j*360//40)), 1, 20, 20,3)
                        else:
                            for j in range(0,40):
                                self.SetMonsterBullet(Monster.X, Monster.Y, 5.5*math.sin(math.radians(j*360//40)),-5.5*math.cos(math.radians(j*360//40)), 1, 20, 20,3)
                    elif (Monster.AttackType == 3):
                        if(Monster.Y > 250):
                            for j in range(0, 100):
                                if(j%10 <= 4):
                                    temp = 5-j%10
                                else:
                                    temp = j%10-4
                                self.SetMonsterBullet(Monster.X, Monster.Y, (temp+2) * math.sin(math.radians((100-j) * 360 / 100)),
                                                      (temp+2) * math.cos(math.radians((100-j) * 360 / 100)), 1, 20, 20,3)
                            Monster.AttackType = 4
                    elif (Monster.AttackType == 4):
                        if(Monster.Y > 250):
                            for j in range(0, 100):
                                if(j%10 <= 4):
                                    temp = 5-j%10
                                else:
                                    temp = j%10-4
                                self.SetMonsterBullet(Monster.X, Monster.Y, (temp+2) * math.sin(math.radians((j) * 360 / 100)),
                                                      (temp+2) * math.cos(math.radians((j) * 360 / 100)), 1, 20, 20,3)
                            Monster.AttackType = 3
                    elif (Monster.AttackType == 5):
                        if(Monster.Y > 400):
                            if (abs(self.g_Player.X - Monster.X) > abs(self.g_Player.Y - Monster.Y)):
                                self.SetMonsterBullet(Monster.X, Monster.Y,
                                                      (self.g_Player.X - Monster.X) / abs(self.g_Player.X - Monster.X),
                                                      (self.g_Player.Y - Monster.Y) / abs(self.g_Player.X - Monster.X),
                                                      15,14, 14,4)
                            else:
                                self.SetMonsterBullet(Monster.X, Monster.Y,
                                                      (self.g_Player.X - Monster.X) / abs(self.g_Player.Y - Monster.Y),
                                                      (self.g_Player.Y - Monster.Y) / abs(self.g_Player.Y - Monster.Y),
                                                      15,14, 14,4)
                        else:
                            Monster.SetDir(0,Monster.DirY-0.1)
    BossSetTime = 57
    def MonsterSet(self):
        if(self.g_Level == 0):
            for i in range(0,3):
                self.g_MonsterPool[i].Set(450,820,30+10*self.g_Hard,(i)*0.5+5,0,10-Global.g_Hard)
                self.g_MonsterPool[i].SetDir(-1,-0.5)
                self.g_MonsterPool[i+3].Set(50,820,30+10*self.g_Hard,(i)*0.5+5,0,10-Global.g_Hard)
                self.g_MonsterPool[i+3].SetDir(1,-0.5)
            for i in range(20,23):
                self.g_MonsterPool[i].Set(50 + 50*(i-20),820,30+10*self.g_Hard,10,0,10-Global.g_Hard)
                self.g_MonsterPool[i].SetDir(0,-0.5)

            for i in range(23,26):
                self.g_MonsterPool[i].Set(450 - 50*(i-23),820,30+10*self.g_Hard,10,0,10-Global.g_Hard)
                self.g_MonsterPool[i].SetDir(0,-0.5)
            for i in range(26,29):
                self.g_MonsterPool[i].Set(150 + 100*(26-i),820,50+10*self.g_Hard,15,1,15-Global.g_Hard*2)
                self.g_MonsterPool[i].SetDir(0,-0.5)

            for i in range(30,40):
                self.g_MonsterPool[i].Set(50 + 50*(random.randint(0,9)),820,30+10*self.g_Hard,random.randint(5,20)*0.5+18,0,15-Global.g_Hard*2)
                self.g_MonsterPool[i].SetDir(0,-0.5)


            self.g_MonsterPool[40].Set(350,820,250+100*self.g_Hard,28,2,5.5)
            self.g_MonsterPool[40].SetDir(-0.25,-0.5)
            for i in range(50,55):
                self.g_MonsterPool[i].Set(50 + 50*(random.randint(0,9)),820,30+10*self.g_Hard,random.randint(10,30),0,15-Global.g_Hard*2)
                self.g_MonsterPool[i].SetDir(0,-0.5)
            self.g_MonsterPool[42].Set(250, 820, 250 + 100 * self.g_Hard, 42, 2, 5.5)
            self.g_MonsterPool[42].SetDir(0, -0.5)

            for i in range(60,65):
                self.g_MonsterPool[i].Set(50 + 50 * (random.randint(0, 9)), 820, 40 + 10 * self.g_Hard,
                                          random.randint(30, 45), 1, 15 - Global.g_Hard * 2)
                self.g_MonsterPool[i].SetDir(0, -0.5)
            for i in range(65, 70):
                self.g_MonsterPool[i].Set(100 + 50 * (random.randint(0, 11)), 820, 40 + 10 * self.g_Hard,
                                          random.randint(20, 40), 1, 15 - Global.g_Hard * 2)
                self.g_MonsterPool[i].SetDir(0, -0.5)

                self.g_MonsterPool[70].Set(350, 820, 250 + 100 * self.g_Hard, 45, 3, 8)
                self.g_MonsterPool[70].SetDir(-0.1, -0.5)

            if(Global.g_Hard >= 1):
                self.g_MonsterPool[41].Set(150, 820, 250 + 100 * self.g_Hard, 14, 2, 5.5)
                self.g_MonsterPool[41].SetDir(0.25, -0.5)

                for i in range(55,60):
                    self.g_MonsterPool[i].Set(50 + 50*(random.randint(0,9)),820,20+10*self.g_Hard,random.randint(10,30),0,15-Global.g_Hard*2)
                    self.g_MonsterPool[i].SetDir(0,-0.5)

            if(Global.g_Hard >= 2):
                self.g_MonsterPool[42].Set(150, 820, 250 + 100 * self.g_Hard, 45, 3, 8)
                self.g_MonsterPool[42].SetDir(0, -0.5)
                for i in range(0, 3):
                    self.g_MonsterPool[90 + i].Set(50 + 100 * i, 820, 50 + 25 * self.g_Hard, 40 + i * 0.2, 5, 0.1)
                    self.g_MonsterPool[90 + i].SetDir(-0.1, -1.5)


        elif(self.g_Level == 1):

            for i in range(0, 3):
                self.g_MonsterPool[90 + i].Set(50 + 40 * i, 820, 50 + 25 * self.g_Hard, 4 + i * 0.25, 5, 0.1)
                self.g_MonsterPool[90 + i].SetDir(+0.1, -1.5)

            for i in range(0, 3):
                self.g_MonsterPool[93 + i].Set(450 - 40 * i, 820, 50 + 25 * self.g_Hard, 8 + i * 0.25, 5, 0.1)
                self.g_MonsterPool[93 + i].SetDir(-0.1, -1.5)

            self.g_MonsterPool[96].Set(150, 820, 250 + 100 * self.g_Hard, 10, 3, 8)
            self.g_MonsterPool[96].SetDir(0, -0.5)

            for i in range(0, 20):
                self.g_MonsterPool[i].Set(random.randint(50,450),820,50+10*self.g_Hard,12+(i),1,15-Global.g_Hard*2)
                self.g_MonsterPool[i].SetDir(0,-0.5)

            for i in range(0, 5):
                self.g_MonsterPool[20+i].Set(50+100*i,820,50+10*self.g_Hard,20,0,10-Global.g_Hard)
                self.g_MonsterPool[20+i].SetDir(0,-0.5)

            for i in range(0, 5):
                self.g_MonsterPool[25+i].Set(50+100*i,820,50+10*self.g_Hard,25,0,10-Global.g_Hard)
                self.g_MonsterPool[25+i].SetDir(0,-0.5)

            for i in range(0, 2):
                self.g_MonsterPool[30 + i].Set(50 + 100 * i, 820, 50 + 10 * self.g_Hard, 30, 0, 10 - Global.g_Hard)
                self.g_MonsterPool[30 + i].SetDir(0, -0.5)
            for i in range(0, 2):
                self.g_MonsterPool[32 + i].Set(350 + 100 * i, 820, 50 + 10 * self.g_Hard, 30, 0, 10 - Global.g_Hard)
                self.g_MonsterPool[32 + i].SetDir(0, -0.5)

            for i in range(0, 3):
                self.g_MonsterPool[40 + i].Set(50 + 50 * i, 820, 50 + 10 * self.g_Hard, 38, 5, 0.1)
                self.g_MonsterPool[40 + i].SetDir(0, -1.5)

            for i in range(0, 3):
                self.g_MonsterPool[43 + i].Set(450 - 50 * i, 820, 50 + 10 * self.g_Hard, 43, 5, 0.1)
                self.g_MonsterPool[43 + i].SetDir(0, -1.5)
            for i in range(0,10):
                self.g_MonsterPool[50 + i].Set(random.randint(250,400), 820, 50 + 10 * self.g_Hard, 43+random.randint(1,9), 1, 15 - Global.g_Hard)
                self.g_MonsterPool[50 + i].SetDir(0, -0.5)

            self.g_MonsterPool[97].Set(150, 820, 250 + 100 * self.g_Hard, 35, 2, 12)
            self.g_MonsterPool[97].SetDir(+0.3, -0.5)

            self.g_MonsterPool[60].Set(250, 820, 350 + 100 * self.g_Hard, 53, 3, 10)
            self.g_MonsterPool[60].SetDir(0.0, -0.5)

            if(Global.g_Hard >= 1):
                self.g_MonsterPool[99].Set(250, 820, 250 + 100 * self.g_Hard, 24, 3, 12)
                self.g_MonsterPool[99].SetDir(0.0, -0.75)
            if(Global.g_Hard >= 2):
                self.g_MonsterPool[98].Set(350, 820, 250 + 100 * self.g_Hard, 35, 2, 12)
                self.g_MonsterPool[98].SetDir(-0.3, -0.5)

                for i in range(0, 15):
                    self.g_MonsterPool[61 + i].Set(random.randint(50, 450), 820, 50 + 10 * self.g_Hard,
                                                   35 + i, 1, 15 - Global.g_Hard)
                    self.g_MonsterPool[61 + i].SetDir(0, -0.5)

        self.g_Boss.life = 1500 + 1000 * Global.g_Level + 400 * Global.g_Hard
        self.g_Boss.AttackType = Global.g_Level
        self.g_Boss.X = 250
        self.g_Boss.Y = 820
        self.g_Boss.SetDes(250, 550)
        if (self.g_Level == 0):
            #self.BossSetTime = 2
            #self.g_Boss.life = 1
            self.g_Boss.SkillCycle = [
                1.5 - self.g_Hard * 0.25,
                2 - self.g_Hard * 0.25,
                1.5 - self.g_Hard * 0.5,
                2.5,
                5,
                20,
                1.25
            ]
        else:
            #self.BossSetTime = 2
            #self.g_Boss.life = 1
            self.g_Boss.SkillCycle = [
                5,
                1.5 - self.g_Hard * 0.25,
                1.5 - self.g_Hard * 0.5,
                2.5,
                5,
                10,
                4
            ]
    def MonsterActive(self):
        global Timer
        for Monster in self.g_MonsterPool:
            if(Monster.life > 0 and Monster.SetTime != 0):
                if Monster.SetTime < get_time()-Timer.Time_Start:
                    Monster.live = True

        if(Global.g_Boss.life > 0):
            if(get_time() - Timer.Time_Start> self.BossSetTime):
                for Monster in self.g_MonsterPool:
                    Monster.life = -1
                    Monster.live = False
                Global.g_Boss.live = True

    def MonsterMove(self):
        global Timer
        for Monster in self.g_MonsterPool:
            if(Monster.live == True):
                Monster.Move()

        if(self.g_Boss.live == True):
            if self.g_Boss.ATT == False:
                self.g_Boss.ATT = self.g_Boss.Move()
                if(self.g_Boss.ATT == True):
                    self.g_Boss.AttackCycle = 10
            else:
                if(self.g_Boss.Attack() > 0):
                    self.g_Boss.AttackDelay = 0.0
                    self.g_Boss.SetDes(random.randint(1,4)*100,random.randint(10,15)*50)
                    self.g_Boss.ATT = False
                    self.g_Boss.AttackType += 1
                else:
                    self.g_Boss.Skill()
                    if(self.g_Level == 0):
                        if(self.g_Boss.AttackType <= 4):
                            for i in range(len(self.g_Boss.SkillCycle)):
                                if(self.g_Boss.SkillCycle[i] < self.g_Boss.SkillDelay[i]):
                                    self.g_Boss.SkillDelay[i] = 0
                                    if( i == 0):
                                        if (abs(self.g_Player.X - self.g_Boss.X) > abs(self.g_Player.Y - self.g_Boss.Y)):
                                            self.SetMonsterBullet(self.g_Boss.X, self.g_Boss.Y,
                                                                  (self.g_Player.X - self.g_Boss.X) / abs(self.g_Player.X - self.g_Boss.X),
                                                                  (self.g_Player.Y - self.g_Boss.Y) / abs(self.g_Player.X - self.g_Boss.X), 10,
                                                                  20, 20, 0)
                                        else:
                                            self.SetMonsterBullet(self.g_Boss.X, self.g_Boss.Y,
                                                                  (self.g_Player.X - self.g_Boss.X) / abs(self.g_Player.Y - self.g_Boss.Y),
                                                                  (self.g_Player.Y - self.g_Boss.Y) / abs(self.g_Player.Y - self.g_Boss.Y), 10,
                                                                  20, 20, 0)
                                    if (i == 3):
                                        if (abs(self.g_Player.X - self.g_Boss.X) > abs(self.g_Player.Y - self.g_Boss.Y)):
                                            self.SetMonsterBullet(self.g_Boss.X+10, self.g_Boss.Y,
                                                                  (self.g_Player.X+10 - self.g_Boss.X) / abs(
                                                                      self.g_Player.X+10 - self.g_Boss.X),
                                                                  (self.g_Player.Y - self.g_Boss.Y) / abs(
                                                                      self.g_Player.X+10 - self.g_Boss.X), 10,
                                                                  20, 20, 0)
                                            self.SetMonsterBullet(self.g_Boss.X-10, self.g_Boss.Y,
                                                                  (self.g_Player.X-10 - self.g_Boss.X) / abs(
                                                                      self.g_Player.X-10 - self.g_Boss.X),
                                                                  (self.g_Player.Y - self.g_Boss.Y) / abs(
                                                                      self.g_Player.X-10 - self.g_Boss.X), 10,
                                                                  20, 20, 0)
                                        else:
                                            self.SetMonsterBullet(self.g_Boss.X+10, self.g_Boss.Y,
                                                                  (self.g_Player.X+10 - self.g_Boss.X) / abs(
                                                                      self.g_Player.Y - self.g_Boss.Y),
                                                                  (self.g_Player.Y - self.g_Boss.Y) / abs(
                                                                      self.g_Player.Y - self.g_Boss.Y), 10,
                                                                  20, 20, 0)
                                            self.SetMonsterBullet(self.g_Boss.X - 10, self.g_Boss.Y,
                                                                  (self.g_Player.X-10 - self.g_Boss.X) / abs(
                                                                      self.g_Player.Y - self.g_Boss.Y),
                                                                  (self.g_Player.Y - self.g_Boss.Y) / abs(
                                                                      self.g_Player.Y - self.g_Boss.Y), 10,
                                                                  20, 20, 0)
                                    TEMP =random.randint(-10-self.g_Hard*10,11+self.g_Hard*10)
                                    if( i == 1):
                                        for j in range(0, 6):
                                            self.SetMonsterBullet(self.g_Boss.X, self.g_Boss.Y,
                                                                  5 * math.sin(math.radians(j * 360 // 6+30+TEMP)),
                                                                  -5 * math.cos(math.radians(j * 360 // 6+30+TEMP)), 0.5, 48,48, 3)
                                    if (i == 2):
                                        for j in range(0, 18):
                                            self.SetMonsterBullet(self.g_Boss.X, self.g_Boss.Y,
                                                                  5 * math.sin(math.radians(j * 360 // 6+TEMP)),
                                                                  -5 * math.cos(math.radians(j * 360 // 6+TEMP)), 1, 48, 48, 2)
                        elif (self.g_Boss.AttackType <= 8):
                            for i in range(len(self.g_Boss.SkillCycle)):
                                if (self.g_Boss.SkillCycle[i] < self.g_Boss.SkillDelay[i]):
                                    self.g_Boss.SkillDelay[i] = 0
                                    if (i == 4):
                                        for angle in range(0,360,20-self.g_Hard*5):
                                            self.SetMonsterBullet(self.g_Boss.X + 5*(angle%20-10) * math.sin(math.radians(angle)), self.g_Boss.Y + 5*(angle%20-10) * math.cos(math.radians(angle)),
                                                                  7 * math.sin(math.radians(angle)),
                                                                  7 * math.cos(math.radians(angle)),
                                                                  0.5, 34, 34, 1)
                                    if (i == 3):
                                        if (abs(self.g_Player.X - self.g_Boss.X) > abs(self.g_Player.Y - self.g_Boss.Y)):
                                            for angle in range(0,360,40):
                                                self.SetMonsterBullet(self.g_Boss.X + (20) * math.sin(math.radians(angle)), self.g_Boss.Y + (20) * math.cos(math.radians(angle)),
                                                                      (self.g_Player.X - self.g_Boss.X) / abs(
                                                                          self.g_Player.X - self.g_Boss.X),
                                                                      (self.g_Player.Y - self.g_Boss.Y) / abs(
                                                                          self.g_Player.X - self.g_Boss.X), 10,
                                                                      20, 20, 0)
                                        else:
                                            for angle in range(0,360,40):
                                                self.SetMonsterBullet(self.g_Boss.X + (20) * math.sin(math.radians(angle)), self.g_Boss.Y + (20) * math.cos(math.radians(angle)),
                                                                  (self.g_Player.X - self.g_Boss.X) / abs(
                                                                      self.g_Player.Y - self.g_Boss.Y),
                                                                  (self.g_Player.Y - self.g_Boss.Y) / abs(
                                                                      self.g_Player.Y - self.g_Boss.Y), 10,
                                                                  20, 20, 0)
                        elif (self.g_Boss.AttackType <= 11):
                            self.g_Boss.AttackCycle = 20
                            for i in range(len(self.g_Boss.SkillCycle)):
                                if (self.g_Boss.SkillCycle[i] < self.g_Boss.SkillDelay[i]):
                                    self.g_Boss.SkillDelay[i] = 0
                                    if (i == 0):
                                        for bullet in self.g_MonsterBulletArr:
                                            if(bullet.Type == 5):
                                                if ( bullet.Live == True):
                                                    self.SetMonsterBullet(bullet.X,bullet.Y,0,0,0,20,20,6)

                                    if (i == 4):
                                        if (abs(self.g_Player.X - self.g_Boss.X) > abs(self.g_Player.Y - self.g_Boss.Y)):
                                            self.SetMonsterBullet(self.g_Boss.X , self.g_Boss.Y ,
                                                                  (self.g_Player.X - self.g_Boss.X) / abs(
                                                                      self.g_Player.X - self.g_Boss.X),
                                                                  (self.g_Player.Y - self.g_Boss.Y) / abs(
                                                                      self.g_Player.X - self.g_Boss.X), 7,
                                                                  40, 40, 5)
                                        else:
                                            self.SetMonsterBullet(self.g_Boss.X , self.g_Boss.Y ,
                                                              (self.g_Player.X - self.g_Boss.X) / abs(
                                                                  self.g_Player.Y - self.g_Boss.Y),
                                                              (self.g_Player.Y - self.g_Boss.Y) / abs(
                                                                  self.g_Player.Y - self.g_Boss.Y), 7,
                                                              40, 40, 5)
                                    if (i == 5):
                                        for bullet in self.g_MonsterBulletArr:
                                            if(bullet.Type == 6):
                                                if (True == bullet.Live):
                                                    temp = random.randint(0,60)
                                                    for angle in range(0, 360, 60):
                                                        self.SetMonsterBullet(bullet.X , bullet.Y,
                                                                  2 * math.sin(math.radians(angle+temp)),
                                                                  2 * math.cos(math.radians(angle+temp)),
                                                                  1,14,14, 4)
                                                    bullet.Live = False

                        else:
                            self.g_Boss.AttackCycle = 10
                            self.g_Boss.AttackType = 0

                    #5,
                    #1.5 - self.g_Hard * 0.25,
                    #1.5 - self.g_Hard * 0.5,
                    #2.5,
                    #5,
                    #10,
                    #14
                    if (self.g_Level == 1):
                        if (self.g_Boss.AttackType <= 6):
                            for i in range(len(self.g_Boss.SkillCycle)):
                                if (self.g_Boss.SkillCycle[i] < self.g_Boss.SkillDelay[i]):
                                    self.g_Boss.SkillDelay[i] = 0
                                    if (i == 0):
                                        if (abs(self.g_Player.X - self.g_Boss.X) > abs(
                                                self.g_Player.Y - self.g_Boss.Y)):
                                            self.SetMonsterBullet(self.g_Boss.X, self.g_Boss.Y,
                                                                  (self.g_Player.X - self.g_Boss.X) / abs(
                                                                      self.g_Player.X - self.g_Boss.X),
                                                                  (self.g_Player.Y - self.g_Boss.Y) / abs(
                                                                      self.g_Player.X - self.g_Boss.X), 4,
                                                                  100, 100, 2)
                                        else:
                                            self.SetMonsterBullet(self.g_Boss.X, self.g_Boss.Y,
                                                                  (self.g_Player.X - self.g_Boss.X) / abs(
                                                                      self.g_Player.Y - self.g_Boss.Y),
                                                                  (self.g_Player.Y - self.g_Boss.Y) / abs(
                                                                      self.g_Player.Y - self.g_Boss.Y), 4,
                                                                  100,100, 2)
                                    if(i==1):
                                        for bullet in self.g_MonsterBulletArr:
                                            if (bullet.Type == 1):
                                                if (bullet.Live == True):
                                                    self.SetMonsterBullet(bullet.X, bullet.Y, 0, 0, 0, 14, 14, 0)
                                            if (bullet.Type == 5):
                                                if (bullet.Live == True):
                                                    self.SetMonsterBullet(bullet.X, bullet.Y, 0, 0, 0, 14, 14, 8)
                                    if (i == 3):
                                        self.SetMonsterBullet(self.g_Boss.X + 10, self.g_Boss.Y,
                                                                    1, 0, 10, 20, 20, 1)

                                        self.SetMonsterBullet(self.g_Boss.X - 10, self.g_Boss.Y,
                                                          -1,0, 10,20, 20, 1)

                                        self.SetMonsterBullet(self.g_Boss.X , self.g_Boss.Y,
                                                                    0, 1, 10, 20, 20, 5)

                                        self.SetMonsterBullet(self.g_Boss.X , self.g_Boss.Y,
                                                          0,-1, 10,20, 20, 5)

                                    if (i == 5):
                                        for bullet in self.g_MonsterBulletArr:
                                            if (bullet.Type == 0):
                                                if (True == bullet.Live):
                                                    if(bullet.Y > 400):
                                                        self.SetMonsterBullet(bullet.X, bullet.Y,
                                                                              0,
                                                                              -2,
                                                                              1, 14, 14, 9)
                                                    bullet.Live = False

                                            if (bullet.Type == 8):
                                                if (True == bullet.Live):
                                                    self.SetMonsterBullet(bullet.X, bullet.Y,
                                                                          -2,
                                                                          0,
                                                                          1, 14, 14, 10)
                                                    self.SetMonsterBullet(bullet.X, bullet.Y,
                                                                          2,
                                                                          0,
                                                                          1, 14, 14, 10)
                                                    bullet.Live = False

                        elif (self.g_Boss.AttackType <= 12):
                            for i in range(len(self.g_Boss.SkillCycle)):
                                if (self.g_Boss.SkillCycle[i] < self.g_Boss.SkillDelay[i]):
                                    self.g_Boss.SkillDelay[i] = 0
                                    if (i == 5):
                                        for bullet in self.g_MonsterBulletArr:
                                            if (bullet.Type == 0):
                                                if (True == bullet.Live):
                                                    if(bullet.Y > 400):
                                                        self.SetMonsterBullet(bullet.X, bullet.Y,
                                                                              0,
                                                                              -2,
                                                                              1, 14, 14, 9)
                                                    bullet.Live = False

                                            if (bullet.Type == 8):
                                                if (True == bullet.Live):
                                                    self.SetMonsterBullet(bullet.X, bullet.Y,
                                                                          -2,
                                                                          0,
                                                                          1, 14, 14, 10)
                                                    self.SetMonsterBullet(bullet.X, bullet.Y,
                                                                          2,
                                                                          0,
                                                                          1, 14, 14, 10)
                                                    bullet.Live = False
                                    if (i == 2):
                                        for j in range(0,3):
                                            if (abs(self.g_Player.X - self.g_Boss.X) > abs(self.g_Player.Y - self.g_Boss.Y)):
                                                self.SetMonsterBullet(self.BossFX[j].X, self.BossFX[j].Y,
                                                                      (self.g_Player.X - self.BossFX[j].X) / abs(self.g_Player.X - self.BossFX[j].X),
                                                                      (self.g_Player.Y - self.BossFX[j].Y) / abs(self.g_Player.X - self.BossFX[j].X), 8,
                                                                      12, 12, 3)
                                            else:
                                                self.SetMonsterBullet(self.BossFX[j].X, self.BossFX[j].Y,
                                                                      (self.g_Player.X - self.BossFX[j].X) / abs(self.g_Player.Y - self.BossFX[j].Y),
                                                                      (self.g_Player.Y - self.BossFX[j].Y) / abs(self.g_Player.Y - self.BossFX[j].Y), 8,
                                                                      12, 12, 3)

                                    if (i == 0):
                                        for j in range(0,180,10):
                                            self.SetMonsterBullet(self.g_Boss.X, self.g_Boss.Y,
                                                                  (5 + j/60)*math.sin((j)),
                                                                  (5 + j/60)*math.cos((j)),
                                                                  0.4,18, 18, 4)

                                        for j in range(180,360,10):
                                            self.SetMonsterBullet(self.g_Boss.X, self.g_Boss.Y,
                                                                  (5 + j/60)*math.sin((j)),
                                                                  (5 + j/60)*math.cos((j)),
                                                                  0.4,18, 18, 4)


                        elif (self.g_Boss.AttackType <= 14):
                            self.g_Boss.AttackCycle = 20
                            for i in range(len(self.g_Boss.SkillCycle)):
                                if (self.g_Boss.SkillCycle[i] < self.g_Boss.SkillDelay[i]):
                                    self.g_Boss.SkillDelay[i] = 0

                                    if (i == 4):
                                        for j in range(0,4):
                                            self.SetMonsterBullet(random.randint(1,500), 799-random.randint(0,50), 0, -1, 8, 24, 24, 4)
                                            self.SetMonsterBullet(random.randint(1,500), 799-random.randint(0,50), 0, -1, 8, 15, 15, 4)

                                    if(i == 5):
                                        for Bullet in Global.g_MonsterBulletArr:
                                            if Bullet.Type == 11:
                                                if(Bullet.DirY == 0):
                                                    Bullet.DirX = (5.5-random.randint(0,10))/10
                                                    if(random.randint(0,10)<2):
                                                        Bullet.DirY = 1
                                                    else:
                                                        Bullet.DirY = -1


                                            if Bullet.Type == 12:
                                                if(Bullet.DirY == 0):
                                                    Bullet.DirX = (2.5-random.randint(0,5))/10
                                                    if(random.randint(0,10)<2):
                                                        Bullet.DirY = 1
                                                    else:
                                                        Bullet.DirY = -1
                                    if (i == 3):
                                        for j in range(0,20):
                                            self.SetMonsterBullet( random.randint(1,500),random.randint(1,20), 0, 0, 5, 24, 24, 12)
                                        for j in range(0,15):
                                            self.SetMonsterBullet( random.randint(1,500),random.randint(1,20), 0, 0, 4, 15, 15, 11)
                                            self.SetMonsterBullet( random.randint(1,500),random.randint(1,20), 0, 0, 4, 15, 15, 11)


                        else:
                            self.g_Boss.AttackCycle = 10
                            self.g_Boss.AttackType = 0







Global =GLOBAL()

open_canvas(Global.WindowX,Global.WindowY )