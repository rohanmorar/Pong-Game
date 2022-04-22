from turtle import Turtle

# allow paddle to inherit from Turtle class 
class Paddle(Turtle):
	def __init__(self, start_pos):
		super().__init__()
		self.shape("square")
		self.fillcolor("white")
		self.shapesize(stretch_wid=5,stretch_len=1)
		self.penup()
		self.goto(start_pos)

	def moveUp(self):
		new_y = self.ycor() + 25
		self.goto(self.xcor(), new_y)

	def moveDown(self):
		new_y = self.ycor() - 25
		self.goto(self.xcor(), new_y)



