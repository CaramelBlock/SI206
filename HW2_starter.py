# Your name: Cassidy McKenna
# Your student id: N/A
# Your email: kittycatmckenna@gmail.com
# List who or what you worked with on this homework: I worked with turtles
# If you used Generative AI, say that you used it and also how you used it.

from turtle import *
import random
### WRITE ALL NEW FUNCTIONS HERE ###

#creates blue background with white hill
def background(t, space, colors):
    space.bgcolor(colors["blue"])
    t.penup()
    t.goto(400,-400)
    t.setheading(90)
    t.fillcolor(colors["white"])
    t.begin_fill()
    t.circle(400,extent = 180)
    t.end_fill()
# makes random snowflakes with turtle stamp
def snow(t, colors):
    t.penup()
    t.color(colors["white"],colors["white"])
    for i in range(25):
        x = random.randint(-320,320)
        y = random.randint(0,320)
        angle = random.randint(0,359)
        t.goto(x,y)
        t.setheading(angle) 
        t.stamp()
#creates a shoe and can be modified to work for both directions
def boot(t, x, y, dirc, color):
    t.color(color, color)
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.setheading(90)
    t.forward(20)
    t.setheading(dirc) 
    t.forward(10)
    t.setheading(270)
    t.forward(10)
    t.goto(x, y)
    t.end_fill()
    if dirc == 0:
        t.setheading(0)
        t.forward(20)
    t.begin_fill()
    t.setheading(90)
    t.circle(10, extent = 180)
    t.end_fill()
#creates a rectangle
def rect(t, x, y, dirc, hight, width, color):
    t.penup()
    t.setheading(dirc)
    t.goto(x,y)
    t.color(color, color)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(hight)
        t.left(90)
        t.forward(width)
        t.left(90)
    t.end_fill()
#creates a triangle
def tri(t, x, y, dirc, hight, color):
    t.penup()
    t.goto(x,y)
    t.setheading(dirc)
    t.color(color, color)
    t.pendown()
    t.begin_fill()
    for i in range(3):
        t.forward(hight)
        t.right(120)
    t.end_fill()
#creates a circle
def circ(t, x, y, dirc, radius, color):
    t.penup()
    t.goto(x,y)
    t.setheading(dirc)
    t.color(color, color)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
#creates a half circle
def half_circ(t, x, y, dirc, radius, color):
    t.penup()
    t.goto(x,y)
    t.setheading(dirc)
    t.color(color, color)
    t.pendown()
    t.begin_fill()
    t.circle(radius, extent = 180)
    t.end_fill()
 #draws a line   
def line(t,x,y, dirc, length, size, color):
    t.color(color)
    t.pensize(size)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(dirc)
    t.forward(length)
    t.penup()
    t.pensize(1)
#draws a bold C
def draw_c(t, x, y, dirc, color):
    t.penup()
    t.goto(x,y)
    t.setheading(dirc)
    t.pensize(30)
    t.color(color)
    t.pendown()
    for i in range(35):
        t.forward(6)
        t.left(7)
# draws a bold M
def draw_m(t, x, y, dirc, color):
    t.penup()
    t.goto(x,y)
    t.setheading(dirc)
    t.pensize(30)
    t.color(color)
    t.pendown()
    t.forward(90)
    t.right(140)
    t.forward(60)
    t.left(100)
    t.forward(60)
    t.right(140)
    t.forward(90)
#draws the winter scene
def draw_winter_scene(t, space, colors):
    #creates background with random snow
    background(t, space, colors)
    snow(t, colors)
    #boots
    boot(t, -80, -20, 180, colors["black"])
    boot(t, -60, -20, 0, colors["black"])
    #body person:
    #legs and socks
    rect(t, -82, 0, 90, 30, 8, colors["cream"])
    rect(t, -52, 0, 90, 30, 8, colors["cream"])
    rect(t, -82, 0, 90, 10, 8, colors["orange"])
    rect(t, -52, 0, 90, 10, 8, colors["orange"])
    rect(t, -82, 10, 90, 5, 8, colors["yellow"])
    rect(t, -52, 10, 90, 5, 8, colors["yellow"])
    #arms
    line(t, -92, 75, 210, 30, 10, colors["cream"])
    line(t, -52, 75, 0, 30, 10, colors["cream"])
    #body
    tri(t, -120, 30, 60, 100, colors["green"])
    #head
    circ(t, -70, 85, 0, 30, colors["cream"])
    line(t, -100, 112, 270, 3, 10, colors["cream"])
    line(t, -40, 112, 270, 3, 10, colors["cream"])
    #hair
    circ(t, -40, 112, 0, 5, colors["bright pink"])
    circ(t, -100, 112, 0, 5, colors["bright pink"])
    circ(t, -100, 90, 0, 7, colors["bright pink"])
    circ(t, -40, 90, 0, 7, colors["bright pink"])
    circ(t, -40, 80, 0, 5, colors["bright pink"])
    circ(t, -100, 80, 0, 5, colors["bright pink"])
    circ(t, -40, 73, 0, 3, colors["bright pink"])
    circ(t, -100, 73, 0, 3, colors["bright pink"])
    #person hat and bottons
    half_circ(t, -36, 115, 90, 34, colors["orange"])
    circ(t, -70, 150, 0, 10, colors["yellow"])
    circ(t, -70, 65, 0, 3, colors["yellow"])
    circ(t, -70, 45, 0, 3, colors["yellow"])
    line(t, -95, 133, 0, 51, 10, colors["yellow"])
    #sticks for snowman
    rect(t, 20, 100, 200, 50, 8, colors["brown"])
    rect(t, 80, 90, 310, 50, 8, colors["brown"])
    rect(t, 100, 70, 30, 15, 5, colors["brown"])
    rect(t, 0, 90, 260, 15, 5, colors["brown"])
    #snowman body
    circ(t, 50, -50, 0, 60, colors["white"])
    circ(t, 50, 40, 0, 40, colors["white"])
    circ(t, 50, 110, 0, 30, colors["white"])
    #snowman hat
    rect(t, 18, 155, 0, 65, 12, colors["black"])
    rect(t, 28, 167, 0, 45, 8, colors["red"])
    rect(t, 28, 175, 0, 45, 30, colors["black"])
    #snowman deatils:
    #nose
    tri(t, 42, 145, 0, 15, colors["orange"])
    #eyes
    circ(t, 70, 140, 0, 3, colors["black"])
    circ(t, 30, 140, 0, 3, colors["black"])
    #buttons
    for i in range(90,60,-10):
        circ(t, 50, i, 0, 3, colors["black"])
    #snowman mouth
    circ(t, 50, 120, 0, 3, colors["black"])
    circ(t, 60, 124, 0, 3, colors["black"])
    circ(t, 40, 124, 0, 3, colors["black"])
    #kid face:
    #eyes
    circ(t, -55, 105, 0, 3, colors["black"])
    circ(t, -85, 105, 0, 3, colors["black"])
    #mouth
    half_circ(t, -78, 98, 270, 8, colors["black"])
    rect(t, -73, 95, 0, 5, 2, colors["white"])
    #nose
    line(t,-72,105,0, 4,5, colors["black"])
    #blush
    line(t,-88,103,0, 4,5, colors["pink"])
    line(t,-56,103,0, 4,5, colors["pink"])

    #draws initials
    draw_c(t, 180, -207, 150, colors["bright pink"])
    draw_m(t, 220, -295, 90, colors["bright pink"])
    #moves turtle away
    t.color(colors["white"])
    t.penup()
    t.goto(320,320)
    """
    Write a function to draw a winter scene using the passed turtle.

    You can earn extra credit for including you initials (in block letters) in your drawing.
    See the instructions for more details.
    """




def main():
    colors = {"white": "#F8FCFF","blue": "#B3E4FF", "black": "#00143A", "cream": "#FFEEDA", "green": "#00C053", "orange": "#FFA671", "yellow": "#FFD171", "brown": "#7F4500", "red": "#FF4824", "pink": "#FF99A2", "bright pink": "#FF1697"}
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.speed(0)
    space = Screen()
    draw_winter_scene(turtle, space, colors)
    space.exitonclick()
    """
    Make sure to create a Screen object, a Turtle object,
    and call draw_winter_scene.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.
    """





if __name__ == '__main__':
    main()