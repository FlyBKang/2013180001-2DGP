from pico2d import *

open_canvas(800,800)

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
for i in range(0,800):
    delay(0.1) 
    character.draw_now(i, 90)

close_canvas()

