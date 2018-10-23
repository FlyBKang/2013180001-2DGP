import math

class Monster:
    def __init__(self, x,y,degree,framesize):
        self.X = x
        self.Y = y
        self.Degree = degree
        self.frame = 0
        self.framesize = framesize
    def Print(self):
        print(self.X,self.Y,self.Degree)
        frame= (frame+1)%framesize
    def Draw(self):
        character.rotate_draw(math.radians(self.Degree),self.X,self.Y,90,90)
    def SetPos(self, x,y):
        self.X = x
        self.Y = y
    def Rotate(self, degree):
        self.Degree = degree

class Player:
    def __init__(self,x,y,life,speed,framesize):
        self.X = x
        self.Y = y
        self.Life = life
        self.Speed = speed
        self.forceX = 0
        self.forceY = 0
        self.framesize = framesize
    def Move(self,command):
        pass
