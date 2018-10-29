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

class Map:
    HightLight = (200,200)
    Size = (0,0)
    def __init__(self,x,y,w,h):
        self.HightLight = (x,y)
        self.Size = (w,h)

class Player:
    live = True
    frame = 0
    slow = False
    BulletSpeed = 12
    BulletNum = 5
    BulletPower = 2
    def __init__(self,x,y,life,speed,framesize):
        self.X = x
        self.Y = y
        self.Life = life
        self.Speed = speed
        self.forceX = 0
        self.forceY = 0
        self.framesize = framesize
        self.AttCnt = 0
        self.AttDelay = 5
    def Move(self):
        if(self.slow == True):
            self.X = self.X + self.forceX*self.Speed*0.5
            self.Y = self.Y + self.forceY*self.Speed*0.5
        else:
            self.X = self.X + self.forceX*self.Speed
            self.Y = self.Y + self.forceY*self.Speed

        if((10 < self.X < 490) == False):
            if(self.slow == True):
                self.X = self.X - self.forceX*self.Speed*0.5
            else:
                self.X = self.X - self.forceX * self.Speed

        if((20 < self.Y < 780) == False):
            if(self.slow == True):
                self.Y = self.Y - self.forceY*self.Speed*0.5
            else:
                self.Y = self.Y - self.forceY * self.Speed
    def Draw(self):
        self.frame = (self.frame + 1) % self.framesize
        if (self.forceX != 0):
            if(self.frame == self.framesize-1):
                self.frame = 4
    def Attack(self,check):
        if(check == True):
            self.AttCnt = self.AttCnt + 1
            self.Att = True
        else:
            self.AttCnt = 0
            self.Att = False


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

class Item:
    IsHave = False
    def __init__(self,num):
        self.ID = num

class PlayerBullet:
    Draw = False

    def __init__(self,id):
        self.ID = id
        self.Type = 0
        self.Speed = 0
        self.X = 800
        self.Y = 800
    def Shoot(self,DirX,DirY):
        if(self.Draw == True):
            if(self.Type == 0 ):
                if(-10 > self.X or 510 < self.X):
                    self.Draw = False
                elif(-10 > self.Y or 810 < self.Y):
                    self.Draw = False
                else:
                    self.Y = self.Y + self.Speed

            elif(self.Type == 1):
                if(-10  > self.X or 510 < self.X):
                    self.Draw = False
                elif(-10 > self.Y or 810 < self.Y):
                    self.Draw = False
                else:
                    self.Y = self.Y + self.Speed
                    self.X = self.X + DirX

    def AutoShoot(self,TargetX,TargetY):
        if(self.Draw == True):
            if(self.Type == 2):
                if(-10 <self.x or 510 < self.X):
                    self.Draw = False
                elif(-10 <self.Y or 810 < self.Y):
                    self.Draw = False
                else:
                    if(self.TargetX-15 > self.X):
                        self.X = self.X + self.Speed*0.8
                    if(self.X > TargetX+15):
                        self.X = self.X - self.Speed*0.8

                    if(self.TargetY-15 > self.Y):
                        self.Y = self.Y + self.Speed
                    if(self.Y > TargetY+15):
                        self.Y = self.Y - self.Speed

    def Set(self,x,y,type,speed,dirX,dirY):
        self.Draw = True
        self.X = x
        self.Y = y
        self.Type = type
        self.Speed = speed
        self.DirX = dirX
        self.DirY = dirY










