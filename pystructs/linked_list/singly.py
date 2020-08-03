''' single linked list implementation '''
import unittest

class Cons():
	def __init__(self, car, cdr):
		self.car = car
		self.cdr = cdr
	
	def __str__(self):
		return self.car
	
class Singly_Linked_List():
	def __init__(self, *args):	
		if len(args)==0:
			self.root = None
			self.len = 0
		elif len(args)==1:
			self.root = Cons(args[0],None)
			self.len = 1
		else:
			prev_node = None
			for i in range(1, len(args)):
				node = Cons(args[len(args)-i], prev_node)
				prev_node = node
			self.root = Cons(args[0], prev_node) 
			self.len = len(args)
	
	def __len__(self):
		return self.len
	
	def	__getnode__(self, i):
		if i < self.len:
			if i >= 0:
				node = self.root
				for j in range(0, i):
					node = node.cdr
				return node
			elif i*-1 < self.len:
				node = self.root
				for j in range(0,self.len+i):
					node = node.cdr
				return node
			else:
				print("error")
		else:
			print("error")
	
	def __getitem__(self, i):
		return self.__getnode__(i).car
	
	def __setitem__(self, i, data):
		self.__getnode__(i).car = data

	def insert(self, i, data):
		if i < self.len:
			if i >=0:
				node = self.root
				for j in range(1, i):
					node = node.cdr
				temp = node.cdr
				node.cdr = Cons(data, temp)
				self.len += 1			
			elif i*-1 < self.len:
				node = self.root
				for j in range(0, self.len+i):
					node = node.cdr
				temp = node.cdr
				node.cdr = Cons(data, temp)
				self.len += 1
			else:
				print("error")

		elif i==self.len:
			self.append(data)
		else:
			print("error")

	def append(self, data):
		if self.root!=None:
			node = self.root
			for i in range(1, self.len):
				node = node.cdr
			node.cdr = Cons(data, None)
			self.len += 1
		else:
			self.root = Cons(data, None)
			self.len += 1
	def __str__(self):
		str_ = "["
		node = self.root
		if node!=None:
			str_ += node.car
			node = node.cdr
		for i in range(1, self.len):
			str_ += ", " + node.car
			node = node.cdr
		if node!=None:
			str_ += node.car
		str_ += "]"
		return str_
	
	def remove(self, i):
		node = self.root
		if i < self.len:
			if i>=0:
				node = self.root
				prev_node = None
				for j in range(0, i):
					prev_node = node
					node = node.cdr
				if prev_node:
					prev_node.cdr = node.cdr
					del node
					self.len -= 1
				else:
					del self.root
					self.root = None
					self.len -= 1
			elif i*-1 < self.len:
				node = self.root
				prev_node = None
				for j in range(0, self.len+i):
					prev_node = node
					node = node.cdr
				prev_node.cdr = node.cdr
				del node
				self.len -= 1
			else:
				print("error")
		else:
			print("error")
	
	def empty(self):
		node = self.root
		del self.root
		self.root = None
		self.len = 0
		for i in range(0, self.len):
			temp = node.cdr
			del node
			node = temp
		
	def contains(self, data):
		node = self.root
		if self.root and self.root.car==data:
			return True
		for i in range(0, self.len):
			if node.car == data:
				return True
			node = node.cdr
		return False

''' tests '''
class Test_Singly_Linked_List(unittest.TestCase):
	def test_constructor_and_str(self):
		# empty, one item, multiple items
		L = Singly_Linked_List()
		self.assertEqual(L.__str__(), "[]")
		L = Singly_Linked_List('a')
		self.assertEqual(L.__str__(), "[a]")
		L = Singly_Linked_List('a', 'b', 'c')
		self.assertEqual(L.__str__(), "[a, b, c]")

	def test_len(self):
		# empty, one item, multiple items
		L = Singly_Linked_List()
		self.assertEqual(len(L), 0)
		L = Singly_Linked_List('a')
		self.assertEqual(len(L), 1)
		L = Singly_Linked_List('a', 'b', 'c')
		self.assertEqual(len(L), 3)
	
	def test_get(self):
		L = Singly_Linked_List('a')
		self.assertEqual(L[0],'a')
		L = Singly_Linked_List('a', 'b', 'c')
		self.assertEqual(L[1],'b')
		self.assertEqual(L[-1], 'c')
		self.assertEqual(L[-2], 'b')
	
	def test_append(self):
		L = Singly_Linked_List()
		L.append('a')
		self.assertEqual(L.__str__(), '[a]')
		L = Singly_Linked_List('a','b','c')
		L.append('d')
		self.assertEqual(L.__str__(), '[a, b, c, d]')
	 
	def test_insert(self):
		L = Singly_Linked_List()
		L.insert(0, 'a')
		self.assertEqual(L.__str__(), '[a]')
		L = Singly_Linked_List('a','c')
		L.insert(1, 'b')
		self.assertEqual(L.__str__(), '[a, b, c]')
		L.insert(-1, 'd')
		self.assertEqual(L.__str__(), '[a, b, c, d]')
		
	def test_set(self):
		L = Singly_Linked_List('a')
		L[0] = 'b'
		self.assertEqual(L.__str__(), '[b]')
		L = Singly_Linked_List('a', 'b', 'c')
		L[1] = 'B'
		self.assertEqual(L.__str__(), '[a, B, c]')
		L[-1] = 'C'
		self.assertEqual(L.__str__(), '[a, B, C]')
	
	def test_remove(self):
		L = Singly_Linked_List('a')
		L.remove(0)
		self.assertEqual(L.__str__(), '[]')
		L = Singly_Linked_List('a','b','b','c')
		L.remove(1)
		self.assertEqual(L.__str__(), '[a, b, c]')
		L.remove(-1)
		self.assertEqual(L.__str__(), '[a, b]')
	
	def test_empty(self):
		L = Singly_Linked_List()
		L.empty()
		self.assertEqual(L.__str__(), '[]')
		L = Singly_Linked_List('a','b','c')
		L.empty()
		self.assertEqual(L.__str__(), '[]')

	def test_contains(self):
		L = Singly_Linked_List()
		self.assertEqual(L.contains('a'), False)
		L.append('a')
		self.assertEqual(L.contains('a'), True)
		L.append('b')
		self.assertEqual(L.contains('b'), True)
		self.assertEqual(L.contains('c'), False)

	'''
	def test_iterator(self):
	'''
if __name__=="__main__":	
	unittest.main()
