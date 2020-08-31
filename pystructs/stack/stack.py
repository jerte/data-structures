import unittest

class StackEmpty(BaseException):
	pass

class Stack():
	def __init__(self, *args):
		if len(args):
			self.stack = []
			for i in args:
				self.push(i)
		else:
			self.stack = []

	def push(self, x):
		self.stack.insert(0, x)

	def pop(self):
		if self.stack:
			return self.stack.pop(0)
		else:
			raise StackEmpty()

	def peek(self):
		if self.stack:
			return self.stack[0]
		else:
			raise StackEmpty()

	def isEmpty(self ):
		return not self.stack

class Test_Stack(unittest.TestCase):
	def test_constructor(self):
		S = Stack()
		S = Stack(1)
		S = Stack(1,2,3)

	def test_push(self):
		S = Stack()
		S.push(1)
		self.assertEqual(S.peek(), 1)
		S.push(2)
		self.assertEqual(S.peek(), 2)

	def test_pop(self):
		S = Stack()
		try:
			S.pop()
		except StackEmpty:
			self.assertEqual(True, True)
		S.push(1)
		self.assertEqual(S.pop(), 1)
		S.push(2)
		S.push(3)
		self.assertEqual(S.pop(), 3)
		self.assertEqual(S.pop(), 2)
		try:
			S.pop()
		except StackEmpty as e:
			self.assertEqual(True, True)

	def test_peek(self):
		S = Stack()
		try:
			S.peek()
		except StackEmpty:
			self.assertEqual(True, True)
		S.push(1)
		self.assertEqual(S.peek(), 1)
		S.push(2)
		self.assertEqual(S.peek(), 2)
		S.pop()
		self.assertEqual(S.peek(), 1)
		S.pop()
		try:
			S.peek()
		except StackEmpty as e:
			self.assertEqual(True, True)

	def test_isEmpty(self):
		S = Stack()
		self.assertEqual(S.isEmpty(), True)
		S.push(1)
		self.assertEqual(S.isEmpty(), False)
		S.pop()
		self.assertEqual(S.isEmpty(), True)

if __name__ == '__main__':
	unittest.main()	
