import turtle as turtle

from random import randint

turtle.speed(0)

turtle.bgcolor('black')

x = 1

while x < 400:

	r = randint(0,255) #makes variables r,g,b whose value is an integer,
	g = randint(0,255) # which is between 0 and 255. It is random, and
	b = randint(0,255) # changes every time the loop runs

	turtle.colormode(255) # this is something that is irrelevant at this point
			   # check the pythondocs link at the end for more info


	turtle.pencolor(r,g,b) # changes the color of the pen to the rgb coordinates
					# obtained by the variables r, g, b changing each time

	turtle.fd(50 + x)
	turtle.rt(90.911)


	x = x+1

turtle.exitonclick()
