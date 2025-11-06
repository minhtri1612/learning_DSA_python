class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkList:
    def __init__(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        self.length=1

    def append(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.length+=1
        return True
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        else:
            newNode=Node(value)
            temp=self.get(index-1)
            newNode.next=temp.next
            temp.next=newNode
            self.length+=1
            return True

    def printLL(self):
        temp=self.head
        while(temp is not None):
            print(temp.value, end=" ")
            temp=temp.next
        print(" ")
my_linked_list=LinkList(1)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.printLL()
my_linked_list.insert(1,2)
my_linked_list.printLL()
