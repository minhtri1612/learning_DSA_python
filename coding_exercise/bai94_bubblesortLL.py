class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class linkedlist:
    def __init__(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        self.length=1

    def append(self,value):
        newNode=Node(value)
        if self.length==0:
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
        print(" ")

    def bubblesort(self):
        if self.length < 2:
            return
        for i in range(self.length-1):
            temp=self.head
            swapped=False
            while temp.next is not None:
                if temp.value > temp.next.value:
                    temp.value, temp.next.value = temp.next.value, temp.value
                    swapped=True
                temp=temp.next
            if not swapped:
                break
        return True


my_linked_list=linkedlist(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.printLL()
print("After sorting:")
my_linked_list.bubblesort()
my_linked_list.printLL()