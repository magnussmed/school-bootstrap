import re
from urllib import urlopen

def get_list( tag, url ) :
	total  = 0
	page   = urlopen( url )

	words = []

	for line in page:
		hit   = re.findall( '<'+tag+'.*?>', str( line ) )
		words.append( hit );

	with open("danish-words.txt", "w") as txt_file:
		for line in words:
			txt_file.write(" ".join(line) + "\n")

get_list( 'div style="font-size:3em; color:#6200C5;"', 'https://dr.dk' )
