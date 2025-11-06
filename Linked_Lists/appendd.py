class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.length+=1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkList(1)
my_linked_list.print_list()
my_linked_list.append(2)
my_linked_list.print_list()