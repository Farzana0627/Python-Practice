class Queue:
	def __init__(self):
		self.Queue= list()

	def add(self, newVal):
		if newVal not in self.Queue:
			self.Queue.insert(0,newVal)

	def printQueue(self):
		for x in self.Queue:
			print(x)

	def remove(self):
		if(len(self.Queue)>0):
			self.Queue.pop()
	

que= Queue()
for x in range(0,6):
	que.add(x)
que.printQueue()

print("After one pop:")
que.remove()
que.printQueue()