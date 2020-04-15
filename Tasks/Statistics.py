# Statistics Class
class Statistics( object ) :
	def __init__( self ) :

		# Retrieve the input
		self.numbers = self.getInput()
		print( 'Your final input: {} ' .format( self.numbers ) )
		print( '----------------------------------------------------------------' )



		# Get the sum
		sum = self.sum()
		print( 'Sum: {}' .format( sum ) )

		# Get the median
		median = self.median()
		print( 'Median: {}' .format( median ) )

		# Get the average
		average = self.average( sum )
		print( 'Average: {}' .format( average ) )

		# Get the lowest and highest number
		difference = self.difference()
		print( 'Lowest number: {}' .format( difference[0] ) )
		print( 'Highest number: {}' .format( difference[1] ) )

		# Get the standard deviation
		deviation = self.standardDeviation( average )
		print( 'Standard deviation: {}' .format( deviation ) )


	def getInput( self ) :

		numbers = []

		print( 'Give me some numbers!' )
		print( 'When you are done, simply type "k" and the query will process' )

		while True :
			inputted = input( 'Type number:' )

			if inputted == 'k' :
				break

			if inputted.isdigit() == True :
				numbers.append( int(inputted) )
				print( 'Your current input: {}' .format( numbers ) )
			else :
				print( 'Please type a number' )

		print( '----------------------------------------------------------------' )
		print( '----------------------------------------------------------------' )

		return numbers

	def sum( self ) :

		return sum(self.numbers)

	def median( self ) :
		set = self.numbers
		set.sort()
		mid = len( set ) // 2
		median = ( set[ mid ] + set[ ~mid ] ) / 2

		return median

	def average( self, sum ) :

		average = sum / len(self.numbers)

		return average

	def difference( self ) :

		diff = [ min(self.numbers), max(self.numbers) ]

		return diff

	def standardDeviation( self, average ) :
		variation = sum( [ ( ( x - average ) ** 2 ) for x in self.numbers ] ) / len( self.numbers )
		deviation = variation ** 0.5

		return deviation

if __name__ == '__main__' :
	stats = Statistics()
