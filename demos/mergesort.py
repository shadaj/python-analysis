def merge2(a):
	length = len(a)
	if length <= 1:
		return a
	halfway = length // 2
	aLeft = merge2(a[:halfway])
	aRight = merge2(a[halfway:])
	i1 = 0
	i2 = 0
	# i1, i2 = 0, 0 #This changes the graph
	t = []
	while i1 != halfway or i2 != length - halfway:
		if i1 == halfway:
			t.append(aRight[i2])
			i2 += 1
		elif i2 == length - halfway:
			t.append(aLeft[i1])
			i1 += 1
		else:
			if aLeft[i1] < aRight[i2]:
				t.append(aLeft[i1])
				i1 += 1
			else:
				t.append(aRight[i2])
				i2 += 1
	return t

def merge2_tuples(a):
	length = len(a)
	if length <= 1:
		return a
	halfway = length // 2
	aLeft = merge2_tuples(a[:halfway])
	aRight = merge2_tuples(a[halfway:])
	i1 = 0
	i2 = 0
	# i1, i2 = 0, 0 #This changes the graph
	t = []
	while i1 != halfway or i2 != length - halfway:
		if i1 == halfway:
			t.append(aRight[i2])
			i2 += 1
		elif i2 == length - halfway:
			t.append(aLeft[i1])
			i1 += 1
		else:
			if aLeft[i1][0] < aRight[i2][0]:
				t.append(aLeft[i1])
				i1 += 1
			else:
				t.append(aRight[i2])
				i2 += 1
	return t

def argmerge(a):
	a_index = [(a[i], i) for i in range(len(a))]
	a_index = merge2_tuples(a_index)
	ret = [i[1] for i in a_index]
	return ret
	# return a_index