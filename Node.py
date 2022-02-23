# Creating a node class
class Node:
    def __init__(self, data):
        self.data = data  # adding data to the node
        self.next = None  # Initally this node will not be linked with any other node
        self.prev = None  # It will not be linked in either direction

    #get data of the node
    def getData(self):
        return self

    # set next of the Node
    def setNext(self, next):
        self.next = next

    # Get data of the Next Node
    def getNext(self):
        return self.next

    # set next of the Node
    def setPrevious(self, previous):
        self.prev = previous

    # Get data of the Next Node
    def getPrevious(self):
        return self.prev

    # Get if it has a Next
    def hasNext(self):
        return self.next is not None

    # Get if it has a Next
    def hasPrevious(self):
        return self.prev is not None