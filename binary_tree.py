import numpy as np

class Node:
    right = None
    left = None
    value = 0

    def __init__(self, value):
        self.value = value

class BinarySearchTree:
    root = None

    def __init__(self):
        pass

    def insertion(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.addNode(self.root, value)

    def addNode(self, root, value):
        if value > root.value:
            if root.right is not None:
                self.addNode(root.right, value)
            else:
                root.right = Node(value)
        elif value < root.value:
            if root.left is not None:
                self.addNode(root.left, value)
            else:
                root.left = Node(value)
    @profile
    def search(self, value):
        if self.root is None:
            return False

        return self.checkNode(self.root, value)
    
    def checkNode(self, root, value):
        if root.value > value:
            if root.left is None:
                return False
            return self.checkNode(root.left, value)
        elif root.value < value:
            if root.right is None:
                return False
            return self.checkNode(root.right, value)
        else:
            return True

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)

def generateList(lowerBound, upperBound, step=1):
    ints = np.arange(lowerBound, upperBound + 1, step)
    return ints

def prepareTree(data, tree):
    for i in data:
        tree.insertion(i)
        
@profile
def indexSearch(data, val):
    for i in data:
        if i == val:
            return True
    return False

myTree = BinarySearchTree()
data = generateList(1, 10000)
prepareTree(data, myTree)
#myTree.inorder(myTree.root)
num = 1283

print(myTree.search(num))
print(indexSearch(data, num))
