#!/usr/bin/env python
# -- coding: utf-8 --


class Node(object):
	
	
	def __init__(self, item):
		self.item = item
		self.next = None
		
		
	def get_item(self):
		return self.item
	
		
	def get_next(self):
		return self.next
	
		
	def set_item(self, new_item):
		self.item = new_item
	
		
	def set_next(self, new_next):
		self.next = new_next
		
	
	
class Linear_list(object):
	
	
	def __init__(self):
		self.head = Node(0)
		self.length = 0
		
		
	def destroy_list(self):
		self.head == None
		self.length == None
		
		
	def clear_list(self):
		self.head.set_next(None)
		self.length = 0
		
		
	def list_empty(self):
		return self.head.get_next() == None
		
		
	def list_length(self):
		return self.length
		
		
	def get_elem(self, i):
		j = 1
		cur_node = self.head
		while cur_node.get_next():
			cur_node = cur_node.get_next()
			if i == j:
				return cur_node.get_item()
			j += 1
		return None
		
		
	def locate_elem(self, e):
		j = 1
		cur_node = self.head.get_next()
		while cur_node:
			if cur_node == e:
				return j
			j += 1
		return None
			
		
		
	def prior_elem(self, e):
		pre_node = self.head
		cur_node = pre_node.get_next()
		if e == cur_node:
			return None
		while cur_node:
			if cur_node == e:
				return pre_node.get_item()
			pre_node = cur_node
			cur_node = pre_node.get_next()
		return None 
		
		
	def next_elem(self, e):
		return e.get_next().get_item()
		
		
		
	def list_insert(self, i, e):
		new_node = Node(e)
		
		if self.list_empty():
			self.head.set_next(new_node)
			self.length = 1
			
		else:
			j = 1
			pre_node = self.head
			while pre_node.get_next():
				cur_node = pre_node.get_next()
				if i == j:
					break
				pre_node = cur_node
				j += 1
			new_node.set_next(cur_node)
			pre_node.set_next(new_node)
			self.length += 1
		
		
	def list_delet(self, i):
		j = 1
		pre_node = self.head
		while pre_node.get_next():
			cur_node = pre_node.get_next()
			if j == i:
				pre_node.set_next(cur_node.get_next())
				self.length -= 1
				return cur_node.get_item()
			j += 1
			pre_node = cur_node
		return None
				
		
	
	def list_traverse(self, func):
		cur_node = self.head.get_next()
		while cur_node:
			try:
				cur_node.set_item(func(cur_node.get_item()))
			except:
				print "Some item failed to apply this function"
			cur_node = cur_node.get_next()
			
				