class DoublyNode:
	def __init__(self, elem=None, nxt=None, prev=None):
		self.elem = elem
		self.next = nxt
		self.prev = prev


class Queue:
	#DHDCL Implementation
	def __init__(self):
		self.start = DoublyNode()
		self.start.next = self.start.prev = self.start
	def enqueue(self, item):
		lastNode = self.start.prev
		lastNode.next = DoublyNode(item, self.start, lastNode)
		self.start.prev = lastNode.next
	def dequeue(self):
		firstNode = self.start.next
		self.start.next = firstNode.next
		firstNode.next.prev = self.start
		return firstNode.elem
	def peek(self):
		return self.start.next.elem
	def isEmpty(self):
		if self.start.next == self.start:
			return True
		return False
