import random
import math
from  globalParamiter import*
from framework import *

#텍스쳐를 불러옵니다.

elapsed_time = 0.00

while(True):
    elapsed_time = get_time()
    clear_canvas()
    Input()
    Draw()
    update_canvas()

    Timer.Time_Frame = get_time() - elapsed_time
    Timer.Sec_Per_Frame += Timer.Time_Frame
    if(Timer.Sec_Per_Frame > Timer.IntTime + 1):
        Timer.IntTime += 1
    #print(Timer.Sec_Per_Frame)
    #print(Timer.IntTime)
    #print(Timer.Time_Frame)
    #print(get_time() - Timer.Time_Start)



