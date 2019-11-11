import re
from urllib import urlopen

##
# Count a specific html-tag from a requested URL
# @args str: tag contains a given html tag e.g. a, img, div, li
# @args str: url contains a given url to scrape
##
def count_tag( tag, url ) :
	total  = 0
	page   = urlopen( url )

	for line in page:
		hit   = re.findall( '<'+tag+'.*?>', str( line ) )
		total += len(hit)

	print( 'Tag <'+tag+'> total: {1}'.format( url, total ) )


count_tag( 'a', 'https://dr.dk' )
count_tag( 'img', 'https://dr.dk' )
