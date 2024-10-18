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
sun.goto(-395, 320)
sun.pendown()
sun.circle(5)
sun.penup()
sun.goto(-395, 320)
sun.pendown()
sun.circle(5)

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
cloud = trtl.Turtle()
cloud.color('white')
cloud.pensize(50)
x = 400
y = 300

for puff in range(5):
    cloud.penup()
    cloud.goto(400, 300)
    cloud.pendown()
    cloud.circle(5)

'''cloud.penup()
cloud.goto(360, 300)
cloud.pendown()
cloud.circle(5)

cloud.penup()
cloud.goto(350, 340)
cloud.pendown()
cloud.circle(5)

cloud.penup()
cloud.goto(370, 340)
cloud.pendown()
cloud.circle(5)

cloud.penup()
cloud.goto(400, 340)
cloud.pendown()
cloud.circle(5)'''

# house code
house = trtl.Turtle()





# the loop stuff to keep it there
wn = trtl.Screen()
wn.mainloop()