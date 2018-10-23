import math
import random

class Monster:
    live = False
    frame = 0
    def __init__(self, x,y,degree,framesize):
        self.X = x
        self.Y = y
        self.Degree = degree
        self.frame = 0
        self.framesize = framesize
    def SetPos(self, x,y):
        self.X = x
        self.Y = y
    def Rotate(self, degree):
        self.Degree = degree
    def Draw(self):
        self.frame = (self.frame+1)%self.framesize


class Player:
    live = True
    frame = 0
    slow = False
    def __init__(self,x,y,life,speed,framesize):
        self.X = x
        self.Y = y
        self.Life = life
        self.Speed = speed
        self.forceX = 0
        self.forceY = 0
        self.framesize = framesize
    def Move(self):
        if(self.slow == True):
            self.X = self.X + self.forceX*self.Speed*0.5
            self.Y = self.Y + self.forceY*self.Speed*0.5
        else:
            self.X = self.X + self.forceX*self.Speed
            self.Y = self.Y + self.forceY*self.Speed

        if((0 < self.X < 600) == False):
            if(self.slow == True):
                self.X = self.X - self.forceX*self.Speed*0.5
            else:
                self.X = self.X - self.forceX * self.Speed

        if((0 < self.Y < 800) == False):
            if(self.slow == True):
                self.Y = self.Y - self.forceY*self.Speed*0.5
            else:
                self.Y = self.Y - self.forceY * self.Speed
    def Draw(self):
        self.frame = (self.frame + 1) % self.framesize
        if (self.forceX != 0):
            if(self.frame == self.framesize-1):
                self.frame = 4

class Effect:
    live = False
    def __init__(self,x,y,Lifetime,desX,desY,w,h):
        self.X = x
        self.Y = y
        self.Life = Lifetime
        self.desx = desX
        self.desy = desY
        self.Wsize = w
        self.Hsize = h
        self.dirX = (self.desx - self.X) // self.Life
        self.dirY = (self.desy - self.Y) // self.Life
    def Move(self):
        if(self.live == True):
            self.X = self.X + self.dirX
            self.Y = self.Y + self.dirY
            self.Life= self.Life-1
            if(self.Life <= 0):
                self.live = False
    def RandomSetting(self,life,MaxX,MaxY):
        self.X = random.randint(0,MaxX)
        self.Y = random.randint(0,MaxY)
        self.dirX = 0
        self.dirY = 0
        self.Life = life



