from pico2d import*
from  globalParamiter import*
from InputManager import *
from Collision import *
from music import *

class TEXTURE:
    P_main = load_image("resource\\main.jpg")
    P_player = load_image("resource\\character.png")
    P_player_alpha = load_image("resource\\character.png")
    P_player_alpha.opacify(0.5)
    P_light1 = load_image("resource\\Eff_Glitter.png")
    P_light2 = load_image("resource\\Eff_Glitter2.png")
    P_light3 = load_image("resource\\Eff_Glitter3.png")
    P_light4 = load_image("resource\\Eff_Glitter4.png")
    P_startbutton = load_image("resource\\startbutton.png")
    P_exitbutton = load_image("resource\\exitbutton.png")
    P_bullet = load_image("resource\\bullet.png")
    P_menuback = load_image("resource\\edge.png")
    P_menuside = load_image("resource\\side.png")
    P_mouse = load_image("resource\\pointer.png")
    P_okbutton = load_image("resource\\okbutton.png")
    P_cancelbutton = load_image("resource\\cancelbutton.png")
    P_levelselect = load_image("resource\\edge2.png")
    P_item = load_image("resource\\item.png")
    P_effectlevel = load_image("resource\\effect_background.png")
    P_leveltype = load_image("resource\\level_type.png")
    P_stage = [load_image("resource\\stage1.jpg"),load_image("resource\\stage2.jpg")]
    P_level = [load_image("resource\\level_easy.png"), load_image("resource\\level_normal.png"), load_image("resource\\level_hard.png")]
    P_textlevel = [load_image("resource\\menu_stage.png"), load_image("resource\\menu_level.png"), load_image("resource\\menu_attack.png"),
                   load_image("resource\\menu_item.png")]
    P_nextbutton = load_image("resource\\nextstage.png")
    # 텍스쳐를 불러옵니다.
    P_Monster = load_image("resource\\Unit.png")
    P_Boss1 = load_image("resource\\boss2.png")
    P_Boss2 = load_image("resource\\boss3.png")
    P_Boss3 = load_image("resource\\boss1.png")
    P_Info = load_image("resource\\Iteminfo.png")
    P_Info2 = load_image("resource\\Iteminfo_plus.png")
    P_life = load_image("resource\\Life.png")
    P_UI = load_image("resource\\UIinfo.jpg")
    P_bullet2 = load_image("resource\\bullet2.png")
    stage_arr = [Map(0, 0, 500, 800),Map(800, 225, 400, 400)]
    Font = load_font('STIXGeneral.ttf', 25)
    P_elec = load_image("resource\\earth0.png")

Texture = TEXTURE()
def Collision():
    global Global
    if(Global.stage == "stage"):
        MonsterCol()
        MonsterBulletCol()
        Global.g_Player.Invin()

def Draw():

    global Global, sound
    sound.play_bgm(Global.stage)
    if (Global.stage == "main"):
        TitleDraw()
    elif(Global.stage == "stage"):
        CreateBullet()
        StageDraw()
        shoot()
        Global.MonsterActive()
        Global.MonsterMove()
        Global.MonsterAttack()
        BulletDraw()
        MonsterDraw()
        Collision()
        BulletEffect()
        UI_Draw()
        if(Global.g_Clear == True):
            ClearUI_Draw()

    elif(Global.stage == "level"):
        LevelDraw()

    if(Global.stage != "stage"):
        EffectDraw()

    #mouse cursor
    Texture.P_mouse.draw(Global.MyMouse[0],Global.MyMouse[1],100,100)

def UI_Draw():
    global Global,Texture,Timer
    Texture.P_UI.draw(650,400,300,800)
    Texture.Font.draw(670,720, '%d' %Global.g_Level, (255, 255, 255))
    Texture.Font.draw(670,675, '%d' %Global.g_Hard, (255, 255, 255))
    Texture.Font.draw(670,590, '%d' %Global.g_Player.Life, (255, 255, 255))

    if(Global.g_Player.Life > 10):
        for i in range(0,10):
            Texture.P_life.draw(570+ i*20,545,40,40)
    else:
        for i in range(0,Global.g_Player.Life):
            Texture.P_life.draw(570+ i*20,545,40,40)
    tempX = 0
    tempY = 0
    for ITEM in Global.MyItem.inven:
        if ITEM.Num != -1:
            ItemDraw(ITEM.Num,570+70*tempX,305-70*tempY,60,60)
        tempX += 1
        if(tempX == 3):
            tempX = 0
            tempY += 1

def EffectDraw():
    global Global
    ##main Effect
    if(Global.stage != "stage"):
        if (Global.g_TimeCheck == False):
            Global.g_Time = Global.g_Time + 2 * Timer.Time_Frame * Timer.CompensatorSpeed
            if (Global.g_Time > Texture.P_main.w - Global.WindowX):
                Global.g_TimeCheck = True
        else:
            Global.g_Time = Global.g_Time - 2 * Timer.Time_Frame * Timer.CompensatorSpeed
            if (Global.g_Time < Global.WindowY):
                Global.g_TimeCheck = False
        for i in range(0,100):
            if(Global.Star_EffectPool[i].live == True):
                if( (i % 2) == 0):
                    Texture.P_light1.composite_draw(math.radians(random.randint(0,360)),'',Global.Star_EffectPool[i].X,Global.Star_EffectPool[i].Y,Global.Star_EffectPool[i].Wsize,Global.Star_EffectPool[i].Hsize)
                else:
                    Texture.P_light2.composite_draw(math.radians(random.randint(0,360)),'',Global.Star_EffectPool[i].X,Global.Star_EffectPool[i].Y,Global.Star_EffectPool[i].Wsize,Global.Star_EffectPool[i].Hsize)
                Global.Star_EffectPool[i].Move()
            else:
                Global.Star_EffectPool[i].RandomSetting(random.randint(50, 100), Global.WindowX, Global.WindowY)
                Global.Star_EffectPool[i].live = True
        for i in range(0,50):
            if(Global.MouseStar[i].live == True):
                if(i%2 == 0):
                    Texture.P_light3.composite_draw(math.radians(random.randint(0, 360)), '', Global.MouseStar[i].X,Global.MouseStar[i].Y, Global.MouseStar[i].Life*2, Global.MouseStar[i].Life*2)
                else:
                    Texture.P_light4.composite_draw(math.radians(random.randint(0, 360)), '', Global.MouseStar[i].X,Global.MouseStar[i].Y, Global.MouseStar[i].Life*2, Global.MouseStar[i].Life*2)
                Global.MouseStar[i].Move()
        angle = float(math.radians(1))
        if(Global.ClickCnt < 50):
            Global.ClickCnt = Global.ClickCnt+1*Timer.Time_Frame*Timer.CompensatorSpeed
            for i in range(0,50):
                if Global.ClickStar[i].live == True:
                    if(i%2==0):
                        Texture.P_light3.composite_draw(math.radians(random.randint(0, 1)), '',
                                                Global.ClickStar[i].X + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.sin(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Y + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.cos(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Wsize, Global.ClickStar[i].Hsize)
                    else:
                        Texture.P_light4.composite_draw(math.radians(random.randint(0, 1)), '',
                                                Global.ClickStar[i].X + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.sin(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Y + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.cos(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Wsize, Global.ClickStar[i].Hsize)

                    if(i%2==0):
                        Texture.P_light3.composite_draw(math.radians(random.randint(0, 1)), '',
                                                Global.ClickStar[i].X + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.sin(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Y + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.cos(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Wsize//0.75, Global.ClickStar[i].Hsize//0.75)
                    else:
                        Texture.P_light4.composite_draw(math.radians(random.randint(0, 1)), '',
                                                Global.ClickStar[i].X + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.sin(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Y + Global.ClickCnt/2*random.randint(20,100)*0.02 * math.cos(angle * float(360 / 50 * i)),
                                                Global.ClickStar[i].Wsize//0.75, Global.ClickStar[i].Hsize//0.75)

    ##main Effect

def TitleDraw():
    global Global, Texture, Timer
    ##main menu
    Texture.P_main.clip_draw(0 + (int)(Global.g_Time), 0, Global.WindowX, Global.WindowY, Global.WindowX // 2,Global.WindowY // 2)
    ##main menu
    if (100 < Global.MyMouse[0] < 700):
        if (400 < Global.MyMouse[1] < 500):
            Texture.P_startbutton.draw(Global.WindowX / 2, Global.WindowY - 350, 620, 110)
        else:
            Texture.P_startbutton.draw(Global.WindowX / 2, Global.WindowY - 350, 600, 100)
    else:
        Texture.P_startbutton.draw(Global.WindowX / 2, Global.WindowY - 350, 600, 100)

    if (100 < Global.MyMouse[0] < 700):
        if (250 < Global.MyMouse[1] < 350):
            Texture.P_exitbutton.draw(Global.WindowX / 2, Global.WindowY - 500, 620, 110)
        else:
            Texture.P_exitbutton.draw(Global.WindowX / 2, Global.WindowY - 500, 600, 100)
    else:
        Texture.P_exitbutton.draw(Global.WindowX / 2, Global.WindowY - 500, 600, 100)



def StageDraw():
    global Global, Timer
    if (Global.stage == "stage"):
        if (Global.g_Level == 0):
            if (Global.stageback == 1):
                Texture.P_stage[0].clip_composite_draw(0 + (int)(Global.g_StageTime / 3 * 2),
                                                       0 + (int)(Global.g_StageTime), (int)(Texture.P_stage[0].w // 3),
                                                       (int)(Texture.P_stage[0].h // 2), 0, "", 250, 400, 500, 800)
                #if (Global.serve == False):
                Global.g_StageTime = Global.g_StageTime + 1.25*Timer.Time_Frame* Timer.MapCompensatorSpeed
                if (Texture.P_stage[0].h > Global.g_StageTime >= Texture.P_stage[0].h // 2):
                    Global.stageback = -1
            elif (Global.stageback == -1):
                if (Global.g_StageTime >= Texture.P_stage[0].h):
                    pass
                else:
                    Global.g_StageTime = Global.g_StageTime + 1.25*Timer.Time_Frame* Timer.MapCompensatorSpeed
                Texture.P_stage[0].clip_composite_draw(0 + (int)(Global.g_StageTime / 3 * 2),
                                                       0 + (int)(Texture.P_stage[0].h - Global.g_StageTime),
                                                       (int)(Texture.P_stage[0].w // 3),
                                                       (int)(Texture.P_stage[0].h // 2), 0, "", 250, 400, 500, 800)
        elif (Global.g_Level == 1):
            if (Global.stageback == 1):
                Texture.P_stage[1].clip_composite_draw(0 + (int)(Global.g_StageTime / 3 * 2),
                                                       0 + (int)(Global.g_StageTime), (int)(Texture.P_stage[1].w // 3),
                                                       (int)(Texture.P_stage[1].h // 2), 0, "", 250, 400, 500, 800)
                #if (Global.serve == False):
                Global.g_StageTime = Global.g_StageTime + 1.25*Timer.Time_Frame* Timer.MapCompensatorSpeed
                if (Texture.P_stage[1].h > Global.g_StageTime >= Texture.P_stage[1].h // 2):
                    Global.stageback = -1
            elif (Global.stageback == -1):
                if (Global.g_StageTime >= Texture.P_stage[1].h):
                    pass
                else:
                    Global.g_StageTime = Global.g_StageTime + 1.25*Timer.Time_Frame* Timer.MapCompensatorSpeed
                Texture.P_stage[1].clip_composite_draw(0 + (int)(Global.g_StageTime / 3 * 2),
                                                       0 + (int)(Texture.P_stage[0].h - Global.g_StageTime),
                                                       (int)(Texture.P_stage[1].w // 3),
                                                       (int)(Texture.P_stage[1].h // 2), 0, "", 250, 400, 500, 800)

        if (Global.g_Player.live == True):
            Global.g_Player.Move()
            if (Global.g_Player.forceX > 0):
                Texture.P_player.clip_draw(Global.g_Player.frame * 32, 60 + 50 * 0, 32, 50, Global.g_Player.X,
                                           Global.g_Player.Y)
            elif (Global.g_Player.forceX < 0):
                Texture.P_player.clip_draw(Global.g_Player.frame * 32, 60 + 50 * 1, 32, 50, Global.g_Player.X,
                                           Global.g_Player.Y)
            else:
                Texture.P_player.clip_draw(Global.g_Player.frame * 32, 60 + 50 * 2, 32, 50, Global.g_Player.X,
                                           Global.g_Player.Y)
            Global.g_Player.Draw()
            if (Global.g_Player.slow == True):
                Texture.P_player.clip_draw(0, 0, 65, 65, Global.g_Player.X, Global.g_Player.Y)
            else:
                Texture.P_player.clip_draw(28, 28, 7, 7, Global.g_Player.X, Global.g_Player.Y)

def BulletEffect():
    for eff in Global.elec:
        if(eff.Live == True):
            Texture.P_elec.draw(eff.X,eff.Y,eff.W,eff.H)
            eff.Check();


def MonsterDraw():
    angle = math.radians(1)

    for monster in Global.g_MonsterPool:
        if (monster.live == True):
            if (monster.AttackType == 0):
                Texture.P_Monster.clip_composite_draw(0, 300, 80, 70, monster.Degree * angle, "", monster.X, monster.Y,
                                                      monster.W, monster.H)
            elif (monster.AttackType == 1):
                Texture.P_Monster.clip_composite_draw(80, 300, 75, 69, monster.Degree * angle, "", monster.X, monster.Y,
                                                      monster.W, monster.H)
            elif (monster.AttackType == 2):
                Texture.P_Monster.clip_composite_draw(0, 1350, 80, 75, monster.Degree * angle, "", monster.X, monster.Y,
                                                      monster.W, monster.H)
            elif (monster.AttackType == 3 or monster.AttackType == 4):
                Texture.P_Monster.clip_composite_draw(0, 1350, 80, 75, monster.Degree * angle, "", monster.X, monster.Y,
                                                      monster.W, monster.H)
            elif (monster.AttackType == 5):
                monster.Rotate(monster.Degree + 3)
                Texture.P_player_alpha.clip_composite_draw(65, 0, 65, 65, monster.Degree * angle, "", monster.X,
                                                           monster.Y, monster.W, monster.H)
            else:
                draw_rectangle(monster.X - 50, monster.Y - 50, monster.X + 50, monster.Y + 50)
    if (Global.g_Boss.live == True):
        if((int)(Global.g_Level) == 0):
            Texture.P_Boss1.clip_composite_draw(0, 0, 74, 74, Global.g_Boss.Degree * angle, "", Global.g_Boss.X,
                                            Global.g_Boss.Y, Global.g_Boss.W, Global.g_Boss.H)
        elif((int)(Global.g_Level) == 1):
            Texture.P_Boss2.clip_composite_draw(0, 0, 79, 79, Global.g_Boss.Degree * angle, "", Global.g_Boss.X,
                                            Global.g_Boss.Y, Global.g_Boss.W, Global.g_Boss.H)
        else:
            Texture.P_Boss3.clip_composite_draw(0, 220, 75, 60, Global.g_Boss.Degree * angle, "", Global.g_Boss.X,
                                            Global.g_Boss.Y, Global.g_Boss.W, Global.g_Boss.H)

def LevelDraw():
    global Texture, Global,Timer
    if(Global.stage == "level"):#
        Texture.P_menuback.draw(Global.WindowX/2,Global.WindowY/2,Global.WindowX,Global.WindowY)
        Texture.P_effectlevel.draw(Global.WindowX/2,Global.WindowY/2,Global.WindowX-80,Global.WindowY-80)
        Texture.P_levelselect.draw(390,660,610,170)
        Texture.P_levelselect.draw(390,460,610,170)
        Texture.P_levelselect.draw(390,260,610,170)
        Texture.P_menuside.draw(Global.WindowX/2,Global.WindowY/10*9-50,900,200)
        Texture.P_menuside.draw(Global.WindowX/2,Global.WindowY/10*9-250,900,200)
        Texture.P_menuside.draw(Global.WindowX/2,Global.WindowY/10*9-450,900,200)
        if (640 < Global.MyMouse[0] < 760):
            if (40 < Global.MyMouse[1] < 120):
                Texture.P_okbutton.draw(700,80,130,90)
            else:
                Texture.P_okbutton.draw(700,80,120,80)
        else:
            Texture.P_okbutton.draw(700,80,120,80)

        if (490 < Global.MyMouse[0] < 610):
            if (40 < Global.MyMouse[1] < 120):
                Texture.P_cancelbutton.draw(550, 80, 130, 90)
            else:
                Texture.P_cancelbutton.draw(550, 80, 120, 80)
        else:
            Texture.P_cancelbutton.draw(550, 80, 120, 80)


        if(Timer.IntTime % 2 == 0):
            Texture.P_bullet.clip_draw(625,000, 60, 61, 330, 662, 70, 70)
            Texture.P_bullet.clip_draw(625,000, 60, 61, 450, 662, 70, 70)
            Texture.P_bullet.clip_draw(625,000, 60, 61, 570, 662, 70, 70)
            Texture.P_bullet.clip_draw(625,000, 60, 61, 330, 455, 70, 70)
            Texture.P_bullet.clip_draw(625,000, 60, 61, 450, 455, 70, 70)
            Texture.P_bullet.clip_draw(625,000, 60, 61, 570, 455, 70, 70)

        if(Global.g_Type== 0):
            Texture.P_item.clip_draw(46*3,3+47*1, 45, 46, 330, 662, 70, 70)
        elif(Global.g_Type == 1):
            Texture.P_item.clip_draw(46*3,3+47*1, 45, 46, 450, 662, 70, 70)
        else:
            Texture.P_item.clip_draw(46*3,3+47*1, 45, 46, 570, 662, 70, 70)

        if(Global.g_Hard == 0):
            Texture.P_item.clip_draw(46*3,3+47*1, 45, 46, 330, 455, 70, 70)
        elif(Global.g_Hard == 1):
            Texture.P_item.clip_draw(46*3,3+47*1, 45, 46, 450, 455, 70, 70)
        else:
            Texture.P_item.clip_draw(46*3,3+47*1, 45, 46, 570, 455, 70, 70)
        Texture.P_bullet.clip_composite_draw(150, 190, 30, 85, math.radians(0), "", 340, 655, 15, 55)
        Texture.P_bullet.clip_composite_draw(150, 190, 30, 85, math.radians(0), "", 320, 655, 15, 55)
        Texture.P_bullet.clip_composite_draw(150, 190, 30, 85, math.radians(0), "", 330, 662, 20, 70)

        Texture.P_bullet.clip_composite_draw(120, 190, 30, 85, math.radians(15), "", 435, 655, 15, 55)
        Texture.P_bullet.clip_composite_draw(120, 190, 30, 85, math.radians(-15), "", 465, 655, 15, 55)
        Texture.P_bullet.clip_composite_draw(120, 190, 30, 85, math.radians(0), "", 450, 662, 20, 70)

        Texture.P_bullet.clip_composite_draw(90, 190, 30, 40, math.radians(-25), "", 585, 645, 15, 25)
        Texture.P_bullet.clip_composite_draw(90, 190, 30, 40, math.radians(25), "", 555, 645, 15, 25)
        Texture.P_bullet.clip_composite_draw(90, 230, 30, 40, math.radians(25), "", 585, 675, 15, 25)
        Texture.P_bullet.clip_composite_draw(90, 230, 30, 40, math.radians(-25), "", 555, 675, 15, 25)
        Texture.P_bullet.clip_composite_draw(0, 190, 30, 85, math.radians(0), "", 570, 662, 20, 70)


        Texture.P_bullet.clip_composite_draw(0, 190, 30, 85, math.radians(-45), "", 190, 640, 40, 100)
        Texture.P_bullet.clip_composite_draw(30, 190, 30, 85, math.radians(45), "", 190, 640, 40, 100)
        Texture.P_leveltype.clip_draw(0,50,200,50,450,707,120,30)
        Texture.P_leveltype.clip_draw(0,0,40,50,330,607,50,25)
        Texture.P_leveltype.clip_draw(40,0,40,50,450,607,30,30)
        Texture.P_leveltype.clip_draw(80,0, 40,50,570,607,30,30)
        Texture.P_textlevel[0].draw(190,490,120,60)
        Texture.P_textlevel[1].draw(450,490,120,60)
        Texture.P_textlevel[2].draw(190,690,120,60)
        Texture.P_textlevel[3].draw(190,290,120,60)
        Texture.P_level[0].draw(330, 390, 100, 50)
        Texture.P_level[1].draw(450, 390, 100, 50)
        Texture.P_level[2].draw(570, 390, 100, 50)
        if (Global.g_Level == -1):
            Texture.P_stage[0].clip_draw(Texture.stage_arr[0].HightLight[0],Texture.stage_arr[0].HightLight[1],Texture.stage_arr[0].Size[0],Texture.stage_arr[0].Size[1],190,440,120,100)
        elif(Global.g_Level==0):
            Texture.P_stage[1].clip_draw(Texture.stage_arr[1].HightLight[0],Texture.stage_arr[1].HightLight[1],Texture.stage_arr[1].Size[0],Texture.stage_arr[1].Size[1],190,440,120,100)

            #P_stage[1].clip_draw(stage_arr[0].HightLight[0],stage_arr[0].HightLight[1],stage_arr[0].Size[0],stage_arr[0].Size[1],330,470,100,100)
            #P_stage[2].clip_draw(stage_arr[0].HightLight[0],stage_arr[0].HightLight[1],stage_arr[0].Size[0],stage_arr[0].Size[1],450,470,100,100)
            #P_stage[3].clip_draw(stage_arr[0].HightLight[0],stage_arr[0].HightLight[1],stage_arr[0].Size[0],stage_arr[0].Size[1],570,470,100,100)
        #ITEM draw
        for i in range(0,8):
        #    if(Global.MyItem.inven[i].Num==-1):
        #        temp = random.randint(0,21)
        #        Global.MyItem.inven[i]= ItemIndex[temp]
        #    else:
            ItemDraw(Global.MyItem.inven[i].Num,180+60*i,250,45,45)

        if(Global.Itemshow != -1):
            if((Global.MyItem.inven[Global.Itemshow].Num) != -1):
                Texture.P_menuback.clip_draw(50,50,400,500,360,120,600,150)
                for i in range(0,6):
                    draw_rectangle(60+i*2,195-i,660-i*2,45+i)
            if(Global.MyItem.inven[Global.Itemshow].Num== 17):
                Texture.P_Info.clip_draw(0,1810 - ((Global.MyItem.inven[Global.Itemshow].Num+2)*80+40),1200,120,380,120,600,120)
            elif (Global.MyItem.inven[Global.Itemshow].Num < 17):
                if(Global.MyItem.inven[Global.Itemshow].Num < 6):
                    Texture.P_Info.clip_draw(0,1810 - ((Global.MyItem.inven[Global.Itemshow].Num+1)*80),1200,80,380,120,600,80)
                else:
                    Texture.P_Info.clip_draw(0,1810 - ((Global.MyItem.inven[Global.Itemshow].Num+2)*80),1200,80,380,120,600,80)
            elif(Global.MyItem.inven[Global.Itemshow].Num != 21):
                Texture.P_Info.clip_draw(0,1810 - ((Global.MyItem.inven[Global.Itemshow].Num+2)*80+40),1200,80,380,120,600,80)
            else:
                Texture.P_Info2.clip_draw(0,0,1200,80,380,120,600,80)
            if(Global.MyItem.inven[Global.Itemshow].Level == 0):
                Texture.Font.draw(550,160, "Normal", (255, 255, 255))
            elif(Global.MyItem.inven[Global.Itemshow].Level == 1):
                Texture.Font.draw(550,160, "Rare", (0, 255, 0))
            elif(Global.MyItem.inven[Global.Itemshow].Level == 2):
                Texture.Font.draw(550,160, "Unique", (255, 100, 0))
            elif(Global.MyItem.inven[Global.Itemshow].Level == 3):
                Texture.Font.draw(550,160, "Legend", (255, 255, 0))

def ClearUI_Draw():
    global Global, Texture
    Texture.P_levelselect.clip_draw(0,0,1100,843,250,400,500,600)
    for i in range(0,3):
        ItemDraw(Global.Gift[i].Num, 110+140*i, 450, 65, 65)
        if (Global.Gift[i].Level == 0):
            Texture.Font.draw(80+140*i, 370, "Normal", (255, 255, 255))
        elif (Global.Gift[i].Level == 1):
            Texture.Font.draw(80+140*i, 370, "Rare", (0, 255, 0))
        elif (Global.Gift[i].Level == 2):
            Texture.Font.draw(80+140*i, 370, "Unique", (255, 100, 0))
        elif (Global.Gift[i].Level == 3):
            Texture.Font.draw(80+140*i, 370, "Legend", (255, 255, 0))

    if(Global.Itemshow != -1):
        i = Global.Itemshow
        if (Global.Gift[i].Num == 17):
            Texture.P_Info.clip_draw(0, 1810 - ((Global.Gift[Global.Itemshow].Num + 2) * 80 + 40), 1200, 120,
                                     300, 550, 500, 150)
        elif (Global.Gift[i].Num < 17):
            if (Global.Gift[i].Num < 6):
                Texture.P_Info.clip_draw(0, 1810 - ((Global.Gift[Global.Itemshow].Num + 1) * 80), 1200, 80, 300,
                                         550, 500, 100)
            else:
                Texture.P_Info.clip_draw(0, 1810 - ((Global.Gift[Global.Itemshow].Num + 2) * 80), 1200, 80, 300,
                                         550, 500, 100)
        elif (Global.Gift[i].Num != 21):
            Texture.P_Info.clip_draw(0, 1810 - ((Global.Gift[Global.Itemshow].Num + 2) * 80 + 40), 1200, 80,
                                     300, 550, 500,100)
        else:
            Texture.P_Info2.clip_draw(0, 0, 1200, 80, 300, 550, 500, 100)

    check = False
    for ITEM in Global.MyItem.inven:
        if ITEM.Num == 21:
            check = True
            break

    if(check == True):
        draw_rectangle(110+140*Global.GiftCheck1-65,390,110+140*Global.GiftCheck1+65,500)
        draw_rectangle(110+140*Global.GiftCheck2-65,390,110+140*Global.GiftCheck2+65,500)
    else:
        draw_rectangle(110+140*Global.GiftCheck1-65,390,110+140*Global.GiftCheck1+65,500)

    if (150 < Global.MyMouse[0] < 350):
        if (250 < Global.MyMouse[1] < 350):
            Texture.P_nextbutton.clip_draw(0,0,614,138,250,300,220,110)
        else:
            Texture.P_nextbutton.clip_draw(0,0,614,138,250,300,200,100)
    else:
        Texture.P_nextbutton.clip_draw(0,0,614,138,250,300,200,100)

def shoot():
    global Global
    for Arr in Global.g_BulletArr:
        if (Arr.Draw == True):
            if (Arr.Type == 2):
                TargetTemp = (Global.g_Player.X, 850)
                for Monster in Global.g_MonsterPool:
                    if Monster.live == True:
                        if Global.g_Player.Y + 125 < Monster.Y :
                            if Arr.Y < Global.g_Player.Y +255:
                                TargetTemp = (Monster.X, Monster.Y)
                                break

                if (TargetTemp[1] == 850):
                    Arr.AutoShoot(Arr.X, TargetTemp[1])
                else:
                    Arr.AutoShoot(TargetTemp[0], TargetTemp[1])

            elif (Arr.Type == 0):
                Arr.Shoot(0, 0)
            else:
                (Arr.Shoot(Arr.DirX, Arr.DirY))

def CreateBullet():
    global Global,Timer
    if (Global.g_Level >= 0):
        if (Global.g_ATT == True):
            Global.g_BulletCnt = Global.g_BulletCnt + 1
            if (Global.g_BulletCnt > Global.g_BulletDelay):
                Bulletlenth = 50 // Global.g_Player.BulletNum
                BulletTemp = 1
                PosTemp = -1
                for Arr in Global.g_BulletArr:
                    if (Arr.Draw == False):
                        if(Global.MyItem.Check(10)):
                            if BulletTemp == 1 or BulletTemp == Global.g_Player.BulletNum:
                                Arr.Set(Global.g_Player.X + Bulletlenth * (
                                        -Global.g_Player.BulletNum // 2 + BulletTemp),
                                        Global.g_Player.Y + 8 * (PosTemp), Global.g_Type,
                                        Global.g_Player.BulletSpeed,
                                        Bulletlenth * (-Global.g_Player.BulletNum // 2 + BulletTemp) // 10, 800,
                                        Global.g_Player.BulletPower / 2)
                            else:
                                Arr.Set(Global.g_Player.X + Bulletlenth * (
                                        -Global.g_Player.BulletNum // 2 + BulletTemp),
                                        Global.g_Player.Y + 8 * (PosTemp), 0, Global.g_Player.BulletSpeed,
                                        Bulletlenth * (-Global.g_Player.BulletNum // 2 + BulletTemp) // 10, 800,
                                        Global.g_Player.BulletPower)
                        if (Global.g_Type != 2):
                            Arr.Set(
                                Global.g_Player.X + Bulletlenth * (-Global.g_Player.BulletNum // 2 + BulletTemp),
                                Global.g_Player.Y + 8 * (PosTemp), Global.g_Type, Global.g_Player.BulletSpeed,
                                Bulletlenth * (-Global.g_Player.BulletNum // 2 + BulletTemp) // 10, 800,
                                Global.g_Player.BulletPower)
                        else:
                            if BulletTemp == 1 or BulletTemp == Global.g_Player.BulletNum:
                                Arr.Set(Global.g_Player.X + Bulletlenth * (
                                        -Global.g_Player.BulletNum // 2 + BulletTemp),
                                        Global.g_Player.Y + 8 * (PosTemp), Global.g_Type,
                                        Global.g_Player.BulletSpeed,
                                        Bulletlenth * (-Global.g_Player.BulletNum // 2 + BulletTemp) // 10, 800,
                                        Global.g_Player.BulletPower / 2)
                            else:
                                Arr.Set(Global.g_Player.X + Bulletlenth * (
                                        -Global.g_Player.BulletNum // 2 + BulletTemp),
                                        Global.g_Player.Y + 8 * (PosTemp), 0, Global.g_Player.BulletSpeed,
                                        Bulletlenth * (-Global.g_Player.BulletNum // 2 + BulletTemp) // 10, 800,
                                        Global.g_Player.BulletPower)

                        BulletTemp = BulletTemp + 1
                        PosTemp = PosTemp * (-1)
                    if (BulletTemp == Global.g_Player.BulletNum + 1):
                        Global.g_BulletCnt = 0
                        break

def BulletDraw():
    global Global,Texture
    # draw Bullet

    for Arr in Global.g_BulletArr:
        if (Arr.Draw == True):

            if Global.MyItem.Check(3) or Global.MyItem.Check(20):
                if(Global.MyItem.Check(20)):
                    Texture.P_bullet2.clip_draw(2, 0, 31,21, Arr.X, Arr.Y, 17, 17)
                else:
                    Texture.P_bullet.clip_draw(385, 137, 22, 22, Arr.X, Arr.Y, 17, 17)


            else:
                if (Arr.Type == 1):
                    Texture.P_bullet.clip_draw(363, 137, 22, 22, Arr.X, Arr.Y, 17, 17)
                elif (Arr.Type == 0):
                    Texture.P_bullet.clip_draw(533, 220, 17, 27, Arr.X, Arr.Y, 12, 22)
                else:
                    Texture.P_bullet.clip_draw(425, 160, 25, 20, Arr.X, Arr.Y, 14, 14)

    for Arr in Global.g_MonsterBulletArr:
        if(Arr.Live == True):
            Arr.Move()
            if(Arr.Type == 0):
                Texture.P_bullet.clip_draw(Arr.Type * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)
            elif(Arr.Type == 1):
                Texture.P_bullet.clip_draw(Arr.Type * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)
            elif(Arr.Type == 2):
                Texture.P_bullet.clip_draw(Arr.Type * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)
            elif(Arr.Type == 3):
                Texture.P_bullet.clip_draw(Arr.Type * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)
            elif(Arr.Type == 4):
                Texture.P_bullet.clip_draw(Arr.Type * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)
            elif(Arr.Type == 5):
                Texture.P_bullet.clip_draw(5 * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)
            elif (Arr.Type == 6):
                Texture.P_bullet.clip_draw(5 * 63, 0, 62, 64, Arr.X, Arr.Y, Arr.W, Arr.H)


def Input():
    events = get_events()
    handle_events(events)


def ItemDraw(num,x,y,sx,sz):
    i = 0
    if(num == i):
        Texture.P_item.clip_draw(46 * 11, 3 + 47 * 2, 45, 45,  x, y, sx,sz)  # 0
    i += 1
    if(num == i):
        Texture.P_item.clip_draw(46 * 0, 3 + 47 * 3, 45, 45,  x,y, sx,sz)  # 1
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 0, 3 + 47 * 1, 45, 45, x,y, sx,sz)  # 2
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 0, 3 + 47 * 0, 45, 45, x,y, sx,sz)  # 3
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 12, 3 + 47 * 3, 40, 45, x,y,sx,sz)  # 4
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(782, 650, 40, 45, x,y, sx,sz)  # 5
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 2, 4 + 46 * 12, 45, 46, x,y, sx,sz)  # 6
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 7, 4 + 46 * 0, 45, 46, x,y, sx,sz)  # 7
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 7, 4 + 46 * 1, 45, 46, x,y, sx,sz)  # 8
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 7, 4 + 46 * 3, 45, 46, x,y, sx,sz)  # 9
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 2, 4 + 46 * 16, 44, 45, x,y, sx,sz)  # 10
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(780, 0 + 47 * 5, 40, 45, x,y,sx,sz)  # 11

    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 3, 4 + 46 * 12, 45, 46, x,y, sx,sz)  # 12
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 2, 4 + 46 * 0, 45, 46, x,y, sx,sz)  # 13
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 8, 4 + 46 * 0, 45, 46, x,y, sx,sz)  # 14
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 12, 4 + 46 * 2, 45, 46, x,y, sx,sz)  # 15
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 6, 4 + 46 * 0, 44, 45, x,y, sx,sz)  # 16
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(774, 4 + 46 * 4, 45, 45, x,y, sx,sz)  # 17
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 2, 4 + 46 * 1, 45, 46, x,y, sx,sz)  # 18
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 1, 4 + 46 * 13, 45, 46,x,y, sx,sz)  # 19
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 2, 4 + 46 * 3, 44, 45, x,y, sx,sz)  # 20
    i += 1
    if (num == i):
        Texture.P_item.clip_draw(46 * 4, 4 + 46 * 13, 44, 45, x,y, sx,sz)  # 20
