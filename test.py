class MyClass(object):
	def __init__(self,start=0):
		self._start = start

	def __str__(self):
		return '"' + self + '"'

	def __iter__(self):
		return self

	def _internalMethod(self):
		self._start += 1

	def externalMethod(self, n=2):
		a = self._start * n
		self._internalMethod()
		return a

class MyInClass(MyClass):
	def __init__(self, x = 0, start = 0):
		super(MyInClass, self).__init__(start)
		self._x = x

	def _internalMethod(self):
		self._start += 10

if __name__ == '__main__':
	mc = MyClass(10)
	print mc.externalMethod(4)
	print mc.externalMethod(4)
	mci = MyInClass(10,10)
	print mci.externalMethod(4)
	print mci.externalMethod(4)