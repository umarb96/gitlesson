from turtle import Turtle


Umar = Turtle()
Umar.color('red')
Umar.shape('turtle')


Umar.penup()
Umar.goto(-160, 100)
Umar.pendown()

ivo = Turtle()
ivo.color('blue')
ivo.shape('turtle')

ivo.penup()
ivo.goto(-160, 70)
ivo.pendown()

liam = Turtle()
liam.color('green')
liam.shape('turtle')

liam.penup()
liam.goto(-160, 40)
liam.pendown()

from random import randint

for movement in range(100):
    Umar.forward(randint(1,5))
    ivo.forward(randint(1,5))
    liam.forward(randint(1,5))


