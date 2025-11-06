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
    
    def printLL(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    
    def remove(self,index):
        if index < 0 or index >=self.length:
            return None
        else:
            prev=self.get(index-1)
            temp=prev.next
            prev.next=temp.next
            temp.next=None
            self.length-=1
            return temp
        
my_linked_list=LinkList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.printLL()
print("Removed value:", my_linked_list.remove(2).value)  # Output: Removed value: 3
my_linked_list.printLL()
