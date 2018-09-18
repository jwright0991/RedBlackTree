#@author Josh Wright
#Red Black Node Object Representation
#Each node has a parent node, except the root of a tree who's parent is null.
#Each node may have 0-2 children(left and right)
#All Red Black Nodes must have BlackLeafNode Children if the child is a leaf
from RedBlackLeafNode import BlackLeafNode
#Data is an integer value
#isEvenSum is a boolean value asserting whether the sum of all the node's
#children's data and the node's data results in an even integer.
#isLeaf is always set to false to distinquish from BlackLeafNodes
class RedBlackNode:
    #default constructor
    #paramater data is the integer value that represents the node
    #isRed: defines color
    def __init__(self,data):
        self.parent = None
        self.data = data
        self.leftChild = BlackLeafNode()
        self.rightChild = BlackLeafNode()
        self.isEvenSum = (data % 2 == 0)
        self.size = 1;
        self.isEven = (data % 2 == 0)
        self.isRed = True
        self.isLeftChild = None
        self.isLeaf = False
    #Returns the string representation of the node and it's children (recursive)
    def __str__(self):
        stringRep = "EMPTY"
        color = "-Black"
        if self.isRed:
            color = "-Red"
        if self.data == None:
            return "NONE"
        elif self.leftChild != None and self.rightChild != None:
            stringRep = str(self.data) + color + "(" + str(self.leftChild) + ", " + str(self.rightChild) + ")"
            return stringRep
        elif self.leftChild == None and self.rightChild != None:
            stringRep = str(self.data) + color + "(EMPTY, " + str(self.rightChild) + ")"
            return stringRep
        elif self.leftChild != None and self.rightChild == None:
            stringRep = str(self.data) + color + "(" + str(self.leftChild) + ",EMPTY)"
            return stringRep
        elif self.leftChild == None and self.rightChild == None:
            stringRep = str(self.data) + color + "(EMPTY, EMPTY)"
            return stringRep
