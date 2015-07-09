import sys

if __name__ == '__main__':
	if len(sys.argv) == 2:
		r = int(sys.argv[1])
		c = int(sys.argv[1])
	elif len(sys.argv) == 3:
		r = int(sys.argv[2])
		c = int(sys.argv[1])
	else:
		c=4
		r=4	
	data = [ [0] * c for j in range(r) ]
	for _list in data:
		print _list

