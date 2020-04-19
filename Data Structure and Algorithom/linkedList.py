class Node:
	def __init__(self,data=None, next=None):
		self.data = data
		self.next = next

	def __repr__(self):
		return repr(self.data)


class LinkedList:
	def __init__(self):
		self.head = Node()

	def __repr__(self):
		nodes = []
		