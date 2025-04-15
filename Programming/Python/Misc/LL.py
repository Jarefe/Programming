class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtFront(data)
            return
        
        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def updateNode(self, data, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next
        
        if current_node is not None:
            current_node.data = data
        else:
            print("Index not present")

    def removeFirstNode(self):
        if self.head is None:
            return
        
        self.head = self.head.next

    def removeLastNode(self):
        if self.head.next is None:
            self.head = None
            return
        
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def removeAtIndex(self,index):
        if self.head is None:
            return
        
        if index == 0:
            self.removeFirstNode()
            return

        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position +=1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    def remove_node(self,data):
        current_node = self.head

        if current_node is not None and current_node.data == data:
            self.removeFirstNode
            return
        
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        print("Node with the given data not found")

    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size
    
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next