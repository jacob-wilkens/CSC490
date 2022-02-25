#the left sibling child position is parent * 2, right sibling child position is parrent * 2 + 1
def GetParentPosition(position):    #get the parent position from child position
    return position // 2

class MinHeap:
    array = []
    count = 0

    def __init__(self):
        self.array.append({
            "value": 0,
            "index": 0,
            "connect": 0
        })

    def swap(self, first, second):
        self.array[first], self.array[second] = self.array[second], self.array[first]

    def determineNode(self, parentNode, leftNode, rightNode):
        node = 0 #node = 1, means the leftNode is the smallest, and node = 2 means the rightNode is the smallest
        if leftNode is not None and leftNode["value"] < parentNode["value"]:
            node = 1
        if rightNode is not None and ((node == 1 and rightNode["value"] < leftNode["value"]) or (node == 0 and rightNode["value"] < parentNode["value"])):
            node = 2

        return node

    def HeapPush(self, value, index, connect):  #add a new node to the tree
        self.array.append({
            "value": value,
            "index": index,
            "connect": connect
        })
        self.count += 1
        self.Heapify(self.Size(), "Up")

    def ExtrudeMin(self):   #take out the root and rebalance the tree
        returnNode = self.GetNode(1)
        lastNode = self.array.pop()
        self.count -= 1
        if self.count > 0:
            self.array[1] = lastNode
        self.Heapify(1, "Down")
        return returnNode

    def Heapify(self, position, direction):  #balance the Heap Tree from low to high
        if position <= 1 and direction == "Up":
            return

        parentPosition = position

        if direction == "Up":
            parentPosition = GetParentPosition(position)

        leftPosition = parentPosition * 2
        rightPosition = parentPosition * 2 + 1

        node = self.determineNode(self.GetNode(parentPosition), self.GetNode(leftPosition), self.GetNode(rightPosition))

        if node == 1:
            self.swap(leftPosition, parentPosition)
            if direction == "Down":
                self.Heapify(leftPosition, direction)
        elif node == 2:
            self.swap(rightPosition, parentPosition)
            if direction == "Down":
                self.Heapify(rightPosition, direction)

        if node != 0 and direction == "Up":
            self.Heapify(parentPosition, direction)

    def Size(self):
        return self.count

    def GetNode(self, position):    #when position is not out of array range, return node. Otherwise return None
        if position > self.count:
            return None #python has None as not exist
        else:
            return self.array[position]
