# Calendar Class
class Calendar( object ) :
	def __init__( self ) :

		# First calendar meetings
		self.firstC = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
		self.firstBound = ['9:00', '20:00']

		# Second calendar meetings
		self.secondC = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
		self.secondBound = ['10:00', '18:30']

		# Possible meeting duration
		self.duration = 30

		# Sample output:
		# [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]

		result = self.availability()

	def compare( self, a ) :
		fr = []
		for i in a[0] :
			print(i)
			fr.append(self.realtime( i, i[+1] ))

		print(fr)

	def availability( self ) :

		# For each current meeting --> get end time and start time from next in loop
		first = []
		for c, n in zip( self.firstC, self.firstC[1:] ) :
			if c[1] != n[0] :
				diff = self.realtime( c[1], n[0] )
				if diff >= self.duration :
					first.append( [c[1], n[0]] )

		#print( "Ledige tidsrum first: {}".format( first ) )

		# For each current meeting --> get end time and start time from next in loop
		second = []
		for c, n in zip( self.secondC, self.secondC[1:] ) :
			if c[1] != n[0] :
				diff = self.realtime( c[1], n[0] )
				if diff >= self.duration :
					second.append( [c[1], n[0]] )

		#print("Ledige tidsrum second: {}".format(second))

		return first, second


	def realtime( self, c, n ) :

		start = c.split(':')
		end = n.split(':')

		start = (int(start[0]) * 60) + int(start[1])
		end = (int(end[0]) * 60) + int(end[1])

		return end - start

if __name__ == '__main__' :
	point = Calendar()
