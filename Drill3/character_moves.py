from pico2d import *
import math


W = 800
H = 800

open_canvas(W,H)

character = load_image('character.png')
UNIT = 40
half_UNIT = 20
x = W/2
y = UNIT
Angle = (float)(math.radians(1))

while True:
    while (x < W-half_UNIT):
        clear_canvas_now()
        character.draw_now(x, y)
        x = x + 5
        delay(0.01)
    

    while (y < H-UNIT):
        clear_canvas_now()
        character.draw_now(x, y)
        y = y + 5
        delay(0.01)

    while (x > half_UNIT):
        clear_canvas_now()
        character.draw_now(x, y)
        x = x - 5
        delay(0.01)


    while (y > UNIT):
        clear_canvas_now()
        character.draw_now(x, y)
        y = y - 5
        delay(0.01)


    while (x < W/2):
        clear_canvas_now()
        character.draw_now(x, y)
        x = x + 5
        delay(0.01)

    
    for i in range(0,360):
        clear_canvas_now()
        character.draw_now(math.sin(Angle*(180 - i))*W/2+W/2, math.cos(Angle*(180-i
                                                                              ))*H/2+H/2 )

    

close_canvas()

