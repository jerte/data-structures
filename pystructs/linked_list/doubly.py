''' doubly linked list implementation '''
import unittest

class Cons():
	def __init__(self, cxr, car, cdr):
		self.cxr = cxr
		self.car = car
		self.cdr = cdr
	
	def __str__(self):
		return self.car

class Doubly_Linked_List():
	def __init__(self, *args):
		if len(args):
			self.root = Cons(None, args[0], None)
			self.len = len(args)
			prev = self.root
			for i in range(1,len(args)):
				node = Cons(prev, args[i], None)
				prev.cdr = node
				prev = node
		else:
			self.root = None
			self.len = 0

	def __len__(self):
		return self.len

	def __get_node__(self, i):
		node = self.root
		if(i>=0 and i<self.len):
			for i in range(i):
				node = node.cdr
		elif(i*-1 <= self.len):
			for i in range(self.len+i):
				node = node.cdr
		else:
			print("index error")
		return node

		
	def __getitem__(self, i):
		return self.__get_node__(i).car

	def __setitem__(self, i, data):
		self.__get_node__(i).car = data

	def __str__(self):
		str = "["
		node = self.root
		if self.len >= 2:
			for i in range(self.len-1):
				str += node.car + ", "
				node = node.cdr
			str += node.car
		elif self.len==1:
			str += node.car
		return str + "]"

	def insert(self, i, data):
		if i<self.len:
			if i>=0:
				replacement = self.__get_node__(i)
				new_ = Cons(replacement.cxr, data, replacement)
				replacement.cxr.cdr = new_
				replacement.cxr = new_
				self.len += 1
			elif i>self.len*-1:
				node = self.root
				for j in range(self.len+i):
					node = node.cdr
				new_ = Cons(node, data, node.cdr)
				node.cdr = new_
				self.len += 1
			else:
				print("index error")
		elif( i==self.len ):
			self.append(data)
		elif( i==0 ):
			temp = self.root
			self.root = Cons(None, data, temp)
			temp.cxr = self.root
			self.len += 1
		else:
			print("index error")

	def append(self, data):
		if self.root:
			node = self.__get_node__(self.len-1)
			new_ = Cons(node, data, None)
			node.cdr = new_
		else:
			self.root = Cons(None, data, None)	
		self.len += 1

	def remove(self, i):
		if( i<self.len and i!=0):
			node = self.__get_node__(i)
			node.cxr.cdr = node.cdr
			if node.cdr:
				node.cdr.cxr = node.cxr	
			del node
			self.len -= 1	
		elif (i==0):
			node = self.root
			self.root = node.cdr
			del node
			self.len -= 1

		else:
			print("index error")
		

	def is_empty(self):
		return self.len==0

	def empty(self):
		node = self.root
		for i in range(1,self.len):
			node = node.cdr
			del node.cxr
		self.root = None
		self.len = 0

	def contains(self, data):
		node = self.root
		for i in range(self.len):
			if(node.car==data):
				return True
			else:
				node = node.cdr
		return False

class Test_Doubly_Linked_List(unittest.TestCase):
	def test_constructor_and_str(self):
		# empty, one item, multiple items
		L = Doubly_Linked_List()
		self.assertEqual(L.__str__(), "[]")
		L = Doubly_Linked_List('a')
		self.assertEqual(L.__str__(), "[a]")
		L = Doubly_Linked_List('a', 'b', 'c')
		self.assertEqual(L.__str__(), "[a, b, c]")
	
	def test_len(self):
		# empty, one item, multiple items
		L = Doubly_Linked_List()
		self.assertEqual(len(L), 0)
		L = Doubly_Linked_List('a')
		self.assertEqual(len(L), 1)
		L.empty()
		self.assertEqual(len(L), 0)
		L = Doubly_Linked_List('a', 'b', 'c')
		self.assertEqual(len(L), 3)
		L.remove(1)
		self.assertEqual(len(L), 2)
	
	def test_get(self):
		L = Doubly_Linked_List('a')
		self.assertEqual(L[0],'a')
		L = Doubly_Linked_List('a', 'b', 'c')
		self.assertEqual(L[1],'b')
		self.assertEqual(L[-1], 'c')
		self.assertEqual(L[-2], 'b')
	
	def test_append(self):
		L = Doubly_Linked_List()
		L.append('a')
		self.assertEqual(L.__str__(), '[a]')
		L = Doubly_Linked_List('a','b','c')
		L.append('d')
		self.assertEqual(L.__str__(), '[a, b, c, d]')
	
	def test_insert(self):
		L = Doubly_Linked_List()
		L.insert(0, 'a')
		self.assertEqual(L.__str__(), '[a]')
		L = Doubly_Linked_List('a','c')
		L.insert(1, 'b')	
		self.assertEqual(L.__str__(), '[a, b, c]')
		L.insert(-1, 'd')
		self.assertEqual(L.__str__(), '[a, b, c, d]')
	
	def test_set(self):
		L = Doubly_Linked_List('a')
		L[0] = 'b'
		self.assertEqual(L.__str__(), '[b]')
		L = Doubly_Linked_List('a', 'b', 'c')
		L[1] = 'B'
		self.assertEqual(L.__str__(), '[a, B, c]')
		L[-1] = 'C'
		self.assertEqual(L.__str__(), '[a, B, C]')
	
	def test_remove(self):
		L = Doubly_Linked_List('a')
		L.remove(0)
		self.assertEqual(L.__str__(), '[]')
		L = Doubly_Linked_List('a','b','b','c')
		L.remove(1)
		self.assertEqual(L.__str__(), '[a, b, c]')
		L.remove(-1)
		self.assertEqual(L.__str__(), '[a, b]')
	
	def test_empty(self):
		L = Doubly_Linked_List()
		L.empty()
		self.assertEqual(L.__str__(), '[]')
		L = Doubly_Linked_List('a','b','c')
		L.empty()
		self.assertEqual(L.__str__(), '[]')
	
	def test_contains(self):
		L = Doubly_Linked_List()
		self.assertEqual(L.contains('a'), False)
		L.append('a')
		self.assertEqual(L.contains('a'), True)
		L.append('b')
		self.assertEqual(L.contains('b'), True)
		self.assertEqual(L.contains('c'), False)
'''
	
	def test_iterator(self):
	'''

if __name__ == "__main__":
	unittest.main()
