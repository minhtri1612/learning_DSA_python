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

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value
    
    def printLL(self):
        temp = self.head
        while(temp is not None):
            print(temp.value, end=" ")
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

my_linked_list = LinkList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
print("Value at index 2:", my_linked_list.get(2))  # Output
my_linked_list.printLL()
