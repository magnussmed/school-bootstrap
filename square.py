import turtle

# to draw a square, or eventually a turtle, you need to do the things below

def draw_square():
	""" draw square for turtles """

	# to draw a square you want to : move forward, turn right,
	#  move forward, turn right,move forward turn right

	brad = turtle.Turtle()
	brad.forward(100)  # forward takes a number which is the distance to move
	brad.right(120)  # turn right
	brad.forward(100)
	brad.right(120)
	brad.forward(100)
	brad.right(120)
	# brad.forward(100)
	# brad.right(90)

window = turtle.Screen()
# this is the background where the turtle will move
window.bgcolor("red") # the color of the window

raw_square()

window.exitonclick()  # click the screen to close it
