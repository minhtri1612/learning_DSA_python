class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

mytree=Tree()
mytree.root=Node(10)
mytree.root.left=Node(5)
mytree.root.right=Node(15)
mytree.root.left.left=Node(3)
mytree.root.left.right=Node(7)
mytree.root.right.right=Node(20)
print(mytree.root.value)
print(mytree.root.left.value)
print(mytree.root.right.value)      
