"""
This module will be composed of a series of classes/data structure objects, i.g. a linked list class.
These are basic classes that could be used for other projects when the standard python list object is
not sufficient.
Good source for more info: 
https://www.geeksforgeeks.org/data-structures/linked-list/#singlyLinkedList
"""
#classes for basic linked list
import sys
class node():
	def __init__(self, data):
		self.data = data
		#ref to next node
		self.next = None

class linkedList():
	def __init__(self):
		self.head = None
		self.size = 0
	def append(self, data):
		nextNode =  node(data)
		if self.head == None:
			#then link the node with the object
			self.head = nextNode
		else:
			newNode = self.head
			#using while loop to find last node
			while newNode.next != None:
				newNode = newNode.next
			newNode.next = nextNode
		self.size +=1
	def insert(self, data, loc):
		if loc+1 > self.size:
			self.append(data)
			self.size+=1
		elif loc == 0:
			#case where we append at beggening of list that has nodes alread
			insNode = node(data)
			currNode = self.head
			self.head = insNode
			insNode.next = currNode
			self.size+=1
		else:
			insNode = node(data)
			#starting at first node
			currNode = self.head
			i = 0
			prevNode=None
			while i<loc:
				#going through each node until we hit the location insert
				#updating current node and keep tracking of previous node
				prevNode = currNode
				currNode = currNode.next
				print(i)
				i+=1
			print(currNode.data)
			print(prevNode.data)
			#adjusting link betwene preceeding node and the inserted node
			prevNode.next=insNode
			#creating like between current node and the original node at that place
			insNode.next=currNode
			self.size+=1

	def delete(self, loc):
		if loc+1>self.size or loc<0:
			print('out of bounds')
			sys.exit(0)
		elif loc == 0:
			#case where we want to delete 0th position
			currNode = self.head
			nextNode = currNode.next
			self.head = nextNode
			currNode.next = None
		else:
			#for all other cases start at head and move until we get to the position to delete
			currNode = self.head
			prevNode = None
			i = 0
			while i<loc:
				prevNode = currNode
				currNode = currNode.next
				i+=1
			if currNode.next == None:
				#case where we are at last node, remove link between last node and node to remove
				prevNode.next = None
			else:
				#get the node in next position
				nextNode = currNode.next
				#link -1 node to +1 node 1->2->3, delete 2, 1->3
				prevNode.next = nextNode
				#remove link between the deleted node and its next node
				currNode.next = None
		self.size-=1

	def retVal(self, index):
		#returns value of node at index specified in linked list
		if index<0 or index+1> self.size:
			#case where indicies are out of bounds
			print('out of bounds')
			sys.exit(1)
		else:
			currNode = self.head
			i = 0
			while i < index:
				currNode = currNode.next
				i+=1
			return currNode.data

	def print(self):
		blank = []
		if self.size == 0:
			print( blank)
			return
		new = self.head
		blank.append(new.data)
		while new.next != None:
			new = new.next
			blank.append(new.data)
		print(blank)

#create a new linked list object:
list1 = linkedList()
arr = [0, 1, 3]
for item in arr:
	list1.append(item)
print(list1.size)
ind = list1.retVal(2)
print(ind)