# Your name: Cassidy McKenna
# Your student id: I'm not sure if my student ID works for collage but I'm guessing it doesn't. my high school ID is 316296
# Your email: kittycatmckenna@gmail.com
# List who or what you worked with on this homework: I worked by myself and made an emoji
# If you used Generative AI, say that you used it and also how you used it.

from turtle import *





### WRITE ALL NEW FUNCTIONS HERE ###

def head(t1):
    t1.fillcolor("yellow")
    t1.begin_fill()
    t1.circle(90)
    t1.end_fill()

def eye(t1,x,y):
    t1.setheading(0)
    t1.penup()
    t1.goto(x,y)
    t1.left(60)
    t1.fillcolor("red")
    t1.begin_fill()
    for i in range(4):
        t1.forward(20)
        t1.left(120)
    t1.end_fill()
    t1.begin_fill()
    t1.forward(8)
    t1.left(90)
    t1.forward(4)
    t1.setheading(0)
    t1.forward(5)
    t1.circle(8)
    t1.end_fill()
    t1.setheading(180)
    t1.forward(20)
    t1.setheading(0)
    t1.forward(5)
    t1.begin_fill()
    t1.circle(8)
    t1.end_fill()

def mouth(t1,x,y):
    t1.penup()
    t1.goto(x,y)
    t1.fillcolor("black")
    t1.begin_fill()
    t1.setheading(270)
    t1.circle(30,extent = 180)
    t1.end_fill()



def draw_emoji(turtle):
    head(turtle)
    eye(turtle,-45,90)
    eye(turtle,45,90)
    mouth(turtle,-30,90)
    """
    Write a function to draw your favorite or most frequently used emoji using the passed turtle.
    """




def main():
    space = Screen()
    t1 = Turtle()
    t1.speed(0)
    space.bgcolor("light blue")
    draw_emoji(t1)
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