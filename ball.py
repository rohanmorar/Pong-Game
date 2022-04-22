from turtle import Turtle

# allow ball to inherit from Turtle class 
class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.fillcolor("white")
		self.penup()
		self.goto(0,0)



