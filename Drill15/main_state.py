import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import json
import rank_state

import world_build_state
name = "MainState"


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

boy = None
zombie_list=None

def enter():
    # game world is prepared already in world_build_state
    global boy, zombie_list
    boy = world_build_state.get_boy()
    zombie_list = world_build_state.zombie_list

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    global boy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            boy.end_time = get_time() - boy.start_time
            print(boy.end_time)
            game_world.save()
        else:
            boy.handle_event(event)


def update():
    global zombie_list
    for game_object in game_world.all_objects():
        game_object.update()
    for Zom in zombie_list:
        if collide(boy,Zom):
            print("Boom")
            import pickle
            text = None
            read_data = []
            with open('rank.pickle', 'rb') as f:
                read_data = pickle.load(f)
            data = (str)(get_time()-boy.start_time)
            read_data.append(data)
            with open('rank.pickle', 'wb') as f:
                pickle.dump(read_data, f)
            game_framework.change_state(rank_state)
            break







def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






