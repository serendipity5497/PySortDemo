import numpy as np

def insertionsort(arr, st, end):
	for i in range(st, end+1):
		key = arr[i]
# Move elements of arr[0..i-1], that are
# greater than key, to one position ahead
# of their current position
		j = i-1
		while j >=0 and key < arr[j] :
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	return arr

def Flashsort(a):
	a = np.asarray(a)
	a = map(int, a)
	#print "length of array", len(a)
	min_ = a[0]
	max_ = 0

	for i in range(0,len(a)):
		if(a[i]<min_):
			min_ = a[i]
		if(a[i]>max_):
			max_ = a[i]
	#print min_, ":", max_

	m = int(0.1*len(a)) + 2

	c1 = float(m-1)/(max_ - min_)
	c2 = min_

	l = []
	for k in range(0,m):
		l.append(0)

	l = np.zeros(m)

	for i in range(0,len(a)):
		diff = int((a[i] - c2)*c1)
		#print a[i],": class :", diff
		l[diff] = l[diff] + 1
	

	for k in range(1,m): 
		l[k]=l[k] + l[k-1];
	for k in range(0,m):
		l[k] = l[k] - 1
	count = 0
	item = a[0]

	while(count<len(a)):
		diff = int((item - c2)*c1)
		end = int(l[diff])
		new_item = a[end]
		#print item, "is replacing", new_item
		a[end] = item
		item = new_item
		#print l
		l[diff] = l[diff] - 1
		count = count + 1
		#print a, item
	#print a

	for i in range(0,len(l)):
		l[i] = l[i] + 1
	for i in range(0,len(l)):
		st = int(l[i])
		if i == len(l) - 1:
			end = len(a) -1
		else: 
			end = int(l[i+1]-1)
		a = insertionsort(a,st,end)
	return a

if __name__=="__main__":
	a = raw_input().split()
	sorted_list = Flashsort(a)
	print sorted_list
	