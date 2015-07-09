import os
from time import time


def disk_usage(path):
	"""Return the number of bytes used by a file/folder and any descendents."""
	total = os.path.getsize(path) # account for direct usage
	if os.path.isdir(path): # if this is a directory,
		for filename in os.listdir(path): # then for each child:
			childpath = os.path.join(path, filename) # compose full path to child
			total += disk_usage(childpath)

	print "%s bytes or %s Mb or %s Gb -- for path >>  %s" % (format(total,",d"), format(total//1000000,",d"), format(total/1000000000,",d"), path) # descriptive output (optional)
	return total # return the grand total

def binary_sum(S, start, stop):
	"""Return the sum of the numbers in implicit slice S[start:stop]."""
	if start >= stop: # zero elements in slice
		return 0
	elif start == stop - 1: # one element in slice
		return S[start]
	else: # two or more elements in slice
		mid = (start + stop) // 2
	return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

def binary_search(S, target):
	"""Return the sum of the numbers in implicit slice S[start:stop]."""
	start = 0
	stop = len(S)
	if start >= stop: # zero elements in slice
		return False
	else: # two or more elements in slice
		mid = (start + stop) // 2
	if target == S[mid]:
		return True
	elif target > S[mid]:
		return binary_search(S[mid+1:], target)
	else:
		return binary_search(S[:mid-1], target)

def hanoi(n, source, helper, target):
    print "hanoi( ", n, source, helper, target, " called"
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source[0]:
            disk = source[0].pop()
            print "moving " + str(disk) + " from " + source[1] + " to " + target[1]
            target[0].append(disk)
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        


if __name__ == '__main__':
	#TEST 1
	#disk_usage('../')

	#TEST 2
	# x = [1,2,3,4,5,6,7,8,9]
	# start_time = time() # record the starting time
	# print binary_sum(x,0,len(x))
	# end_time = time() # record the ending time
	# elapsed = end_time - start_time
	# print "Elapsed time in binary sum (ms): %s" % (elapsed)
	# start_time = time() # record the starting time
	# print sum(x)
	# end_time = time() # record the ending time
	# elapsed = end_time - start_time
	# print "Elapsed time in sum (ms): %s" % (elapsed)

	#TEST 3
	# x = [1,2,3,4,5,6,7,8,9]
	# print binary_search(x,82)

	#TEST 4
	source = ([4,3,2,1], "source")
	target = ([], "target")
	helper = ([], "helper")
	print source, helper, target
	hanoi(len(source[0]),source,helper,target)
	print source, helper, target
