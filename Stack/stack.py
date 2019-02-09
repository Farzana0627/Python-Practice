class Stack:
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items ==[]

	def push(self, newVal):
		self.items.append(newVal)

	def pop(self):
		self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

	def stackPrint(self):
		for x in self.items:
			print(x)


stk= Stack()
for x in range (0,6):
	stk.push(x)
stk.stackPrint()

print("Peek:")
print(stk.peek())

print("Pop:")
stk.pop()
stk.stackPrint()
