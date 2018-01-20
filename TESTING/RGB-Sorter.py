for f in L:
	if '-B-' in f:
		if '-R-' in L[L.index(myNumber)-1]:
			RED = L[L.index(myNumber)-1]
		else:
			RED = ''
		if '-G-' in L[L.index(myNumber)+1]:
			GREEN = L[L.index(myNumber)+1]
		else:
			GREEN = ''
	print 'RED = '+RED
	print 'GREEN = 'GREEN
	print 'BLUE = '+f
	print ''



