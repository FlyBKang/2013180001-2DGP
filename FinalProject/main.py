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
P_startbutton = load_image("startbutton.png")
#텍스쳐를 불러옵니다.


def handle_events():
    global stage,MyMouse
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            stage = "serve"
        if(stage == "main"):
            if event.type == SDL_MOUSEMOTION:
                MyMouse = (event.x,WindowY-event.y)
                num = g_Time%50
                MouseStar[num].X = event.x + random.randint(-5,6)
                MouseStar[num].Y = WindowY-event.y + random.randint(-5,6)
                MouseStar[num].dirX = MouseStar[num].dirY = 0
                MouseStar[num].Life = random.randint(8,16)
                MouseStar[num].live = True
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



while(True):
    handle_events()
    clear_canvas()
    if(stage == "main"):
        P_main.clip_draw(0+g_Time,0,WindowX,WindowY,WindowX//2,WindowY//2)
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
        P_main.draw(g_Player.X,g_Player.Y,90,90)
    elif(stage == "end"):
        break
    delay(0.033)

    ##main menu
    print(MyMouse)
    if(100 <MyMouse[0] <700):
        if(400<MyMouse[1]<500):
            P_startbutton.draw(WindowX/2,WindowY-350,620,110)
        else:
            P_startbutton.draw(WindowX/2,WindowY-350,600,100)
    else:
        P_startbutton.draw(WindowX / 2, WindowY - 350, 600, 100)
    ##main menu

    ##main Effect
    for i in range(0,300):
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
                P_light1.composite_draw(math.radians(random.randint(0, 360)), '', MouseStar[i].X,MouseStar[i].Y, MouseStar[i].Wsize, MouseStar[i].Hsize)
            else:
                P_light2.composite_draw(math.radians(random.randint(0, 360)), '', MouseStar[i].X,MouseStar[i].Y, MouseStar[i].Wsize, MouseStar[i].Hsize)
            MouseStar[i].Move()

    ##main Effect
    draw_rectangle(MyMouse[0]-25,MyMouse[1]-25,MyMouse[0]+25,MyMouse[1]+25)
    if(g_TimeCheck == False):
        g_Time = g_Time+1
        if(g_Time > 5000):
            g_TimeCheck = True
    else:
        g_Time = g_Time-1
        if(g_Time < 0):
            g_TimeCheck = False
    update_canvas()



close_canvas()