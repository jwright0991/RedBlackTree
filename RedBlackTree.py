from RedBlackNode import RedBlackNode
from RedBlackLeafNode import BlackLeafNode
from RedBlackTreeSecondary import insertFixup, transplant, rightRotate ,leftRotate
#@author Josh Wright
#Red-Black Tree Object Representation: Tree of RedBlackNodes, each node has between 0-2
#child nodes. Left child is strictly less than and right child is greater than or equal to parent node.
#each node has a color and the tree must satisfy the 5 properties of a red-black tree
class RedBlackTree:
    #default constructor, an empty tree is just None
    def __init__(self):
        self.root = None       
    #locates and returns the parent node of child in the RB tree(self)
    #also updates the size of each tree and whether the sum is even along the path from the root to the parent
    #@updates self
    def locateParentUpdateSize(self,child):
        result = None
        node = self.root
        while node != None and not node.isLeaf:
            node.size +=1
            if(not node.isEvenSum and not child.isEven) or (node.isEvenSum and child.isEven):
                node.isEvenSum = True
            else:
                node.isEvenSum = False               
            result = node
            if child.data < node.data:
                node = node.leftChild
            else:
                node = node.rightChild
        return result
    #adds node to the RB tree(self) as a child of parent
    #@requires parent must be found by calling locateParentUpdateSize(node)
    def insert(self,node, parent):
        if self.root == None:
            self.root = node
            node.isRed = False
        else:
            node.parent = parent
            if(node.data < parent.data):
                parent.leftChild = node
                node.isLeftChild = True
            else:
                parent.rightChild = node
                node.isLeftChild = False
        root = self.root
        insertFixup(self,node)
   
    #returns the string representation of the root
    # format returns node.data(leftChild,rightChild)
    # if the tree is empty
    #see the RedBlackNode __str__ method
    
    def __str__(self):
        if self.root == None:
            return "EMPTY"
        return str(self.root)
    
    
    
        

                    
                
            
        
            
        
