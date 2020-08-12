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
			for i in range(self.len+1+i):
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
		for i in range(self.len):
			str += node.cdr + ", "
			node = node.cdr
		return str+="]"

	def insert(self, i, data):
		if(i<self.len and i>self.len*-1-1):
			replacement = self.__get_node(i)
			new_ = Cons(replacement.cxr, data, replacement)
			replacement.cxr = new_
			self.len += 1
		elif( i==self.len ):
			self.append(data)
			self.len += 1
		else:
			print("index error")

	def append(self, data):
		node = self.__get_node__(self.len-1)
		new_ = Cons(node, data, None)
		node.cdr = new_
		self.len += 1

	def remove(self, i):
		if( i<self.len and i!=0):
			node = self.__get_node__(i)
			node.cxr.cdr = node.cdr
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

if __name__ == "__main__":
	#unittest.main()
