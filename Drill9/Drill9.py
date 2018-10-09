from pico2d import *
import random
H = V = 800
open_canvas(H,V)
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
small_ball = load_image("ball21x21.png")
big_ball = load_image("ball41x41.png")

class boy:
    def __init__(self, X, Y, Speed):
        self.x = X
        self.y = Y
        self.speed = Speed
    def move(self):
        if(self.x < H+40):
            self.x = self.x  + self.speed

class ball:
    def __init__(self, X,Y,Size,Speed):
        self.x = X
        self.y = Y
        self.size = Size
        self.speed = Speed

    def drop(self):
        if(self.size == 1):
            if(self.y > 75):
                self.y = self.y - self.speed
            else:
                self.y = 75
        else:
            if(self.y > 65):
                self.y = self.y - self.speed
            else:
                self.y = 65

ball_arr = [ball(random.randint(0,H),V,random.randint(0,1),random.randint(2,6)) for i in range(0,20)]
boy_arr = [boy(0 - random.randint(0,600),90,4) for i in range(0,20)]
frame = 0
while True:
    clear_canvas()
    grass.draw(400, 30)
    for i in range(0,20):
        if(ball_arr[i].size == 1):
            big_ball.draw(ball_arr[i].x,ball_arr[i].y)
        else:
            small_ball.draw(ball_arr[i].x,ball_arr[i].y)
        character.clip_draw(frame * 100, 100, 100, 100,boy_arr[i].x,boy_arr[i].y)
        boy_arr[i].move()
        ball_arr[i].drop()
    delay(0.01)
    frame = (frame+1)%8

    update_canvas()


close_canvas()
