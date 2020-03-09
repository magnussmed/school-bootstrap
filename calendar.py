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

	def compare( self, a ) :
		t = []
		for a, b, c, d in zip( a[0], a[1], a[2], a[3] ):
			diff = b[1] - d[0]
			if diff >= self.duration :
				t += c[0], a[1]

		return t

	def availability( self ) :
		# For each current meeting --> get end time and start time from next in loop
		first = []
		firstReal = []
		for c, n in zip( self.firstC, self.firstC[1:] ) :
			if c[1] != n[0] :
				rt = self.realtime( c[1], n[0] )
				diff = rt[1] - rt[0]
				if diff >= self.duration :
					first.append( [c[1], n[0]] )
					firstReal.append( [rt[0], rt[1]] )

		# For each current meeting --> get end time and start time from next in loop
		second = []
		secondReal = []
		for c, n in zip( self.secondC, self.secondC[1:] ) :
			if c[1] != n[0] :
				rt = self.realtime( c[1], n[0] )
				diff = rt[1] - rt[0]
				if diff >= self.duration :
					second.append( [c[1], n[0]] )
					secondReal.append( [rt[0], rt[1]] )

		return first, firstReal, second, secondReal

	def realtime( self, c, n ) :
		start = c.split(':')
		end = n.split(':')

		start = ( int( start[0] ) * 60 ) + int( start[1] )
		end = ( int( end[0] ) * 60 ) + int( end[1] )

		return start, end

if __name__ == '__main__' :
	point = Calendar()
