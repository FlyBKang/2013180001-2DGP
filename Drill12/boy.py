import game_framework
from pico2d import *
from ball import Ball

import game_world
import random
# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 100.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
ROTATE_METER_TO_PIXEL = 3 * PIXEL_PER_METER
# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE,GHOST = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.timer = 0
        boy.enter_time = get_time()

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.timer = get_time()

        if  boy.timer- boy.enter_time >= 10:
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocity, 1)



    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)


class GhostState:
    @staticmethod
    def enter(boy,event):
        boy.enter_time = get_time()
        boy.timer = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.timer = get_time()
        boy.AlPha()

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw( 0, 300, 100, 100, 3.141592 / 2, '', boy.x - 25,
                                          boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(0, 200, 100, 100, -3.141592 / 2, '', boy.x + 25,
                                          boy.y - 25, 100, 100)
        if(boy.timer - boy.enter_time < 5):
            if boy.dir == 1:
                boy.ghostimage.clip_composite_draw(0, 300, 100, 100, (3.141592 / 2) - (3.141592 / 2 *(boy.timer-boy.enter_time)/5), '', boy.x + 5*(boy.timer - boy.enter_time-5),
                                          boy.y -25 + (10*(boy.timer - boy.enter_time)), 100, 100)
            else:
                boy.ghostimage.clip_composite_draw(0, 200, 100, 100,
                                                   (-3.141592 / 2) + (3.141592 / 2 * (boy.timer - boy.enter_time) / 5),
                                                   '', boy.x - 5 * (boy.timer - boy.enter_time - 5),
                                                   boy.y - 25 + (10 * (boy.timer - boy.enter_time)), 100, 100)
        elif(boy.timer - boy.enter_time < 10):

            if boy.dir == 1:
                boy.ghostimage.clip_composite_draw(0, 300, 100, 100, 0 , '', boy.x,
                                          boy.y+25 + (10*(boy.timer - boy.enter_time-5)) , 100, 100)
            else:
                boy.ghostimage.clip_composite_draw(0, 200, 100, 100, 0 , '', boy.x,
                                          boy.y+25 + (10*(boy.timer - boy.enter_time-5)) , 100, 100)

        else:
            if boy.dir == 1:
                boy.ghostimage.clip_composite_draw(0, 300, 100, 100, 0 , '', boy.x+ROTATE_METER_TO_PIXEL*math.sin(math.radians(720*(boy.timer-boy.enter_time-10))),
                                          boy.y+75+ROTATE_METER_TO_PIXEL*math.cos(math.radians(720*(boy.timer-boy.enter_time-10))) , 100, 100)
            else:
                boy.ghostimage.clip_composite_draw(0, 200, 100, 100, 0 , '', boy.x+ROTATE_METER_TO_PIXEL*math.sin(math.radians(720*(boy.timer-boy.enter_time-10))),
                                          boy.y+75+ROTATE_METER_TO_PIXEL*math.cos(math.radians(720*(boy.timer-boy.enter_time-10))) , 100, 100)

            if(boy.timer-boy.enter_time > 10.5):
                boy.enter_time += 0.5




class SleepState:

    @staticmethod
    def enter(boy, event):
        boy.enter_time = get_time()
        boy.timer = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.timer = get_time()
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if(boy.timer- boy.enter_time >= 5):
            boy.add_event(GHOST)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)






next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState,GHOST: GhostState},
    GhostState: {LEFT_DOWN: RunState, RIGHT_DOWN:RunState,LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        self.ghostimage = load_image('animation_sheet.png')
        self.ghostimage.opacify(0.6)
        # fill here
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.enter_time = 0
    def AlPha(self):
        self.ghostimage.opacify(random.randint(3,8)/10)

    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        # fill here
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

