class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        newNode = Node(value)
        self.top = newNode
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_stack = Stack(3)
print(my_stack.top.value)      # Output: 3
print(my_stack.height)         # Output: 1
my_stack.print_stack()         # Output: 3