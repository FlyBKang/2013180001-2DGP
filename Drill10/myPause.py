from pico2d import*

key = False
def handle():
    global key
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RSHIFT:
                key = False

def draw():
    PP = load_image('pause.png')
    PP.clip_draw(300, 200, 300, 500, 400, 400)
