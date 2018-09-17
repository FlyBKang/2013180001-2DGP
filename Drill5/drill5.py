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
(203, 535), (132, 243), (535, 470), (477, 203), (715, 136), (316, 225), (510, 92), (692, 518), (682, 336), (712, 349)
arr = [203, 535, 132, 243, 535, 470,477, 203, 715, 136, 316, 225, 510, 92, 692, 518, 682, 336, 712, 349]
myX, myY,frame = 0,0,0


def Move2Pos(x, y):  # 캐릭터 이동을 방향을 정의합니다.
    global myX, myY, frame

    Col_X,Col_Y = 0,0
    def MoveRight():
        pass
    def MoveLeft():
        pass
    def MoveUp():
        pass
    def MoveDown():
        pass

    if(x - myX < 0):    #이전값과 비교
        Col_X = -1
    else:
        Col_X = 1
    if(y - myY < 0):
        Col_Y = -1
    else:
        Col_Y = 1

    def SetDirection(n):
        global myX, myY, frame
        clear_canvas()
        if(n>0):
            character.clip_draw(frame * 100, 100, 100, 100, myX, myY)
        else:
            character.clip_draw(frame * 100, 200, 100, 100, myX, myY)
        update_canvas()
        frame = (frame + 1) % 8

    if(Col_X>0):
        MoveRight()
        SetDirection(Col_X)
    else:
        MoveLeft()
        SetDirection(Col_X)

    if(Col_Y>0):
        MoveUp()
    else:
        MoveDown()

while (True):
    for i in range(0,20,2):
        Move2Pos(i,i+1)


close_canvas()
