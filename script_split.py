# Simple script to split whole pgn into individual game files with names game{1, 2, 3, ...}
# Author: Jishan Shaikh
# Last updated: May 26, 2022

with open('lichess_magnus2.pgn') as fp:
	contents = fp.read()
	count = 1
	for content in contents.split('\n\n\n'):
		file = "game{}.txt".format(count)
		count = count + 1
		with open(file, 'w+') as df:
			df.write(content)
		# For testing
		# if(count > 2):
		# 	break

