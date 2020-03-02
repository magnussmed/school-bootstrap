from PIL import Image
from multiprocessing import Process
import os

class Point( object ) :
	def __init__( self ) :
		self.photo = Image.open( "assets/img/3.jpg" )
		self.width, self.height = self.photo.size

		p1 = Process( target = self.middle_top )
		p2 = Process( target = self.bottom_middle )
		p1.start()
		p2.start()

	def bottom_middle( self ) :
		width = int( self.width )
		height = int( self.height / 2 )

		for x in range( 0, width ) :
			for y in range( 0, height ) :
				r, g, b = self.photo.getpixel(( x, y ))
				average = int( sum([r, g, b]) / 3 )
				if average < 50 :
					print(r,g,b)
					print(x,y)
					break
				#print( "Bottom-middle average: {} ({},{},{})".format(average, r, g, b) )
				#print( "Bottom-middle: {}, {}".format(x, y) )
			else :
				continue
			break

	def middle_top( self ) :
		width = int( self.width )
		height = int( self.height / 2 )

		for x in range( 0, width ) :
			for y in range( height, self.height ) :
				r, g, b = self.photo.getpixel(( x, y ))
				average = int( sum([r, g, b]) / 3 )
				if average < 50 :
					print(r,g,b)
					print(x,y)
					break
				#print( "Middle-top average: {} ({},{},{})".format(average, r, g, b) )
				#print( "Middle-top: {}, {}".format(x, y) )
			else :
				continue
			break


if __name__ == '__main__' :
	point = Point()
