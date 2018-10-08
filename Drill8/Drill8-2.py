#KPU 배경을 바탕으로 캐릭터의 랜덤 이동 구현 (1점)
# 랜덤으로 임의의 점 10개 지정
# 10개의 점을 부드럽게 이동, 계속해서 반복함.

#KPU 2D프로그래밍 수업중 Drill8-2
#작성일 2018 10 08 작성자 강현웅

from pico2d import *
import random
import math

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

def Move2Pos(x, y,arr):  # 캐릭터 이동을 방향을 정의합니다.
    global myX, myY, frame,points,size
    global ClickX,ClickY,move
    direction = 0
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
        direction = -1
    else:
        Col_X = 1
        direction = 1
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
        for i in range(size):
            draw_rectangle(points[i][0]-10,points[i][1]+10,points[i][0]+10,points[i][1]-10)

        for i in range(len(arr)):
            draw_rectangle(arr[i][0] - 2, arr[i][1] + 2, arr[i][0] + 2, arr[i][1] - 2)

        if (direction > 0):
            character.clip_draw(frame * 100, 100, 90, 90, myX, myY)
        else:
            character.clip_draw(frame * 100, 0, 90, 90, myX, myY)

        update_canvas()
        frame = (frame + 1) % 8

        if (Col_X == Col_Y == 0):
            break;



def draw_line(p1, p2,p3,p4):
    arr = []
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        arr.append((x,y))

    for i in range(0, len(arr)):
        Move2Pos(arr[i][0],arr[i][1],arr)


size = 10
points = [(random.randint(50, W-50), random.randint(50, H-50)) for i in range(size)]

myX = points[3][0]
myY = points[3][1]

num = 0
while True:
    draw_line(points[num - 3], points[num-2],points[num-1],points[num])
    num = (num+1)%size

close_canvas()
