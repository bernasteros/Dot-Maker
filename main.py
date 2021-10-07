import colorgram
from random import choice
from turtle import Turtle, Screen


def random_rgb(image):
    """Analyses the picture in the image file and returns a random color from it"""

    rgb_colors = []
    colors = colorgram.extract(image, 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    return rgb_colors


def offset(object, x, y):
    """"""
    object.penup()
    object.setx(x)
    object.sety(y)
    object.pendown()


def dot_go(object, dot_color):
    object.dot(20, dot_color)
    object.penup()
    object.forward(50)
    object.pendown()


# Start Program here

hirst_team = []
random_color = random_rgb('ohSpQQS.jpg')
my_screen = Screen()
my_screen.colormode(255)

for i in range(10):
    y_offset = i * 50
    new_painter = Turtle()
    offset(new_painter, -200, -200 + y_offset)
    new_painter.speed("fastest")
    hirst_team.append(new_painter)

for dot in hirst_team:
    for i in range(10):
        dot_go(dot, choice(random_color))

my_screen.exitonclick()
