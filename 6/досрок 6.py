from turtle import *
tracer(0)
koef = 20
for x in range(2):
    forward(13 * koef)
    right(90)
    forward(18 * koef)
    right(90)
up()
forward(5 * koef)
right(90)
forward(9 * koef)
left(90)
down()
for y in range(2):
    forward(11 * koef)
    right(90)
    forward(7 * koef)
    right(90)
up()
for z in range(-koef,koef):
    for g in range(-koef,  koef):
        goto(z * koef, g * koef)
        dot(3)
exitonclick()

