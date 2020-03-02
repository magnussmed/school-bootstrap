from PIL import Image
import multiprocessing as mp
import os

class Point( object ) :
	def __init__( self ) :
		self.photo = Image.open( "assets/img/3.jpg" )
		self.width, self.height = self.photo.size

		mp.Process( target = self.bottom_middle ).start()
		mp.Process( target = self.middle_top ).start()

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
				print( "Bottom-middle average: {} ({},{},{})".format(average, r, g, b) )
				print( "Bottom-middle: {}, {}".format(x, y) )
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
