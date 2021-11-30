def mergesort_return(a):
	a = merge2(a)
	return a

def merge2(a):
	length = len(a)
	if length <= 1:
		return a
	halfway = length // 2
	aLeft = merge2(a[:halfway])
	aRight = merge2(a[halfway:])
	i1, i2 = 0, 0
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