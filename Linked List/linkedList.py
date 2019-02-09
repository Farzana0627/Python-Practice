class Node:
	def __init__(self, dataval=None):
		self.dataval= dataval
		self.nextval = None

class SLinkedList:
	def __init__(self):
		self.headval= None

	def listPrint(self):
		printval= self.headval
		while(printval):
			print(printval.dataval)
			printval= printval.nextval

	def atBeginning(self, newNode):
		if(self.headval is None):
			self.headval= newNode
			return
		
		newNode.nextval=self.headval
		self.headval= newNode

	def atEnd(self, newNode):
		if(self.headval is None):
			self.headval= newNode
			return
		
		temp= self.headval
		while(temp.nextval):
			temp=temp.nextval
		temp.nextval= newNode

	def inBetween(self, prevNode, newNode):
		if prevNode is None:
			print("The previous node doesn't exist!")
			return
		newNode.nextval= prevNode.nextval
		prevNode.nextval= newNode

	def reverse(self):
		
		current= self.headval
		if(current is None):
			return
		prev = None
		tempNext= Node()
		while(current is not None):
			tempNext= current.nextval
			current.nextval= prev
			prev=current
			current= tempNext
		self.headval=prev


		
	def remove(self, node):
		current= self.headval
		prev= None
		while(current is not None):
			if current.dataval==node.dataval:
				if(prev is not None):
					prev.nextval= current.nextval
				else:
					self.headval=current.nextval
				current=None
				break
			else:
				prev=current
				current=current.nextval

def getMiddle(head):
	tempA= head
	tempB= head
	while( tempB is not None and tempB.nextval is not None):
		tempB= tempB.nextval.nextval
		tempA= tempA.nextval

	print ("Middle value of the linked list: ", tempA.dataval, "\n")
#creation and traversal

list1= SLinkedList()
list1.headval= Node(1)
e2= Node(2)
e3= Node(3)
e4= Node(4)
e5= Node(5)
list1.headval.nextval= e2
e4.nextval= e5
e3.nextval=e4
e2.nextval= e3

#list1.listPrint()


#Insertion in a Linked List

startNode= Node(0)
list1.atBeginning(startNode)


endNode= Node(5)
list1.atEnd(endNode)

midNode= Node("mid")
list1.inBetween(list1.headval.nextval.nextval,midNode)

print("List1:\n")
list1.listPrint()


print("Middle of List1:\n")
getMiddle(list1.headval)
#Reversing a one way linked list

print("Reverse:\n")
list1.reverse()
list1.listPrint()


#Removing a one way linked list

print("Removed:\n")
list1.remove(Node(5))
list1.listPrint()








