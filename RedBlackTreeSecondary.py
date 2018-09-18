#Secondary Red Black Tree Methods
#applies the fixup for the three insertion fixup cases
def insertFixup(tree,z):
        insertFixupA(tree.root,z)
        insertFixupB(tree.root,z)
        insertFixupC(tree.root,z)
        tree.root.isRed = False
#right rotates the tree on x
#updates isEvenSum 
def rightRotate(tree,x):
        y = x.leftChild
        b = y.rightChild
        transplant(tree,x,y)
        x.leftChild = b
        if b != None:
            b.parent = x
        y.rightChild = x
        x.parent = y
        yEvenSum = y.isEvenSum
        if b.isEvenSum != x.isEvenSum:
            y.isEvenSum = not y.isEvenSum
        if b.isEvenSum != yEvenSum:
            x.isEvenSum = not x.isEvenSum
        y.isLeftChild = x.isLeftChild
        x.isLeftChild = False
        b.isLeftChild = True
#left rotates the tree on x
#updates isEvenSum 
def leftRotate(tree,x):
        y = x.rightChild
        b = y.leftChild
        transplant(tree,x,y)
        x.rightChild = b
        if b != None:
            b.parent = x
        y.left = x
        x.parent = y
        xEvenSum = x.isEvenSum
        if b.isEvenSum != y.isEvenSum:
            x.isEvenSum = not x.isEvenSum
        if b.isEvenSum != xEvenSum:
            y.isEvenSum = not y.isEvenSum
        x.isLeftChild = y.isLeftChild
        y.isLeftChild = False
        b.isLeftChild = True
#finds the sibling of the node
def sibling(node):
        if node.isLeftChild:
            return node.parent.rightChild
        else:
            return node.parent.leftChild
#transplants u into v
def transplant(tree,u, v):
        parent = u.parent
        if parent == None:
            tree.root = v
        elif u.isLeftChild:
            parent.leftChild = v
        else:
            parent.rightChild = v
        if v != None:
            v.parent = parent
#fixup for red black tree insert case 1
def insertFixupA(root,z):
        while (z != root) and (z.parent.isRed):
            y = sibling(z.parent)
            if not y.isRed:
                return
            z.parent.isRed = False
            y.isRed = False
            z = z.parent.parent
            z.isRed = True
#fixup for red black tree insert case 1
def insertFixupB(root,z):
        if z == root or not z.parent.isRed:
            return
        x = z.parent
        w = x.parent
        if z == x.rightChild and x == w.leftChild:
            z = x
            leftRotate(root,x)
        elif z == x.leftChild and x == w.rightChild:
            z = x
            rightRotate(root,x)
#fixup for red black tree insert case 1
def insertFixupC(root,z):
        if z == root or not z.parent.isRed:
            return
        x = z.parent
        w = x.parent
        if z == x.leftChild and x == w.leftChild:
            rightRotate(root,w)
            x.isRed = False
            w.isRed = True
        elif z == x.rightChild and x == w.rightChild:
            leftRotate(root, w)
            x.isRed = False
            w.isRed = True




        

