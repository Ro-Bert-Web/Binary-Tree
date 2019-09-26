from random import *

class binTree:
	def __init__(self, x = None, treeType = None):
		self.treeType = treeType # Set tree's type to treeType
		if(x != None and type(x) != list):
			if(treeType != None and type(x) != treeType): # If type of x differs from treeType, raise error
				raise ValueError
			self.treeType = type(x) # Set tree's type to type of x
		self.x = x
		self.lower = None
		self.middle = None
		self.upper = None
		if(type(x) == list): # If x is a list, populate this binary tree with that list
			self.x = None
			for i in x:
				self.add(i)

	def __eq__(self, other):
		return (type(other) == binTree
			and self.unpack() == other.unpack())

	def __repr__(self):
		if(self.lower == None):
			if(self.upper == None):
				if(self.middle == None):
					return "{}".format(self.x)
				else:
					return "{}, {}".format(self.x, repr(self.middle))
			else:
				if(self.middle == None):
					return "{}, {}".format(self.x, repr(self.upper))
				else:
					return "{}, {}, {}".format(self.x, repr(self.middle), repr(self.upper))
		else:
			if(self.upper == None):
				if(self.middle == None):
					return "{}, {}".format(repr(self.lower), self.x)
				else:
					return "{}, {}, {}".format(repr(self.lower), self.x, repr(self.middle))
			else:
				if(self.middle == None):
					return "{}, {}, {}".format(repr(self.lower), self.x, repr(self.upper))
				else:
					return "{}, {}, {}, {}".format(repr(self.lower), self.x, repr(self.middle), repr(self.upper))

	def add(self, x):
		if(type(x) == list): # If x is a list, itterate through x and fill this binary tree with each element
			for i in x:
				self.add(i)
			return

		if(self.treeType != None and type(x) != self.treeType): # Raise error if the type of x does not meet the type of this tree
			raise ValueError

		if(self.x == None): # If tree's x does not exist, set it to x
			self.treeType = type(x)
			self.x = x
		elif(x > self.x): # If x is greater than tree's x, push to upper
			if(self.upper == None):
				self.upper = binTree(x, self.treeType)
			else:
				self.upper.add(x)
		elif(x < self.x): # If x is less than tree's x, push to lower
			if(self.lower == None):
				self.lower = binTree(x, self.treeType)
			else:
				self.lower.add(x)
		else: # If x is equal to tree's x, push to middle
			if(self.middle == None):
				self.middle = binTree(x, self.treeType)
			else:
				self.middle.add(x)

	def unpack(self): # All of this is copied from __repr__ just with listing out and returning arrays
		if(self.lower == None):
			if(self.upper == None):
				if(self.middle == None):
					return [self.x]
				else:
					return [self.x, *self.middle.unpack()]
			else:
				if(self.middle == None):
					return [self.x, *self.upper.unpack()]
				else:
					return [self.x, *self.middle.unpack(), *self.upper.unpack()]
		else:
			if(self.upper == None):
				if(self.middle == None):
					return [*self.lower.unpack(), self.x]
				else:
					return [*self.lower.unpack(), self.x, *self.middle.unpack()]
			else:
				if(self.middle == None):
					return [*self.lower.unpack(), self.x, *self.upper.unpack()]
				else:
					return [*self.lower.unpack(), self.x, *self.middle.unpack(), *self.upper.unpack()]

	def contains(self, x):
		if(x > self.x and self.upper != None): # If x is greater than tree's x and upper exists, check upper
			return self.upper.contains(x)
		elif(x < self.x and self.lower != None): # If x is less than tree's x and lower exists, check lower
			return self.lower.contains(x)
		else:
			return x == self.x # Otherwise, return whether x equals tree's x (this will trigger if it is equal to (True), or it is at the end of a branch (False))


if __name__ == '__main__':
	tree = binTree()
	while(True):
		x = input("Enter a value or (\"print\", \"unpack\", \"contains _\", \"exit\"): ")
		if(x == "print"):
			print(tree)
		elif(x == "unpack"):
			print(tree.unpack())
		elif(x.find("contains ") == 0):
			print(tree.contains(x[9:]))
		elif(x == "exit"):
			break
		else:
			tree.add(x)
