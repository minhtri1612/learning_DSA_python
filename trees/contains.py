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
    
    def contains(self,value):
        if self.root is None:
            return False
        temp=self.root
        while temp is not None:
            if value < temp.value:
                temp=temp.left
            elif value > temp.value:
                temp=temp.right
            else:
                return True
        return False
    
mytree=Tree()
mytree.insert(2)
mytree.insert(1)       
mytree.insert(3)
print(mytree.root.value)
print(mytree.root.left.value)
print(mytree.root.right.value)
print(mytree.contains(2))
print(mytree.contains(1))
print(mytree.contains(3))
print(mytree.contains(4))