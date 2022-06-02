# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printSLL(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next


# Singly Linked List with insertion and print methods
SLL = LinkedList()
SLL.insert(4)
SLL.insert(5)
SLL.insert(6)
SLL.printSLL()


