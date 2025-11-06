class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def prepend(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode

        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True
    
    def printLL(self):
        temp = self.head
        while(temp is not None):
            print(temp.value, end=" ")
            temp = temp.next

my_linked_list = LinkList(2)
my_linked_list.printLL()
print("\n")
my_linked_list.prepend(1)
my_linked_list.printLL()    
