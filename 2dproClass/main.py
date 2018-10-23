from pico2d import*
from  globalParamiter import*
import random
import pico2dtest as container



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
            if event.type == SDL_KEYDOWN:  # key down
                if event.key == SDLK_LSHIFT:
                    slow = True
                if(slow == False):
                    if event.key == SDLK_RIGHT:
                        g_Player.forceX = 1
                    elif event.key == SDLK_LEFT:
                        g_Player.forceX = -1
                    elif event.key == SDLK_UP:
                        g_player.forceY = 1
                    elif event.key == SDLK_DOWN:
                        g_player.forceY = -1
                else:
                    if event.key == SDLK_RIGHT:
                        g_Player.forceX = 0.2
                    elif event.key == SDLK_LEFT:
                        g_Player.forceX = -0.2
                    elif event.key == SDLK_UP:
                        g_player.forceY = 0.2
                    elif event.key == SDLK_DOWN:
                        g_player.forceY = -0.2
                if event.key == SDLK_ESCAPE:
                    stage = "serve"
            elif event.type == SDL_KEYUP:  # key up
                if event.key == SDLK_RIGHT:
                    if event.key == SDLK_LEFT:
                        g_Player.forceX = 0

                if event.key == SDLK_UP:
                    if event.key == SDLK_DOWN:
                        g_Player.forceY = 0

                if event.key == SDLK_LSHIFT:
                    slow = False
        elif(stage == "level"):
            pass
        elif(stage == "stage"):
            if event.type == SDL_KEYDOWN:  # key down
                if event.key == SDLK_LSHIFT:
                    slow = True
                if(slow == False):
                    if event.key == SDLK_RIGHT:
                        g_Player.forceX = 1
                    elif event.key == SDLK_LEFT:
                        g_Player.forceX = -1
                    elif event.key == SDLK_UP:
                        g_player.forceY = 1
                    elif event.key == SDLK_DOWN:
                        g_player.forceY = -1
                else:
                    if event.key == SDLK_RIGHT:
                        g_Player.forceX = 0.2
                    elif event.key == SDLK_LEFT:
                        g_Player.forceX = -0.2
                    elif event.key == SDLK_UP:
                        g_player.forceY = 0.2
                    elif event.key == SDLK_DOWN:
                        g_player.forceY = -0.2
                if event.key == SDLK_ESCAPE:
                    stage = "serve"
            elif event.type == SDL_KEYUP:  # key up
                if event.key == SDLK_RIGHT:
                    if event.key == SDLK_LEFT:
                        g_Player.forceX = 0

                if event.key == SDLK_UP:
                    if event.key == SDLK_DOWN:
                        g_Player.forceY = 0

                if event.key == SDLK_LSHIFT:
                    slow = False
        else:
            pass




while(True):
    handle_events()
    if(stage == "main"):
        P_main.draw(WindowX/2,WindowY/2,WindowX,WindowY)
    elif(stage == "stage"):
        P_main.draw(WindowX/2,WindowY/2,WindowX,WindowY)
    elif(stage == "level"):#
        P_main.draw(g_Player.X,g_Player.Y,90,90)
    elif(stage == "end"):
        break
    update_canvas()



close_canvas()