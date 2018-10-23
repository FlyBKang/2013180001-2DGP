from pico2d import*
from  globalParamiter import*
import random



open_canvas(WindowX,WindowY )
#텍스쳐를 불러옵니다.
P_main = load_image("main.jpg")
P_player = load_image("character.png")
#텍스쳐를 불러옵니다.


def handle_events():
    global stage
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            stage = "serve"
        if(stage == "main"):
            pass
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
        P_main.draw(WindowX/2,WindowY/2,WindowX,WindowY)
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
    update_canvas()



close_canvas()