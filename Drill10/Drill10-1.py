from pico2d import*
import myPause as pause

open_canvas(800,800)

grass = load_image('grass.png')
character = load_image('animation_sheet.png')
frame = 0
x = 0
way = 0
stop = False
def handle():
    global pause
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LSHIFT:
                print("input")
                if(pause.key == False):
                    pause.key = True

def MoveRight():
    global x,frame,way,stop
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)

    x += 5
    frame = (frame + 1) % 8
    if(x > 800):
        way = 1

def MoveLeft():
    global x,frame,way,stop
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)

    x -= 5
    frame = (frame + 1) % 8
    if(x < 0):
        way = 0

time = 0

while True:
    time = (time + 1)%10
    clear_canvas()
    grass.draw(400, 30)

    if(pause.key != True):
        handle()
        if way == 0:
            MoveRight()
        else:
            MoveLeft()
    else:
        pause.handle()
        pause.draw()
    delay(0.01)
    update_canvas()

close_canvas()
