from  globalParamiter import*

def MonsterCol():
    global Global

    for Monster in Global.g_MonsterPool:
        if Monster.live == True:
            if(-20< Monster.X< 520)==False:
                Monster.live = False
                Monster.life = 0
            if(-50< Monster.Y< 850)==False:
                Monster.live = False
                Monster.life = 0
            for Bullet in Global.g_BulletArr:
                if (Bullet.Draw == True):
                    if (Monster.X - Monster.W // 2 < Bullet.X < Monster.X + Monster.W // 2):
                        if (Monster.Y - Monster.H // 2 < Bullet.Y < Monster.Y + Monster.H // 2):

                            tempCheck1 = False
                            for Item in Global.MyItem.inven:
                                if (Item.Name == "부적[번개]"):
                                    tempCheck1 = True
                                    Global.elec[Global.eleccnt].Set(Bullet.X,Bullet.Y)
                                    Global.eleccnt= Global.eleccnt+1
                                    if(Global.eleccnt == 100):
                                        Global.eleccnt = 0
                                    break

                            tempCheck = False
                            for Item in Global.MyItem.inven:
                                if (Item.Name == "냉기폭풍"):
                                    tempCheck = True
                                    break
                            if(tempCheck == True):
                                if(tempCheck1 == True):
                                    Monster.Hit(Bullet.Damage*2+8)
                                else:
                                    Monster.Hit(Bullet.Damage*2)
                            else:
                                if(tempCheck1 == True):
                                    Monster.Hit(Bullet.Damage+8)
                                else:
                                    Monster.Hit(Bullet.Damage)
                            print(tempCheck,tempCheck1)
                            tempCheck = False
                            for Item in Global.MyItem.inven:
                                if (Item.Name == "관통"):
                                    tempCheck = True
                                    break
                            if(tempCheck == True):
                                Bullet.Draw = True
                            else:
                                Bullet.Draw = False


    if(Global.g_Boss.live == True):
        for Bullet in Global.g_BulletArr:
            if (Bullet.Draw == True):
                if (Global.g_Boss.X - Global.g_Boss.W // 2 < Bullet.X < Global.g_Boss.X + Global.g_Boss.W // 2):
                    if (Global.g_Boss.Y - Global.g_Boss.H // 2 < Bullet.Y < Global.g_Boss.Y + Global.g_Boss.H // 2):
                        Global.g_Boss.Hit(Bullet.Damage)
                        Bullet.Draw = False
                        if(Global.g_Boss.live == False):
                            for MonBullet in Global.g_MonsterBulletArr:
                                MonBullet.Live = False
                                Global.g_Clear = True

def MonsterBulletCol():
    global Global
    for Arr in Global.g_MonsterBulletArr:
        if Arr.Live == True:
            if(0< Arr.X < 500) == False:
                Arr.Live = False
            if(0< Arr.Y < Global.WindowY) == False:
                Arr.Live = False
            if(Arr.X - Arr.W/2 < Global.g_Player.X <Arr.X + Arr.W/2):
                if(Arr.Y - Arr.H/2 < Global.g_Player.Y <Arr.Y + Arr.H/2):
                    Arr.Live = False
                    if(Global.g_Player.invincibility == False):
                        if(Global.MyItem.Check(16) == True):
                            if 0 <= random.randint(0,100) < 25:
                                pass
                            else:
                                Global.g_Player.Life -= 1
                                Global.g_Player.invincibility = True
                        else:
                            Global.g_Player.Life -= 1
                            Global.g_Player.invincibility = True

                        if(Global.MyItem.Check(9) and  Global.MyItem.Check(17) ):
                            for Arr in Global.g_MonsterBulletArr:
                                if (Arr.Live == True):
                                    Arr.Live = False
                        else:
                            for Item in Global.MyItem.inven:
                                if (Item.Name == "부적[수호]"):
                                    for Arr in Global.g_MonsterBulletArr:
                                        if(Arr.Live == True):
                                            if Global.g_Player.X - 50 < Arr.X < Global.g_Player.X + 50 :
                                                if Global.g_Player.Y - 50 < Arr.Y < Global.g_Player.Y + 50 :
                                                    Arr.Live = False
                                if (Item.Name == "부적[수호2]"):
                                    for Arr in Global.g_MonsterBulletArr:
                                        if(Arr.Live == True):
                                            if Global.g_Player.X - 150 < Arr.X < Global.g_Player.X + 150 :
                                                if Global.g_Player.Y - 150 < Arr.Y < Global.g_Player.Y + 150 :
                                                    Arr.Live = False

