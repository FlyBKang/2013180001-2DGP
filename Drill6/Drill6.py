# 작성일 2018 09 18
# 작성자 강현웅
# 2Dprogram수업

from pico2d import *

W = 800
H = 800

open_canvas(W, H)
background = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')
ClickX,ClickY = 0,0
MouseX,MouseY = 0,0
myX, myY, frame = 400, 400, 0
running = True
move = True
n = 0
hide_cursor()
def Move2Pos(x, y):  # 캐릭터 이동을 방향을 정의합니다.
    global myX, myY, frame,n
    global ClickX,ClickY,move

    Col_X, Col_Y = 0, 0
    def MoveRight():
        global myX, myY
        myX = myX + 1

    def MoveLeft():
        global myX, myY
        myX = myX - 1

    def MoveUp():
        global myX, myY
        myY = myY + 1

    def MoveDown():
        global myX, myY
        myY = myY - 1

    if (x - myX < 0):  # 이전값과 비교
        Col_X = -1
    else:
        Col_X = 1
    if (y - myY < 0):
        Col_Y = -1
    else:
        Col_Y = 1


    if (Col_X > 0):
        MoveRight()
    elif (Col_X < 0):
        MoveLeft()
    if (Col_Y > 0):
        MoveUp()
    elif (Col_Y < 0):
        MoveDown()
    n = Col_X
    if (myX - 2 < x < myX + 2):
        Col_X = 0
    if (myY - 2 < y < myY + 2):
        Col_Y = 0
    if (Col_X == Col_Y == 0):
        move = True

def handle_events():
    global running,move
    global ClickX,ClickY,MouseX, MouseY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:  # key down
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            move = False
            ClickX, ClickY = event.x-20, H - 1 - event.y+20
        elif event.type == SDL_MOUSEMOTION:
            MouseX, MouseY = event.x, H - 1 - event.y

while (True):
    clear_canvas()
    background.draw(W/2,H/2)

    if (n > 0):
        character.clip_draw(frame * 100, 100, 90, 90, myX, myY)
    else:
        character.clip_draw(frame * 100, 0, 90, 90, myX, myY)
    mouse.draw(MouseX,MouseY )
    if(move == False):
        Move2Pos(ClickX,ClickY)


    update_canvas()
    handle_events()
    frame = (frame+1) % 8
    if(running == False):
        break

close_canvas()

