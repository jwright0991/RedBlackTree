from RedBlackTree import RedBlackTree
from RedBlackLeafNode import BlackLeafNode
from RedBlackNode import RedBlackNode
from BinarySearchTree import BinarySearchTree
from TreeNode import TreeNode
from evenSumRange import treeCountOddInRange
from balancedEvenSumRange import treeCountOddInRangeBalanced
t2 = BinarySearchTree()
t = RedBlackTree()

n2 = TreeNode(17)
t2.insert(n2,t2.locateParentUpdateSize(n2))
n1 = RedBlackNode(17)
t.insert(n1,t.locateParentUpdateSize(n1))

n2 = TreeNode(54)
t2.insert(n2,t2.locateParentUpdateSize(n2))
n1 = RedBlackNode(54)
t.insert(n1,t.locateParentUpdateSize(n1))

n2 = TreeNode(12)
t2.insert(n2,t2.locateParentUpdateSize(n2))
n1 = RedBlackNode(12)
t.insert(n1,t.locateParentUpdateSize(n1))

n2 = TreeNode(60)
t2.insert(n2,t2.locateParentUpdateSize(n2))
n1 = RedBlackNode(60)
t.insert(n1,t.locateParentUpdateSize(n1))

n2 = TreeNode(18)
t2.insert(n2,t2.locateParentUpdateSize(n2))
n1 = RedBlackNode(18)
t.insert(n1,t.locateParentUpdateSize(n1))

n2 = TreeNode(15)
t2.insert(n2,t2.locateParentUpdateSize(n2))
n1 = RedBlackNode(15)
t.insert(n1,t.locateParentUpdateSize(n1))

n2 = TreeNode(1)
t2.insert(n2,t2.locateParentUpdateSize(n2))
n1 = RedBlackNode(1)
t.insert(n1,t.locateParentUpdateSize(n1))

print(t)
print(t2)
