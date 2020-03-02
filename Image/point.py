from PIL import Image
import multiprocessing as mp
import collections
import os

# Point Class
class Point( object ) :
	def __init__( self ) :
		# Set image
		self.photo = Image.open( "assets/img/2.jpg" )
		self.width, self.height = self.photo.size

		# Photo average color
		self.average = self.average()

		# Set confidence percentage
		self.conf = 0.25

		# Start middle to top and bottom to middle simultaneously
		self.p1 = mp.Process( target = self.middle_top ).start()
		self.p2 = mp.Process( target = self.bottom_middle ).start()
	#	p1.start()
	#	p2.start()


	def terminate( self, who ) :
		if who == 'p1' :
			self.p1.mp.terminate()
		else :
			self.p2.mp.terminate()

	# Get average color from image
	# For each pixel get the RGB colorset and get average value afterwards
	#
	# Return int color
	def average( self ) :

		colors = []
		average = 0
		counter = []
		for c in self.photo.getdata() :
			average = int(sum( list(c) ) / 3)
			colors.append(average)

		return round(sum(colors) / len(colors))

	# From the bottom to the middle
	# For each pixel from the bottom of the image to the middle
	# searching for an interesting change in color from average
	#
	# Return string
	def bottom_middle( self ) :
		width = int( self.width )
		height = int( self.height / 2 )

		# For each x from 0 to total width
		for x in range( 0, width ) :
			# For each y from 0 to half height
			for y in range( 0, height ) :
				r, g, b = self.photo.getpixel(( x, y ))
				average = int( sum([r, g, b]) / 3 )

				# Break if the current average color is above image average * confience percentage
				# or if it is under image average * confience percentage
				if int( self.average + (self.conf * self.average) ) > average < int( self.average - (self.conf * self.average) ) :
					print(r,g,b)
					print("x: {}, y: {}".format(x,y))
					self.terminate( 'p1' )
					break

				# Uncomment below if you like
				# print( "Bottom-middle average: {} ({},{},{})".format(average, r, g, b) )
				# print( "Bottom-middle: {}, {}".format(x, y) )
			else :
				continue
			break

	# From the middle to the top
	# For each pixel from the bottom of the image to the middle
	# searching for an interesting change in color from average
	#
	# Return string
	def middle_top( self ) :
		width = int( self.width )
		height = int( self.height / 2 )

		# For each x from 0 to total width
		for x in range( 0, width ) :
			# For each y from half height to full height
			for y in range( height, self.height ) :
				r, g, b = self.photo.getpixel(( x, y ))
				average = int( sum([r, g, b]) / 3 )

				# Break if the current average color is above image average * confience percentage
				# or if it is under image average * confience percentage
				if int( self.average + (self.conf * self.average) ) > average < int( self.average - (self.conf * self.average) ) :
					print(r,g,b)
					print("x: {}, y: {}".format(x,y))
					self.terminate( 'p2' )
					break

				# Uncomment below if you like
				# print( "Middle-top average: {} ({},{},{})".format(average, r, g, b) )
				# print( "Middle-top: {}, {}".format(x, y) )
			else :
				continue
			break


if __name__ == '__main__' :
	point = Point()
