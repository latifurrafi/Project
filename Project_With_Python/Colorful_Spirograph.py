import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    return (r, g, b)

def draw(size_of_draw):
    for _ in range(int(360 / size_of_draw)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_draw)

draw(5)

screen = t.Screen()
screen.exitonclick()



