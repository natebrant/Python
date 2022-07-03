#https://stackoverflow.com/questions/55426014/how-to-make-this-wheel-spin
from turtle import Screen, Turtle
# hsv is a way of specifying colors
from colorsys import hsv_to_rgb #converts HSV (Hue Saturation Value) coordinates to RGB (Red Green Blue) coordinates

RADIUS = 300
NUMBER_OF_WEDGES = 15
SLICE_ANGLE = 360 / NUMBER_OF_WEDGES

screen = Screen()
screen.tracer(False)

turtle = Turtle(visible=False)
turtle.penup()
center = turtle.position()

turtle.sety(turtle.ycor() - RADIUS)

hues = [color / NUMBER_OF_WEDGES for color in range(NUMBER_OF_WEDGES)]  # precompute hues

index = 0

def draw_circle():
    global index

    for hue in range(NUMBER_OF_WEDGES):
        turtle.color(hsv_to_rgb(hues[(hue + index) % NUMBER_OF_WEDGES], 1.0, 1.0))

        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(RADIUS, extent=SLICE_ANGLE)
        position = turtle.position()
        turtle.goto(center)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(position)

    screen.update()
    index = (index + 1) % NUMBER_OF_WEDGES
    screen.ontimer(draw_circle, 40)


draw_circle()
screen.exitonclick()