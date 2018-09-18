#Black Null Nodes for bottom level of each path of a Red-Black Tree
#data is set to 0 so it will not be counted as odd
class BlackLeafNode:
    def __init__(self):
        self.isRed = False
        self.data = None
        self.isLeaf = True
        self.isEvenSum = True
        self.data = 0 
    def __str__(self):
        return "B/N LEAF"
