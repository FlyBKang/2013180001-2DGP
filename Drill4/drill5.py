from pico2d import *
#10개의 (x,y) 좌표로 구성된 경로를 따라 움직이는 캐릭터 구현
#작성일 2018 09 17
#작성자 강현웅
#2Dprogram수업

arr = [203,535,132,243,535,470,203,715,136,316,225,510,92,692,518,682,336,712,349]
myX,myY = arr[0],arr[1]

def Move2Pos(x,y):#캐릭터 이동을 정의합니다.
    global myX.myY
    Col_X = x - myX
    Col_Y = y - myY
    
    
while(True):
    
