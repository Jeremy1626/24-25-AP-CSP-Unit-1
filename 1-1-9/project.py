import turtle as trtl
import random as rd
from random import randint

# sky code here (makes background with just a really big circle)
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
    if sray%2 == 0:
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
sun.penup()
sun.goto(-420, 320)
sun.pendown()
sun.circle(3)
# draw mouth
sun.penup()
sun.goto(-420, 300)
sun.down()
sun.right(60)
sun.circle(20, 180)
sun.up()

# ground code
#Finished
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

#cloud code
# cloud set-up
global cloudpen
cloudpen = trtl.Turtle()
cloudpen.color('white')
cloudpen.speed(0)
global x
global y

# Defining the cloud function
def drawcloud():
    global x,y
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
        if puff%2 == 0:
            y = 340 + variancey
        else:
            y = 300 + variancey

#DRAW THE CLOUD
# Initial coords
x = 400
y = 300
drawcloud()

# house code
house = trtl.Turtle()





# the loop stuff to keep it there
wn = trtl.Screen()
wn.mainloop()