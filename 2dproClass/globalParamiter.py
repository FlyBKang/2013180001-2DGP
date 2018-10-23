import pico2dtest as container

#stage = title, main, level, stage, serve, end
stage = "stage"
prev_stage = "main"

#main menu


g_Player = container.Player(300,100,5,8,8)
g_MonsterPool = [container.Monster(-1,-1,0,0)for i in range(1,100)]
WindowX = 1000
WindowY = 800
