from PIL import Image
import multiprocessing as mp
import os

def photo() :
	start = os.getcwd()
	img = Image.open( "assets/img/1.jpg" )
	width, height = img.size

	return [width, height, img]

def bottom_middle( photo ) :
	width = int(photo[0])
	height = int(photo[1]/2)

	for x in range( 0, width ) :
		for y in range( height, 0, -1 ) :
			r, g, b = photo[2].getpixel((x, y))
			average = int(sum([r, g, b])/3)
			if average < 150 :
				print(r,g,b)
				break
			print( "Bottom-middle average: {} ({},{},{})".format(average, r, g, b) )
			print( "Bottom-middle: {}, {}".format(x, y) )
		else :
			continue
		break

def middle_top( photo ) :
	width = int(photo[0])
	height = int(photo[1]/2)

	for x in range( 0, photo[0] ) :
		for y in range( height, photo[1] ) :
			r, g, b = photo[2].getpixel((x, y))
			average = int(sum([r, g, b])/3)
			if average < 150 :
				print(r,g,b)
				break
			print( "Middle-top average: {} ({},{},{})".format(average, r, g, b) )
			print( "Middle-top: {}, {}".format(x, y) )
		else :
			continue
		break

if __name__=='__main__':
	photo = photo()
	p1 = mp.Process( target = bottom_middle, args=(photo,) )
	p2 = mp.Process( target = middle_top, args=(photo,) )
	p1.start()
	p2.start()
