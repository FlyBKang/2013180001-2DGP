from pico2d import*
from  globalParamiter import*
import random
import math



open_canvas(WindowX,WindowY )
#텍스쳐를 불러옵니다.
P_main = load_image("main.jpg")
P_player = load_image("character.png")
P_light1 = load_image("Eff_Glitter.png")
P_light2 = load_image("Eff_Glitter2.png")
P_light3 = load_image("Eff_Glitter3.png")
P_light4 = load_image("Eff_Glitter4.png")
P_startbutton = load_image("startbutton.png")
P_exitbutton = load_image("exitbutton.png")
P_bullet = load_image("bullet.png")
P_menuback = load_image("edge.png")
P_menuside = load_image("side.png")
P_mouse = load_image("pointer.png")
P_okbutton = load_image("okbutton.png")
P_cancelbutton = load_image("cancelbutton.png")
P_levelselect = load_image("edge2.png")
P_item = load_image("item.png")
P_effectlevel = load_image("effect_background.png")
P_leveltype = load_image("level_type.png")

P_stage = [load_image("stage1.jpg")]
P_level = [load_image("level_easy.png"),load_image("level_normal.png"),load_image("level_hard.png")]
P_textlevel = [load_image("menu_stage.png"),load_image("menu_level.png"),load_image("menu_attack.png"),load_image("menu_item.png")]
#텍스쳐를 불러옵니다.
stage_arr = [container.Map(0,0,500,800)]

def handle_events():
    global stage,MyMouse,ClickCnt,g_Level,g_Hard,g_Type,serve
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            MyMouse = (event.x, WindowY - event.y)
            num = g_Time % 50
            MouseStar[num].X = event.x + random.randint(-5, 6)
            MouseStar[num].Y = WindowY - event.y + random.randint(-5, 6)
            MouseStar[num].dirX = MouseStar[num].dirY = 0
            MouseStar[num].Life = random.randint(12, 20)
            MouseStar[num].live = True

        if event.type == SDL_MOUSEBUTTONDOWN:
            for i in range(0,50):
                ClickStar[i].live = True
                ClickStar[i].Life = 5
                ClickStar[i].X = event.x
                ClickStar[i].Y = WindowY -event.y
                ClickStar[i].dirX = ClickStar[i].dirY = 0
            ClickCnt = 0

        if(stage == "main"):
            if event.type == SDL_MOUSEBUTTONDOWN:
                if (100 < MyMouse[0] < 700):
                    if (400 < MyMouse[1] < 500):
                        stage = "level"

                if (100 < MyMouse[0] < 700):
                    if (250 < MyMouse[1] < 350):
                        exit(1);

        elif(stage == "level"):
            if event.type == SDL_MOUSEBUTTONDOWN:
                if ( 620 < MyMouse[0] < 780):
                    if (40 < MyMouse[1] < 120):
                        #reset
                        stage = "stage"
                        g_Level = g_Level + 1
                        g_Player.X,g_Player.Y = WindowX / 8 * 2.5, WindowY / 8 * 1

                if ( 490 < MyMouse[0] < 610):
                    if (40 < MyMouse[1] < 120):
                        stage = "main"
                        g_Level = -1

                if(330-70 < MyMouse[0] <330+70):
                    if (470-65 < MyMouse[1] < 470+65):
                        g_Hard = 0

                if(450-70 < MyMouse[0] <450+70):
                    if (470-65 < MyMouse[1] < 470+65):
                        g_Hard = 1

                if(570-70 < MyMouse[0] <570+70):
                    if (470-65 < MyMouse[1] < 470+65):
                        g_Hard = 2

                if(330-70 < MyMouse[0] <330+70):
                    if (670-65 < MyMouse[1] < 670+65):
                        g_Type = 0

                if(450-70 < MyMouse[0] <450+70):
                    if (670-65 < MyMouse[1] < 670+65):
                        g_Type = 1

                if(570-70 < MyMouse[0] <570+70):
                    if (670-65 < MyMouse[1] < 670+65):
                        g_Type = 2

                if(g_Level == -1):
                    pass

        elif(stage == "stage"):
            if event.type == SDL_KEYDOWN:  # key down
                if event.key == SDLK_LSHIFT:
                    g_Player.slow = True
                if event.key == SDLK_RIGHT:
                    g_Player.forceX = 1
                elif event.key == SDLK_LEFT:
                    g_Player.forceX = -1
                elif event.key == SDLK_UP:
                    g_Player.forceY = 1
                elif event.key == SDLK_DOWN:
                    g_Player.forceY = -1

            if event.type == SDL_KEYUP:  # key up
                if event.key == SDLK_LSHIFT:
                    g_Player.slow = False
                if event.key == SDLK_RIGHT:
                    if(g_Player.forceX == 1):
                        g_Player.forceX = 0
                if event.key == SDLK_LEFT:
                    if(g_Player.forceX == -1):
                        g_Player.forceX = 0

                if event.key == SDLK_DOWN:
                    if(g_Player.forceY == -1):
                        g_Player.forceY = 0
                if event.key == SDLK_UP:
                    if(g_Player.forceY == 1):
                        g_Player.forceY = 0

                if event.key == SDLK_ESCAPE:
                    if(serve == True):
                        serve = False
                    else:
                        serve = True
                    print(serve)
        else:
            pass

hide_cursor()
while(True):
    handle_events()
    clear_canvas()
    if(stage == "main"):
        P_main.clip_draw(0+g_Time,0,WindowX,WindowY,WindowX//2,WindowY//2)
        ##main menu
        if (100 < MyMouse[0] < 700):
            if (400 < MyMouse[1] < 500):
                P_startbutton.draw(WindowX / 2, WindowY - 350, 620, 110)
            else:
                P_startbutton.draw(WindowX / 2, WindowY - 350, 600, 100)
        else:
            P_startbutton.draw(WindowX / 2, WindowY - 350, 600, 100)

        if (100 < MyMouse[0] < 700):
            if (250 < MyMouse[1] < 350):
                P_exitbutton.draw(WindowX / 2, WindowY - 500, 620, 110)
            else:
                P_exitbutton.draw(WindowX / 2, WindowY - 500, 600, 100)
        else:
            P_exitbutton.draw(WindowX / 2, WindowY - 500, 600, 100)
        ##main menu
    elif(stage == "stage"):
        if(g_Level == 0):
            if(stageback ==1):
                P_stage[0].clip_composite_draw(0+(int)(g_StageTime/3*2),0+(int)(g_StageTime),(int)(P_stage[0].w//3),(int)(P_stage[0].h//2),0,"",250,400,500,800)
                if(serve == False):
                    g_StageTime = g_StageTime+1
                if(P_stage[0].h > g_StageTime >= P_stage[0].h//2):
                    stageback = -1
            elif(stageback == -1):
                if(g_StageTime >= P_stage[0].h):
                    pass
                else:
                   g_StageTime = g_StageTime + 1
                P_stage[0].clip_composite_draw(0 + (int)(g_StageTime / 3 * 2), 0 + (int)(P_stage[0].h-g_StageTime), (int)(P_stage[0].w // 3), (int)(P_stage[0].h // 2), 0, "", 250, 400, 500, 800)

        if(g_Player.live == True):
            g_Player.Move()
            if(g_Player.forceX > 0):
                P_player.clip_draw(g_Player.frame * 32, 60+50*0,32,50,g_Player.X,g_Player.Y)
            elif (g_Player.forceX < 0):
                P_player.clip_draw(g_Player.frame * 32, 60+50*1,32,50,g_Player.X,g_Player.Y)
            else:
                P_player.clip_draw(g_Player.frame * 32, 60+50*2,32,50,g_Player.X,g_Player.Y)
            g_Player.Draw()
            if(g_Player.slow == True):
                P_player.clip_draw(0,0,65,65,g_Player.X,g_Player.Y)
            else:
                P_player.clip_draw(28,28,7,7,g_Player.X,g_Player.Y)
    elif(stage == "level"):#
        P_menuback.draw(WindowX/2,WindowY/2,WindowX,WindowY)
        P_effectlevel.draw(WindowX/2,WindowY/2,WindowX-80,WindowY-80)
        P_levelselect.draw(390,660,610,170)
        P_levelselect.draw(390,460,610,170)
        P_levelselect.draw(390,260,610,170)

        P_menuside.draw(WindowX/2,WindowY/10*9-50,900,200)
        P_menuside.draw(WindowX/2,WindowY/10*9-250,900,200)
        P_menuside.draw(WindowX/2,WindowY/10*9-450,900,200)
        if (640 < MyMouse[0] < 760):
            if (40 < MyMouse[1] < 120):
                P_okbutton.draw(700,80,130,90)
            else:
                P_okbutton.draw(700,80,120,80)
        else:
            P_okbutton.draw(700,80,120,80)

        if (490 < MyMouse[0] < 610):
            if (40 < MyMouse[1] < 120):
                P_cancelbutton.draw(550, 80, 130, 90)
            else:
                P_cancelbutton.draw(550, 80, 120, 80)
        else:
            P_cancelbutton.draw(550, 80, 120, 80)



        if(g_Type== 0):
            P_item.clip_draw(46*3,3+47*1, 45, 46, 330, 655, 70, 70)
        elif(g_Type == 1):
            P_item.clip_draw(46*3,3+47*1, 45, 46, 450, 655, 70, 70)
        else:
            P_item.clip_draw(46*3,3+47*1, 45, 46, 570, 655, 70, 70)

        if(g_Hard == 0):
            P_item.clip_draw(46*3,3+47*1, 45, 46, 330, 455, 70, 70)
        elif(g_Hard == 1):
            P_item.clip_draw(46*3,3+47*1, 45, 46, 450, 455, 70, 70)
        else:
            P_item.clip_draw(46*3,3+47*1, 45, 46, 570, 455, 70, 70)
        P_bullet.clip_composite_draw(150, 190, 30, 85, math.radians(0), "", 340, 655, 15, 55)
        P_bullet.clip_composite_draw(150, 190, 30, 85, math.radians(0), "", 320, 655, 15, 55)
        P_bullet.clip_composite_draw(150, 190, 30, 85, math.radians(0), "", 330, 662, 20, 70)

        P_bullet.clip_composite_draw(120, 190, 30, 85, math.radians(15), "", 435, 655, 15, 55)
        P_bullet.clip_composite_draw(120, 190, 30, 85, math.radians(-15), "", 465, 655, 15, 55)
        P_bullet.clip_composite_draw(120, 190, 30, 85, math.radians(0), "", 450, 662, 20, 70)

        P_bullet.clip_composite_draw(90, 190, 30, 40, math.radians(-25), "", 585, 645, 15, 25)
        P_bullet.clip_composite_draw(90, 190, 30, 40, math.radians(25), "", 555, 645, 15, 25)
        P_bullet.clip_composite_draw(90, 230, 30, 40, math.radians(25), "", 585, 675, 15, 25)
        P_bullet.clip_composite_draw(90, 230, 30, 40, math.radians(-25), "", 555, 675, 15, 25)
        P_bullet.clip_composite_draw(0, 190, 30, 85, math.radians(0), "", 570, 662, 20, 70)


        P_bullet.clip_composite_draw(0, 190, 30, 85, math.radians(-45), "", 190, 640, 40, 100)
        P_bullet.clip_composite_draw(30, 190, 30, 85, math.radians(45), "", 190, 640, 40, 100)
        P_leveltype.clip_draw(0,50,200,50,450,707,120,30)
        P_leveltype.clip_draw(0,0,40,50,330,607,50,25)
        P_leveltype.clip_draw(40,0,40,50,450,607,30,30)
        P_leveltype.clip_draw(80,0, 40,50,570,607,30,30)
        P_textlevel[0].draw(190,490,120,60)
        P_textlevel[1].draw(450,490,120,60)
        P_textlevel[2].draw(190,690,120,60)
        P_textlevel[3].draw(190,290,120,60)
        P_level[0].draw(330, 390, 100, 50)
        P_level[1].draw(450, 390, 100, 50)
        P_level[2].draw(570, 390, 100, 50)
        if (g_Level == -1):
            P_stage[0].clip_draw(stage_arr[0].HightLight[0],stage_arr[0].HightLight[1],stage_arr[0].Size[0],stage_arr[0].Size[1],190,440,120,100)
            #P_stage[1].clip_draw(stage_arr[0].HightLight[0],stage_arr[0].HightLight[1],stage_arr[0].Size[0],stage_arr[0].Size[1],330,470,100,100)
            #P_stage[2].clip_draw(stage_arr[0].HightLight[0],stage_arr[0].HightLight[1],stage_arr[0].Size[0],stage_arr[0].Size[1],450,470,100,100)
            #P_stage[3].clip_draw(stage_arr[0].HightLight[0],stage_arr[0].HightLight[1],stage_arr[0].Size[0],stage_arr[0].Size[1],570,470,100,100)
    elif(stage == "end"):
        break
    delay(0.033)



    ##main Effect
    if(stage != "stage"):
        for i in range(0,100):
            if(Star_EffectPool[i].live == True):
                if( (i % 2) == 0):
                    P_light1.composite_draw(math.radians(random.randint(0,360)),'',Star_EffectPool[i].X,Star_EffectPool[i].Y,Star_EffectPool[i].Wsize,Star_EffectPool[i].Hsize)
                else:
                    P_light2.composite_draw(math.radians(random.randint(0,360)),'',Star_EffectPool[i].X,Star_EffectPool[i].Y,Star_EffectPool[i].Wsize,Star_EffectPool[i].Hsize)
                Star_EffectPool[i].Move()
            else:
                Star_EffectPool[i].RandomSetting(random.randint(50, 100), WindowX, WindowY)
                Star_EffectPool[i].live = True
    for i in range(0,50):
        if(MouseStar[i].live == True):
            if(i%2 == 0):
                P_light3.composite_draw(math.radians(random.randint(0, 360)), '', MouseStar[i].X,MouseStar[i].Y, MouseStar[i].Life*2, MouseStar[i].Life*2)
            else:
                P_light4.composite_draw(math.radians(random.randint(0, 360)), '', MouseStar[i].X,MouseStar[i].Y, MouseStar[i].Life*2, MouseStar[i].Life*2)
            MouseStar[i].Move()
    angle = float(math.radians(1))
    if(ClickCnt < 35):
        ClickCnt = ClickCnt+1
        for i in range(0,50):
            if ClickStar[i].live == True:
                if(i%2==0):
                    P_light3.composite_draw(math.radians(random.randint(0, 1)), '',
                                            ClickStar[i].X + ClickCnt/2*random.randint(20,100)*0.02 * math.sin(angle * float(360 / 50 * i)),
                                            ClickStar[i].Y + ClickCnt/2*random.randint(20,100)*0.02 * math.cos(angle * float(360 / 50 * i)),
                                            ClickStar[i].Wsize, ClickStar[i].Hsize)
                else:
                    P_light4.composite_draw(math.radians(random.randint(0, 1)), '',
                                            ClickStar[i].X + ClickCnt/2*random.randint(20,100)*0.02 * math.sin(angle * float(360 / 50 * i)),
                                            ClickStar[i].Y + ClickCnt/2*random.randint(20,100)*0.02 * math.cos(angle * float(360 / 50 * i)),
                                            ClickStar[i].Wsize, ClickStar[i].Hsize)

                if(i%2==0):
                    P_light3.composite_draw(math.radians(random.randint(0, 1)), '',
                                            ClickStar[i].X + ClickCnt/2*random.randint(20,100)*0.02 * math.sin(angle * float(360 / 50 * i)),
                                            ClickStar[i].Y + ClickCnt/2*random.randint(20,100)*0.02 * math.cos(angle * float(360 / 50 * i)),
                                            ClickStar[i].Wsize//0.75, ClickStar[i].Hsize//0.75)
                else:
                    P_light4.composite_draw(math.radians(random.randint(0, 1)), '',
                                            ClickStar[i].X + ClickCnt/2*random.randint(20,100)*0.02 * math.sin(angle * float(360 / 50 * i)),
                                            ClickStar[i].Y + ClickCnt/2*random.randint(20,100)*0.02 * math.cos(angle * float(360 / 50 * i)),
                                            ClickStar[i].Wsize//0.75, ClickStar[i].Hsize//0.75)

    ##main Effect
    P_mouse.draw(MyMouse[0],MyMouse[1],100,100)
    if(g_TimeCheck == False):
        g_Time = g_Time+2
        if(g_Time > 5000):
            g_TimeCheck = True
    else:
        g_Time = g_Time-2
        if(g_Time < 0):
            g_TimeCheck = False
    update_canvas()



close_canvas()