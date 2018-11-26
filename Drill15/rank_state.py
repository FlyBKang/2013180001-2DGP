import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import world_build_state
import json

name = "RankState"
Ranking = []

def enter():
    global Ranking
    Ranking.clear()
    with open('rank.pickle', 'rb') as f:
        arr = pickle.load(f)
    for temp in arr:
        Ranking.append((float)(temp))
    Ranking.sort(reverse=True)
    print(Ranking)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)


def update():
    pass


font = None
def draw():
    clear_canvas()
    global Ranking, font
    if font is None:
        font = load_font('ENCR10B.TTF', 20)
    for i in range(9):
        font.draw(50,400-20*(i+2), '# '+str(i+1)+'( Time: %3.2f)' % (Ranking[i]), (0, 0, 0))
    font.draw(50, 400 - 20 * (9 + 2), '#' + str(9 + 1) + '( Time: %3.2f)' % (Ranking[9]), (0, 0, 0))
    update_canvas()






