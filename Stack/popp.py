class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        newNode = Node(value)
        self.top = newNode
        self.height = 1

    def pop(self):
        if self.height == 0:
            return None
        temp=self.top
        self.top=self.top.next
        temp.next=None
        self.height-=1
        return temp
    def push(self,value):
        newNode=Node(value)
        if self.height==0:
            self.top=newNode
        else:
            newNode.next=self.top
            self.top=newNode
        self.height+=1

    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next


my_stack = Stack(3)
my_stack.push(5)
my_stack.push(7)
my_stack.print_stack()
popped_node = my_stack.pop()
print("Popped node value:", popped_node.value)  # Output: 7
my_stack.print_stack()