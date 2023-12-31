class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traversal():
        if self.head is None:
            print('LinkedList is empty!')
        else:
            a = self.head
            while a.next is not None:
                print(a.data)
                a = a.next

ll = LinkedList()
n1 = Node(5)
ll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3
n4 = Node(20)
n3.next = n4 
n5 = Node(25)
n4.next = n5 

ll.traversal()
