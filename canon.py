from random import *
from turtle import *
from base import vector

#Position of the ball
ball = vector(-200, -200)
speed = vector(10, 10)
targets = []

def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

def tap(x, y):
    #respond to screen
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200)/25
        speed.y = (y + 200)/25

def draw():
    # define ball and targets
    clear()
    for target in targets:
        goto(target.x, target.y)
        dot(30, 'blue')
    if inside(ball):
        goto(ball.x, ball.y)
        dot(15, 'red')
        
    update()

def move():
    # movement of ball and target
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
        
    for target in targets:
        #Speed of target's movement
        target.x -= 1
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
    draw()

    for target in targets:
        if not inside(target):
            return
    ontimer(move, 50)

setup(420, 420, 370,0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

        




