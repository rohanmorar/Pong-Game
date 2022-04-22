from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

# create display
display = Screen()
display.bgcolor("black")
display.setup(width=800, height = 600)
display.title("Pong")
display.tracer(0)

# create left and right paddles
lPaddle = Paddle((-350,0))
rPaddle = Paddle((350,0))

# create ball
ball = Ball()


# up/down for right player, w/s for left player - controls
display.listen()
display.onkey(rPaddle.moveUp, "Up")
display.onkey(rPaddle.moveDown, "Down")
display.onkey(lPaddle.moveUp, "w")
display.onkey(lPaddle.moveDown, "s")


game_is_on = True
while game_is_on:
	display.update()

display.exitonclick()



