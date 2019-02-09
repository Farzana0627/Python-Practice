class Node:
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.left= None
		self.right= None

	def insert(self, data):
		if(self.data):
			if(self.data > data):
				if(self.left):
					self.left.insert(data)
				else:
					self.left=Node(data)
			else:
				if(self.right):
					self.right.insert(data)
				else:
					self.right= Node(data)

		else:
			self.data= data

	def printTree(self):
		if(self.left):
			self.left.printTree()
		print(self.data)
		if(self.right):
			self.right.printTree()


tree = Node(10)
tree.insert(6)
tree.insert(14)
tree.insert(3)
tree.insert(0)
tree.insert(6)
tree.insert(31)
tree.insert(19)
tree.printTree()


		