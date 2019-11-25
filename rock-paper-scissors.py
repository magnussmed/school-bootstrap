import random

rock = 1
paper = 2
scissors = 3

def choice() :
	pv = raw_input( "(Game) Rock(1), paper(2) or scissors(3)? " )

	try :
		pv = int(pv)
		if pv > 3 or pv < 1 :
			print "Noob... Read again! Not between"
			return(choice())
		else :
			cv = random.randint( 1, 3 )
			return [ pv, cv ]
	except :
		print "Noob... Read again! Not int"
		return(choice())

def draw( pv, cv ) :
	print "It's a draw!"
	return False

choices = choice()
pv = choices[0]
cv = choices[1]

while pv == cv :
	draw( pv, cv )
	choices = choice()
	pv = choices[0]
	cv = choices[1]

if pv == 1 and cv == 2 :
	print "Spiller vinder"
elif pv == 2 and cv == 3 :
	print "Spiller vinder"
elif pv == 3 and cv == 1 :
	print "Spiller vinder"
else :
	print "Computeren vinder..."
