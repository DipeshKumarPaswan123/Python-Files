import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Set the dimensions of the flag
width = 1200
height = 600
t.penup()
t.goto(-width/2, height/2)
t.pendown()

# Draw the background color
t.begin_fill()
t.color('#FF9933')
for i in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height/3)
    t.right(90)
t.end_fill()

# Draw the white stripe
t.penup()
t.goto(-width/2, height/6)
t.pendown()
t.begin_fill()
t.color('white')
for i in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height/3)
    t.right(90)
t.end_fill()

# Draw the green stripe
t.penup()
t.goto(-width/2, -height/6)
t.pendown()
t.begin_fill()
t.color('#138808')
for i in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height/3)
    t.right(90)
t.end_fill()

# Draw the Ashoka Chakra in the center of the flag
t.penup()
t.goto(0, 0)
t.pendown()
t.color('navy')
t.pensize(7)
t.circle(height/6, 24)

# Draw the 24 spokes of the Ashoka Chakra
t.penup()
t.goto(0, 0)
t.pendown()
t.color('navy')
t.pensize(2)
for i in range(24):
    t.forward(height/6)
    t.backward(height/6)
    t.left(15)

# Hide the turtle
t.hideturtle()

# Keep the window open until it is manually closed
turtle.done()
