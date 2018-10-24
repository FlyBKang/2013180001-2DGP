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
#텍스쳐를 불러옵니다.


def handle_events():
    global stage,MyMouse,ClickCnt
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
            print("click")
            for i in range(0,50):
                ClickStar[i].live = True
                ClickStar[i].Life = 30
                ClickStar[i].X = event.x
                ClickStar[i].Y = WindowY -event.y
                ClickStar[i].dirX = ClickStar[i].dirY = 0
            ClickCnt = 0

        if(stage == "main"):
            if event.type == SDL_MOUSEBUTTONDOWN:
                if (100 < MyMouse[0] < 700):
                    if (400 < MyMouse[1] < 500):
                        stage = "level"
        elif(stage == "level"):
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
                if event.key == SDLK_ESCAPE:
                    stage = "serve"

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
        #P_main.draw(WindowX/2,WindowY/2,WindowX,WindowY)
        if(g_Player.live == True):
            g_Player.Move()
            if(g_Player.forceX > 0):
                P_player.clip_draw(g_Player.frame * 32, 60+50*0,32,50,g_Player.X,g_Player.Y)
            elif (g_Player.forceX < 0):
                P_player.clip_draw(g_Player.frame * 32, 60+50*1,32,50,g_Player.X,g_Player.Y)
            else:
                P_player.clip_draw(g_Player.frame * 32, 60+50*2,32,50,g_Player.X,g_Player.Y)
            g_Player.Draw()
            P_player.clip_draw(0,0,65,65,g_Player.X,g_Player.Y)
    elif(stage == "level"):#
        P_menuback.draw(WindowX/2,WindowY/2,WindowX,WindowY)
        P_menuside.draw(WindowX/2,WindowY/10*9-50,900,200)
        P_menuside.draw(WindowX/2,WindowY/10*9-250,900,200)
        P_menuside.draw(WindowX/2,WindowY/10*9-450,900,200)
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
    if(ClickCnt < 40):
        print(ClickCnt)
        ClickCnt = ClickCnt+1
        for i in range(0,50):
            print(math.sin(angle * float(360/50*i)))
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