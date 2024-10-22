import turtle as trtl
import random as rd
from random import randint

# sky code here (makes background with just a big circle)
# Finished
sky = trtl.Turtle()
sky.speed(0)
sky.color('#00a6ff')
sky.pensize(5000)
sky.circle(100)
sky.hideturtle()

# sun code
# Finished (except smiley face :))
sun = trtl.Turtle()
sun.hideturtle()
sun.speed(0)
sun.pensize(75)
sun.color('yellow')
# Set up sun
sun.penup()
sun.goto(-400, 300)
sun.pendown()
sun.showturtle()
sun.circle(5)
# Code for sun rays
sun.pensize(5)
# sray is shorthand for sun ray
for sray in range(8):
    sun.hideturtle()
    sun.penup()
    sun.goto(-400, 305)
    sun.setheading((sray * 45) + 10)
    sun.forward(60)
    sun.pendown()
    sun.showturtle()
    if sray % 2 == 0:
        sun.forward(40)
    else:
        sun.forward(25)
sun.hideturtle()
# Code for sun smiley face
sun.color('black')
sun.penup()
sun.goto(-385, 320)
sun.pendown()
sun.circle(3)
# eye
sun.penup()
sun.goto(-420, 320)
sun.pendown()
sun.circle(3)
# mouth
sun.penup()
sun.goto(-420, 300)
sun.down()
sun.right(60)
sun.circle(20, 180)
sun.up()

# ground code
# Finished
grass = trtl.Turtle()
grass.hideturtle()
grass.speed(0)
# hex code #3f9b0b is a pretty nice grass color
grass.color('#3f9b0b')
grass.pensize(250)
grass.penup()
grass.goto(-500, -350)
grass.pendown()
grass.showturtle()
grass.forward(1000)
grass.hideturtle()

# cloud code
# Finished
# cloud set-up
global cloudpen
cloudpen = trtl.Turtle()
cloudpen.color('white')
cloudpen.speed(0)
global x
global y


# Defining the cloud function
def drawcloud():
    global x, y
    global cloudpen
    for puff in range(5):
        # The next 2 variables help to randomize the clouds a little bit
        variancex = randint(-10, 5)
        variancey = randint(-10, 0)
        cloudpen.penup()
        cloudpen.goto(x, y)
        cloudpen.pendown()
        cloudpen.pensize(50 + randint(0, 10))
        cloudpen.circle(5)
        x = x + variancex - 20
        if puff % 2 == 0:
            y = y + 40 + variancey
        else:
            y = y - 40 + variancey


# DRAW THE CLOUD
cloud_start_xcoords = [400, 100, -200]
cloud_start_ycoords = [300, 150, 225]
for clouds in range(3):
    x = cloud_start_xcoords[clouds]
    y = cloud_start_ycoords[clouds]
    drawcloud()

# house code
house = trtl.Turtle()
house.color('#000000')
house.pensize(3)
house.speed(0)
house.penup()
house.goto(-175, -225)
house.pendown()
house.setheading(90)
house.begin_fill()
for wall in range(4):
    house.forward(200)
    house.right(90)
house.fillcolor('#f0f0d7')
house.end_fill()

# window
house.color('#000000')
house.speed(0)
house.fillcolor('#40e6ff')
pane_startx = [-150, -150, -120, -120]
pane_starty = [-175, -125, -175, -125]
for pane in range(4):
    house.penup()
    house.goto(pane_startx[pane], pane_starty[pane])
    house.pendown()
    for sill in range(4):

        if sill % 2 == 0:
            dist = 50
        else:
            dist = 30
        house.forward(dist)
        house.right(90)
house.end_fill()

# door

# the loop stuff to keep it there
wn = trtl.Screen()
wn.mainloop()