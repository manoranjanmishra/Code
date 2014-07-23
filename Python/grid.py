#Draw a Grid Problem, Downey Pg 30
def drawgrid(r,c,h,w):
	h=h+1
	w=w+1
	lines=r*h
	while(lines>=0):
		if(lines%h==0):
			#+------+
			space=c*w
			while(space>=0):
				if(space%w==0):
					print "+",
				else:
					print "-",
				space=space-1
			print "\n"
		else:
			#|      |
			space=c*w
			while(space>=0):
				if(space%w==0):
					print "|",
				else:
					print " ",
				space=space-1
			print "\n"
		lines=lines-1
	return "Done!"
print drawgrid(int(raw_input()),int(raw_input()),int(raw_input()),int(raw_input()))