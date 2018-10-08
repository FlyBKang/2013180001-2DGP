#Turtle를 이용해서, 네 점 사이의 부드러운 점찍기 구현(1점)
#points = [(-300, 200), (400, 350),(100,100), (300, -300), (-200, -200)]

#KPU 2D프로그래밍 수업중 Drill8-1
#작성일 2018 10 08 작성자 강현웅

import pico2d
import turtle
import random
import math


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))

color = 0
def draw_point(p):
    global color
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2,p3,p4):
    # fill here
    pass

def draw_line(p1, p2,p3,p4):
    draw_big_point(p2)
    draw_big_point(p3)

    draw_point(p2)
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        draw_point((x, y))
    draw_point(p3)


points = [ (300, -300),(100,100), (-200, -200),(-300, 200), (400, 350)]

size = len(points)
n = 1

prepare_turtle_canvas()

while True:
    for i in range(0,size):
        draw_line(points[i-3],points[i-2],points[i-1],points[i])

turtle.done()
