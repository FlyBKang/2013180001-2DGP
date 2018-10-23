import math


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