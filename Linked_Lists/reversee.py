class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkList:
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

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
    
    def reverse(self):
        if self.head is None or self.head.next is None:
            return self.head
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True
    
my_linked_list = LinkList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
print("Original linked list:")
my_linked_list.printLL()
print("Reversed linked list:")
my_linked_list.reverse()
my_linked_list.printLL()