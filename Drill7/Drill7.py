# 20개의 임의의(x,y) 좌표로 구성된 경로를 따라 움직이는 캐릭터 구현
#   조건1 마지막 점에 다다르면, 그 다음에는 다시 맨 처음 점으로 이동
#   조건2 무한 반복함.
#   조건3 캐릭터의 바라보는 방향(facing direction)을 이동 방향과 일치시켜야 함.

# 작성일 2018 10 02
# 작성자 강현웅
# 2Dprogram수업

from pico2d import *
import random
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
hide_cursor()

def Move2Pos(x, y):  # 캐릭터 이동을 방향을 정의합니다.
    global myX, myY, frame
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

    while True:
        if (Col_X > 0):
            MoveRight()
        elif (Col_X < 0):
            MoveLeft()
        if (Col_Y > 0):
            MoveUp()
        elif (Col_Y < 0):
            MoveDown()
        if (myX - 2 < x < myX + 2):
            Col_X = 0
        if (myY - 2 < y < myY + 2):
            Col_Y = 0
        clear_canvas()
        background.draw(W / 2, H / 2)
        if (Col_X > 0):
            character.clip_draw(frame * 100, 100, 90, 90, myX, myY)
        else:
            character.clip_draw(frame * 100, 0, 90, 90, myX, myY)

        update_canvas()
        frame = (frame + 1) % 8

        if (Col_X == Col_Y == 0):
            break;

#def handle_events():
#    global running,move
#    global ClickX,ClickY,MouseX, MouseY
#    events = get_events()
#    for event in events:
#        if event.type == SDL_QUIT:
#            running = False
#        elif event.type == SDL_KEYDOWN:  # key down
#            if event.key == SDLK_ESCAPE:
#                running = False
#        elif event.type == SDL_MOUSEBUTTONDOWN:
#            move = False
#            ClickX, ClickY = event.x-20, 800 - 1 - event.y+20
#        elif event.type == SDL_MOUSEMOTION:
#            MouseX, MouseY = event.x, 800 - 1 - event.y

def draw_line(p1, p2):
    global myX, myY, frame, move
    CurveParamiter = 20

    for i in range(0,CurveParamiter+1):
        t = i / CurveParamiter
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        Move2Pos(x,y)


size = 20
points = [(random.randint(100, W-100), random.randint(100, H-100)) for i in range(20)]
num = 1
myX = 50
myY = 600
while True:
    draw_line(points[num - 1], points[num])
    num = (num + 1) % size

close_canvas()

