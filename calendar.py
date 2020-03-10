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

		a = self.availability()
		p = self.compare( a )

		print( p )

	# Compare availability lists and sort out time matches
	#
	# Return list
	def compare( self, a ) :
		t = []
		for a, b, c, d in zip( a[0], a[1], a[2], a[3] ):
			diff = b[1] - d[0]
			if diff >= self.duration :
				bounds = self.realtime( self.firstBound[1], self.secondBound[1] )
				if b[1] < bounds[1] and d[0] < bounds[0] :
					t += c[0], a[1]
				else :
					t += a[0], c[1]
		return t

	# Get each part's availability from their current calendar
	#
	# Return 4 lists with free time in datetime and as minutes
	def availability( self ) :
		# For each current meeting --> get end time and start time from next in loop
		first = []
		firstReal = []
		i = 0
		for c, n in zip( self.firstC, self.firstC[1:] ) :
			if c[1] != n[0] :
				rt = self.realtime( c[1], n[0] )
				diff = rt[1] - rt[0]
				if diff >= self.duration :
					first.append( [c[1], n[0]] )
					firstReal.append( [rt[0], rt[1]] )
					i += 1

		# Add bound preference
		first.append( [self.firstC[i][1], self.firstBound[1]] )
		firstReal.append( self.realtime( self.firstC[i][1], self.firstBound[1] ) )

		# For each current meeting --> get end time and start time from next in loop
		second = []
		secondReal = []
		i = 1
		for c, n in zip( self.secondC, self.secondC[1:] ) :
			if c[1] != n[0] :
				rt = self.realtime( c[1], n[0] )
				diff = rt[1] - rt[0]
				if diff >= self.duration :
					second.append( [c[1], n[0]] )
					secondReal.append( [rt[0], rt[1]] )
					i += 1

		# Add bound preference
		second.append( [self.secondC[i][1], self.secondBound[1]] )
		secondReal.append( self.realtime( self.secondC[i][1], self.secondBound[1] ) )

		return first, firstReal, second, secondReal

	# Takes two datetime e.g. 10:30 inputs and convert them to minutes
	def realtime( self, c, n ) :
		start = c.split(':')
		end = n.split(':')

		start = ( int( start[0] ) * 60 ) + int( start[1] )
		end = ( int( end[0] ) * 60 ) + int( end[1] )

		return start, end

if __name__ == '__main__' :
	point = Calendar()
