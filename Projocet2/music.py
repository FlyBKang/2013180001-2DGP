from pico2d import *
from globalParamiter import *
first = False

class Music:
    def __init__(self):
        self.mysound = 32
        self.mystage = "main"
        self.boss = False
        self.main_bgm = load_music("music\\tavern_loop.mp3")
        self.stage1_bgm = load_music("music\\stage3.mp3")
        self.stage2_bgm = load_music("music\\stage2.mp3")
        self.boss_bgm = load_music("music\\boss.mp3")

        self.main_bgm.set_volume(self.mysound)
        self.stage1_bgm.set_volume(self.mysound)
        self.stage2_bgm.set_volume(self.mysound)
        self.boss_bgm.set_volume(self.mysound)

    def play_bgm(self,stage):
        global first, Global

        if(first== False):
            first = True
            self.main_bgm.repeat_play()
        elif(Global.g_Boss.live == True):
            if(self.boss == False):
                self.StopOther()
                self.boss_bgm.play(1)
                self.boss = True
        elif (self.mystage != stage):
            if(stage == "main" or stage == "level"):
                if (self.mystage == "main" or stage == "level"):
                    pass
                else:
                    self.StopOther()
                    self.main_bgm.repeat_play()
            if(stage == "stage"):
                self.StopOther()
                if(Global.g_Level == 0):
                    self.stage1_bgm.repeat_play()
                elif(Global.g_Level == 1):
                    self.stage2_bgm.repeat_play()
            self.mystage = stage
            self.boss = False


    def StopOther(self):
        self.main_bgm.stop()
        self.stage1_bgm.stop()

sound = Music()