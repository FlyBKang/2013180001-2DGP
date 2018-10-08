from pico2d import *
import math

class monster:
    def __init__(self, x,y,degree):
        self.X = x
        self.Y = y
        self.Degree = degree
    def Print(self):
        print(self.X,self.Y,self.Degree)
    def Draw(self):
        character.rotate_draw(math.radians(self.Degree),self.X,self.Y,90,90)
    def SetPos(self, x,y):
        self.X = x
        self.Y = y
    def Rotate(self, degree):
        self.Degree = degree
