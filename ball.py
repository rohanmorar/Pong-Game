from turtle import Turtle

# allow ball to inherit from Turtle class 
class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.fillcolor("white")
		self.penup()
		self.goto(0,0)
		self.x_move = 10
		self.y_move = 10
		self.sleep_factor = 0.1

	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce_y(self):
		self.y_move *= -1

	def bounce_x(self):
		self.x_move *= -1
		self.sleep_factor *= 0.9

	def reset_position(self):
		self.goto(0,0)
		self.sleep_factor = 0.1
		self.bounce_x()






