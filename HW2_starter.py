# Your name: Cassidy McKenna
# Your student id: N/A
# Your email: kittycatmckenna@gmail.com
# List who or what you worked with on this homework: I worked with turtles
# If you used Generative AI, say that you used it and also how you used it.

from turtle import *
import random
### WRITE ALL NEW FUNCTIONS HERE ###

def background(t, space, colors):
    space.bgcolor(colors["blue"])
    t.penup()
    t.goto(400,-400)
    t.setheading(90)
    t.fillcolor(colors["white"])
    t.begin_fill()
    t.circle(400,extent = 180)
    t.end_fill()

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
        

def draw_winter_scene(t, space, colors):
    background(t, space, colors)
    snow(t, colors)
    """
    Write a function to draw a winter scene using the passed turtle.

    You can earn extra credit for including you initials (in block letters) in your drawing.
    See the instructions for more details.
    """




def main():
    colors = {"white": "#F8FCFF","blue": "#C3E1FF" }
    turtle = Turtle()
    turtle.shape("turtle")
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