#!/usr/bin/env python


class binaryTree(object):
	
	def __init__(self, value):
		self.value = value
		self.leftBranch = None
		self.rightBranch = None
		self.parent = None
	
	def __str__(self):
		return self.value
		
	def getValue(self):
		return self.value
		
	def setParent(self, parent):
		self.parent = parent
		
	def getParent(self):
		return self.parent
		
	def setLeftBranch(self, node):
		self.leftBranch = node
	
	def getLeftBranch(self):
		return self.leftBranch
	
	def setRightBranch(self, node):
		self.rightBranch = node
	
	def getRightBranch(self):
		return self.rightBranch



def DFSBinary(root, num):
	stack = [root]
	while len(stack) > 0:
		print 'at node', str(stack[0].getValue())
		if num == stack[0].value:
			return TracePath(stack[0])
		else:
			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
	return False
	
	
def WFSBinary(root, num):
	queue = [root]
	while len(queue) > 0:
		print 'at node', str(stack[0], getValue())
		if num == queue[0].value:
			return TracePath(queue[0])
		else:
			temp = queue.pop(0)
			if temp.getLeftBranch():
				queue.append(temp.getLeftBranch())
			if temp.getRightBranch():
				queue.append(temp.getRightBranch())
	return False


def TracePath(node):
	if node.getParent():
		return [node] + TracePath(node.getParent())
	else:
		return [node]	
	
def DFBinatyOrderd(root, num):
	stack = [root]
	while len(stack) > 0
		print 'at node', str(stack[0].getValue)
		if num == stack[0].value:
			return True
		elif num < stack[0].value:
			temp = stack.pop(0)
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
		else:
			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
	return False





## Decision Trees

def buildDecisionTree(sofar, todo):
	if len(todo) == 0:
		return binaryTree(sofar)
	else:
		withelt = buildDecisionTree(sofar + todo[0], todo[1:])
		withoutelt = buildDecisionTree(sofar, todo[1:])
		here = binaryTree(sofar)
		here.setLeftBranch(withelt)
		here.setRightBranch(withoutelt)
		return here



		
		

def test():
	n1 = binaryTree(1)
	n2 = binaryTree(2)
	n3 = binaryTree(3)
	n4 = binaryTree(4)
	n5 = binaryTree(5)
	n6 = binaryTree(6)
	n7 = binaryTree(7)
	n8 = binaryTree(8)
	
	n5.setLeftBranch(n2)
	n2.setParent(n5)
	n5.setRightBranch(n8)
	n8.setParent(n5)
	n2.setLeftBranch(n1)
	n1.setParent(n2)
	n2.setRightBranch(n4)
	n4.setParent(n2)
	n8.setLeftBranch(n6)
	n6.setParent(n8)
	n6.setLeftBranch(n7)
	n7.setParent(n6)
	
	
	DOutput = DFSBinary(n5, 1)
	WOutput = WFSBinary(n5, 7)
	print [e.getValue() for e in DOutput]
	print [e.getValue() for e in WOutput]
	

if __name__ == '__main__':
	test()