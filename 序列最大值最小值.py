import random
def fmam(l):
	if l == []:
		return (None,None)
	else:
		min = l[0]
		max = l[0]
		for i in l:
			if max < i:
				max = i
			if min > i:
				min = i
		return (max, min)
l = list(range(0, 10))
random.shuffle(l)
print(l)
print(fmam(l))
