
from turtle import Turtle, Screen
import random
scout = Turtle()

colours = ["red", "yellow", "lime green", "blue", "magenta", "dark violet", "dark orange", "light slate gray", "cyan"]


def draw(num_sides):
    scout.pencolor(random.choice(colours))
    scout.pensize(2)
    scout.speed(1)
    angle = 360 / num_sides
    for _ in range(num_sides):
        scout.forward(100)
        scout.right(angle)


for sides in range(3,11):
    draw(sides)

screen = Screen()
screen.exitonclick()
