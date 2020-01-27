import math

def ros() :
	try:
		h = int(input( 'Hvor højt er teltet? (CM)' ))
		b = int(input( 'Hvor bredt er det teltet? (CM)' ))
		l = int(input( 'Hvor langt er teltet? (CM)' ))

		c2 = (h**2) + ((b/2)**2)
		sq = math.sqrt( c2 )
		sides = (l * sq) * 2

		result = [round(sides/l,0), round(l,0)]

		print(result)
		return result
	except :
		print ( 'Noob... Angiv kun tal i CM' )
		return False


result = ros()

print( result )
