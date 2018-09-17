# 10개의 (x,y) 좌표로 구성된 경로를 따라 움직이는 캐릭터 구현
#   조건1 마지막 점에 다다르면, 그 다음에는 다시 맨 처음 점으로 이동
#   조건2 무한 반복함.
#   조건3 캐릭터의 바라보는 방향(facing direction)을 이동 방향과 일치시켜야 함.

# 작성일 2018 09 17
# 작성자 강현웅
# 2Dprogram수업

from pico2d import *

W = 800
H = 800

open_canvas(W, H)
character = load_image('animation_sheet.png')
arr = [203, 535, 132, 243, 535, 470, 477, 203, 715, 136, 316, 225, 510, 92, 692, 518, 682, 336, 712, 349]
myX, myY, frame = 400, 400, 0


def Move2Pos(x, y):  # 캐릭터 이동을 방향을 정의합니다.
    global myX, myY, frame

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
    print(Col_X, Col_Y)

    def SetDirection(n):
        global myX, myY, frame
        clear_canvas()
        if (n > 0):
            character.clip_draw(frame * 100, 100, 90, 90, myX, myY)
        else:
            character.clip_draw(frame * 100, 0, 90, 90, myX, myY)
        frame = (frame + 1) % 8
        update_canvas()

    while True:
        if (Col_X > 0):
            MoveRight()
        elif (Col_X < 0):
            MoveLeft()
        if (Col_Y > 0):
            MoveUp()
        elif (Col_Y < 0):
            MoveDown()
        SetDirection(Col_X)

        if (myX - 3 < x < myX + 3):
            Col_X = 0
        if (myY - 3 < y < myY + 3):
            Col_Y = 0
        if (Col_X == Col_Y == 0):
            break


while (True):
    for i in range(0, 20, 2):
        print(i, arr[i], i + 1, arr[i + 1])
        Move2Pos(arr[i], arr[i + 1])
        delay(0.5)

close_canvas()

