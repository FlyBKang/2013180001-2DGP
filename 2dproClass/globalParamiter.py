import pico2dtest as container

#stage = title, main, level, stage, serve, end
stage = "main"
prev_stage = "main"
slow = False

#main menu


g_Player = container.Player
g_MonsterPool = [container.Monster(-1,-1,0,0)for i in range(1,100)]
WindowX = WindowY = 800
