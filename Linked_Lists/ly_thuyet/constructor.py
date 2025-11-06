class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

my_linked_list = LinkList(5)
print("Head:", my_linked_list.head.value)  # Output: Head: 5