import sys
from RedBlackNode import RedBlackNode
from RedBlackLeafNode import BlackLeafNode
from RedBlackTree import RedBlackTree
#@author Josh Wright
#starting at the given node of a tree, finds the first node in the range 
#@param rootNode
#   the root NODE of the tree to search in
#@param start
#   the smallest value in the range
#@param end
#   the largest value in the range
def firstRootInRange(rootNode,start,end):
        node = rootNode
        if node == None or node.isLeaf:
            return None
        else:
            if node.data <= end and node.data >= start:
                return node
            elif node.data < start:
                return firstRootInRange(rootNode.rightChild, start, end)
            elif node.data > end:
                return firstRootInRange(rootNode.leftChild,start,end)
#counts the number of odd children in the left subtree of a tree starting at root(node)
#as long as the value of the node is greater than or equal to start.
#when a node has a right child that is not empty and has an odd sum, the entire subtree is
#considered to be "one" odd value. This keeps the algorith performing in theta(h)
#@requires root must be a TreeNode (not a BinarySearchTree)
#@param root
#   the node that marks the root of the subtree to search in
#@param start
#   the smallest value that a node can contain for it to be counted
def treeCountOddGE(root, start):
    countOdd = 0
    node = root.leftChild
    while(node != None and not node.isLeaf):
        if (node.data >= start):
            if not(node.isEven):
                countOdd +=1
            if(node.rightChild != None and not node.rightChild.isLeaf and not(node.rightChild.isEvenSum)):
                countOdd +=1
            node = node.leftChild
        else:
            node = node.rightChild
    return countOdd
#counts the number of odd children in the right subtree of a tree starting at root(node)
#as long as the value of the node is less than or equal to end.
#when a node has a left child that is not empty and has an odd sum, the entire subtree is
#considered to be "one" odd value. This keeps the algorith performing in theta(h)
#@requires root must be a TreeNode (not a BinarySearchTree)
#@param root
#   the node that marks the root of the subtree to search in
#@param end
#   the largest value that a node can contain for it to be counted
def treeCountOddLE(root, end):
    countOdd = 0
    node = root.rightChild
    while(node != None and not node.isLeaf):
        if (node.data <= end):
            if not (node.isEven):
               countOdd +=1
            if(node.leftChild != None and not node.leftChild.isLeaf and not(node.leftChild.isEvenSum)):
                countOdd += 1
            node = node.rightChild
        else:
            node = node.leftChild
    return countOdd
#counts the number of odd children in the left and right subtree of the given tree
#within the range of [start,end] and whether the root of the tree is odd
#@requires tree must be a BinarySearchTree
#@param tree
#   the BinarySearchTree that is being searched in
#@param start
#   the smallest value that a node can contain for it to be counted
#@param end
#   the largest value that a node can contain for it to be counted
def treeCountOddInRangeBalanced(tree, start, end):
        if tree.root == None:
            return 0
        node = firstRootInRange(tree.root,start,end)
        countOdd = 0
        if node != None and not node.isLeaf:
            if not(node.isEven):
                countOdd +=1
            countOdd += treeCountOddGE(node,start)
            countOdd += treeCountOddLE(node,end)
        return countOdd

#main function
if len(sys.argv) == 3:
    #initialize an empty binary tree
    tree = RedBlackTree()
    #variable used to store the end result
    result = ""
    #open the file containing the values to be adde to the BinarySearchTree
    dataFile = open(sys.argv[1], 'r')
    #add all of the values from the file to the tree
    for line in dataFile:
        node = RedBlackNode(int(line))
        tree.insert(node,tree.locateParentUpdateSize(node))
    #open the file containing the ranges to check
    dataRanges = open(sys.argv[2],'r')
    #iterate through each line of the file
    for line in dataRanges:
        #get the starting and ending values of the range
        i = 0
        start = ""
        end = ""
        while(line[i] != ' '):
            start += line[i]
            i+=1       
        start = int(start)
        while(line[i] != '\n'):
            i+=1
            end += line[i]
        end = int(end)
        #if there is an even number of odd values in the sum, then the sum is even, otherwise it's odd
        if treeCountOddInRangeBalanced(tree,start,end) % 2 == 0:
            result = "even sum"
        else:
            result = "odd sum"
        #print the results
        print("Range ["+ str(start)+","+str(end)+"]"+": "+result)
    dataFile.close()
    dataRanges.close()
#the rest of the program will be skipped and this print statement will execute
#if the user inputs an incorrect number of command line arguments
else:
    print("invalid number of command line arguments")
