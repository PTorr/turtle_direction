import turtle
from time import sleep
import numpy as np
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def draw_line(t, p1, p2):
    t.penup()
    t.goto(p1)
    t.pendown()
    t.goto(p2)
    t.penup()

def main(name):
    screen = turtle.Screen()
    turtle.bgcolor("black")
    turtle.title('Siren DOA')

    ### add car
    image = "car.gif"

    # add the shape first then set the turtle shape
    screen.addshape(image)
    t2 = turtle.Turtle()
    t2.speed(50)
    t2.shape(image)
    t2.left(200)


    r = 200
    t1 = turtle.Turtle()
    t1.speed(1000000)
    t1.hideturtle()
    t1.color('white')

    n = 32
    for a in range(n):
        ang = (np.pi * 360/n * a) / 180
        p1 = (np.cos(ang) * r, np.sin(ang) * r)
        if a % 2:
            rr = 10
        else:
            rr = 20
        p2 = (np.cos(ang) * (r+rr), np.sin(ang) * (r+rr))
        draw_line(t1, p1, p2)

    ### write the directions
    t1.home()
    for p, direction in zip([(0, r+25), (-r-60, -25), (0, -r-70), (r+70, -25)], ['Forward', 'Left', 'Rear', 'Right']):
        t1.penup()
        t1.goto(p)
        t1.write(direction, font=('Arial', 30, 'normal'), align="center")
    t1.home()

    ### Draw the circle
    t1.home()
    t1.goto(0,-r)
    t1.pendown()
    # t1.circle(r)

    # ### mock rotation
    # t = turtle.Turtle()
    # t.shape('arrow')
    # S = 3
    # t.shapesize(S,S,S)
    # t.color('white')
    # sleep(1)
    # SA = 135 # starting angle
    # dA = 10 # hoe much the angle changed
    # t.rt(SA)
    # for i in range (10):
    #     sleep(.2)
    #     if S == 3:
    #         S = 4
    #         c = 'red'
    #     else:
    #         S = 3
    #         c = 'white'
    #     t.shapesize(S,S,S)
    #     t.color(c)
    #     t.rt(dA)

    ### mock rotation
    t = turtle.Turtle()
    t.hideturtle()
    t.shape('circle')
    S = 1
    t.shapesize(S, S, S)
    t.color('white')
    sleep(1)

    a0 = 235
    af = 135
    # for a in range(50):
    while a0 > af:
        a0 -=1
        ang = (np.pi / 180) * a0
        p1 = (np.cos(ang) * r+30, np.sin(ang) * r+30)
        t.penup()
        t.goto(p1)
        t.showturtle()
        if S == 1:
            S = 1.5
            c = 'red'
        else:
            S = 1
            c = 'white'
        t.shapesize(S,S,S)
        t.color(c)
        sleep(.1)

    turtle.done()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = turtle.getscreen()
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
