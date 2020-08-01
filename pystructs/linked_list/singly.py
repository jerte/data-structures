''' single linked list implementation '''
import unittest

class Cons():
	def __init__(self, car, cdr):
		self.car = car
		self.cdr = cdr
	
class Singly_Linked_List():
	def __init__(self, *args):	
		if len(args)==0:
			self.root = None
			self.len = 0
		elif len(args)==1:
			self.root = Cons(args[0],None)
			self.len = 1
		else:
			nodes = []
			prev_node = None
			for i in range(1, len(args)-1):
				node = Cons(args[len(args)-1-i], prev_node)
				prev_node = node
			self.root = Cons(args[0], prev_node)
			self.len = len(args)
	
	def __len__(self):
		return self.len

	def __getitem__(self, i):
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

	def __setitem__(self, i, data):
		self.__getitem__(i).car = data

	def insert(self, i, data):
		if i < self.len:
			if i >=0:
				node = self.root
				for j in range(0, i):
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
		node = self.root
		for i in range(0, self.len):
			node = node.cdr
		node.cdr = Cons(data, None)
		self.len += 1

	def __str__(self):
		str_ = "["
		node = self.root
		if node:
			str_ += str(node.car)
		for i in range(0, self.len):
			str_ += ", " + str(node.car)
			node = node.cdr
		if node:
			str_ += str(node.car)
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
				prev_node.cdr = node.cdr
				del node
			elif i*-1 < self.len:
				node = self.root
				prev_node = None
				for j in range(0, self.len+i):
					prev_node = node
					node = node.cdr
				prev_node.cdr = node.cdr
				del node
			else:
				print("error")
		else:
			print("error")
	
	def remove_all(self):
		node = self.root
		for i in range(0, self.len):
			temp = node.cdr
			del node
			node = temp
		
	def contains(self, data):
		node = self.root
		for i in range(0, self.len):
			if node.car == data:
				return True
			node = node.cdr
		return False
