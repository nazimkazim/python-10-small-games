from random import *
from turtle import *
from base import vector

def value():

    #this || generate me value from [-5,-3] to [3,5]

    return (3 + random() * 2 * choice([-1, 1]))
ball = vector(0, 0)
aim = vector(value(), value())

#projection or movement

def draw():
    #move the ball and draw the screen
    ball.move(aim)
    x = ball.x
    y = ball.y

    if x < -200 or x > 200:
        aim.x = -aim.x
    if y < -200 or y > 200:
        aim.y = -aim.y

    clear()
    goto(x, y)
    dot(10)
    ontimer(draw, 50)
        

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
draw()
done()
