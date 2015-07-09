from time import time

def InsertionSort(A):
	start_time = time() # record the starting time
	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while (i >=0) and (A[i] > key):
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	end_time = time() # record the ending time
	elapsed = end_time - start_time
	print "Elapsed time (ms): %s" % (elapsed)
	return A

"""
	ALL THESE BELONG TO THE HEAP SORT
"""
def HeapSort(iterable):
	start_time = time() # record the starting time
	from heapq import heappush, heappop
	h = []
	print "ready.."
	for value in iterable:
	    heappush(h, value)
	end_time = time() # record the ending time
	elapsed = end_time - start_time
	print "Elapsed time (ms): %s" % (elapsed)
	return [heappop(h) for i in range(len(h))]

"""
	ALL THESE BELONG TO THE MERGE SORT
"""
def merge(left, right):
	result=[]
	i, j=0,0
	while(i<len(left) and j<len(right)):
		if(left[i]<=right[j]):
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
 
	result+=left[i:]
	result+=right[j:]
	return result
 
 
def MergeSort(a):
	start_time = time() # record the starting time
	if(len(a)<2):
		return a
	middle=len(a)/2
	left = MergeSort(a[:middle])
	right = MergeSort(a[middle:])
 
	out = merge(left,right)
	end_time = time() # record the ending time
	elapsed = end_time - start_time
	print "Elapsed time (ms): %s" % (elapsed)
	return out