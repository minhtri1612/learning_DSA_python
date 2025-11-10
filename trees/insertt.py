class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree: 
    def __init__(self):
        self.root=None

    def insert(self,value):
        newNode=Node(value)
        if self.root is None:
            self.root=newNode
            return
        temp=self.root
        while True:
            if newNode.value < temp.value:
                if temp.left is None:
                    temp.left=newNode
                    return
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=newNode
                    return
                temp=temp.right

mytree=Tree()
mytree.insert(2)
mytree.insert(1)
mytree.insert(3)
print(mytree.root.value)
print(mytree.root.left.value)
print(mytree.root.right.value)