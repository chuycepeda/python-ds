import sys

def ch1_ex1_1():
	"""
	Write a short Python function, is multiple(n, m), that takes two integer
	values and returns True if n is a multiple of m, that is, n = mi for some
	integer i, and False otherwise.

	"""
	print "This is call for excercise R1.1 in CH1."
	reply = input('Please input x and y (space separated) to see if x is multiple of y: ')
	_reply = reply.split()
	x = int(_reply[0])
	y = int(_reply[1])
	try:
		if y % x == 0:
				print "Yes, %s by %s equals %s" % (x, y/x, y)
		else:
			try:
				i = 0
				if x>0:
					while (i+1)*x < y:
						i+=1
					print "No, best result is %s by %s with a remainder of %s to equal %s" % (x, i, y%x, y)
				else:
					print "Please input a number bigger than 0"
					ch1_ex1_1()
			except ZeroDivisionError:
				print 'I know what you did here...ZeroDivisionError detected'
	except ZeroDivisionError:
			print 'I know what you did here...ZeroDivisionError detected'

def ch1_ex1_4():
	"""
		4 Write a short Python function that takes a positive integer n and returns
		the sum of the squares of all the positive integers smaller than n

	"""
	print "This is call for excercise R1.4 in CH1."
	x = input('Please input x to see the squares of integers less than x: ')
	try:
		_sqrs= [k*k for k in range(1,x+1)]
		print "Squares are: %s" % (_sqrs)
		_sum = input("Want me to sum? (y/n): ")
		if _sum == 'y':
			print "Sum is: %s" % (sum(_sqrs))
		else:
			print "OK, eom."
	except:
		print "Please input a correct integer number..."
		ch1_ex1_4()

def ch1_ex1_14():
	"""
		Write a short Python function that takes a sequence of integer values and
		determines if there is a distinct pair of numbers in the sequence whose
		product is odd.

	"""
	print "This is call for excercise C1.14 in CH1."
	reply = input('Please input an array of numbers as a string separated by spaces: ')
	_reply = reply.split()
	print 'Input: %s' % (_reply)
	_rep_set = set(_reply)
	print 'Set: %s' % (_rep_set)
	_rep_list = list(_rep_set)
	print 'List: %s' % (_rep_list)
	odd = False
	for x in range(0, len(_rep_list)):
		for y in range(x+1, len(_rep_list)):
			try:
				if int(_rep_list[x])*int(_rep_list[y]) % 2 == 0:
					print "Yes, %s by %s equals %s, so they are odd" % (_rep_list[x],_rep_list[y],int(_rep_list[x])*int(_rep_list[y]))
					odd = True
			except Exception, e:
				print "Not enough distinct elements in array: %s" % (e)
		if odd:
			break
	if not odd:
		print "No, there are NO odd products"

	#for x in _reply:


def main(argv):
	if argv:
		if argv[0] == '':
			method = input("Choose the method you want me to run for you: ")
			main([method])
		elif argv[0] == 'ch1.ex1.1':
			ch1_ex1_1()
		elif argv[0] == 'ch1.ex1.4':
			ch1_ex1_4()
		elif argv[0] == 'ch1.ex1.14':
			ch1_ex1_14()
	else:
		method = input("Choose the method you want me to run for you: ")
		main([method])



if __name__ == '__main__':
	main(sys.argv[1:])