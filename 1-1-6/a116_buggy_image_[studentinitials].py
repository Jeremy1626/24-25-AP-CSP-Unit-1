#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
cirlce = trtl.Turtle()
cirlce.pensize(40)
cirlce.circle(20)
legs = 6
leg_length = 70
angle = 380 / legs
cirlce.pensize(5)
n = 0
while (n < legs):
  cirlce.goto(0, 0)
  cirlce.setheading(angle * n)
  cirlce.forward(leg_length)
  n = n + 1
cirlce.hideturtle()
wn = trtl.Screen()
wn.mainloop()