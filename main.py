from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create display
display = Screen()
display.bgcolor("black")
display.setup(width=800, height = 600)
display.title("Pong")
display.tracer(0)

# create left and right paddles and set their initial coordinates
lPaddle = Paddle((-350,0))
rPaddle = Paddle((350,0))

# create ball
ball = Ball()

# create scoreboard 
scoreboard = Scoreboard()


# up/down for right player, w/s for left player - controls
display.listen()
display.onkey(rPaddle.moveUp, "Up")
display.onkey(rPaddle.moveDown, "Down")
display.onkey(lPaddle.moveUp, "w")
display.onkey(lPaddle.moveDown, "s")


game_is_on = True
while game_is_on:
	time.sleep(ball.sleep_factor)
	display.update()
	ball.move()

	# detect top/bot wall collision

	if ball.ycor() > 280 or ball.ycor() < -280:
		# bounce off wall
		ball.bounce_y()

	# detect right / left paddle collisions
	if ball.distance(rPaddle) < 50 and ball.xcor() > 320 or ball.distance(lPaddle) < 50 and ball.xcor() < -320:
		ball.bounce_x()


	# hit right wall; left player gets a point
	if ball.xcor() > 380:
		ball.reset_position()
		scoreboard.lPoint()

	# hit left wall; right player gets a point
	if ball.xcor() < -380:
		ball.reset_position()
		scoreboard.rPoint()

display.exitonclick()



