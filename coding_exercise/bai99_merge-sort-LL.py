class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self,arr):
        # Merge two sorted linked lists (self and arr) into self in-place.
        # If one list is empty, keep the other.
        if arr is None or arr.head is None:
            return self.head, self.tail, self.length

        # If self is empty, adopt arr
        if self.head is None:
            self.head = arr.head
            self.tail = arr.tail
            self.length = arr.length
            return self.head, self.tail, self.length

        ptr1 = self.head
        ptr2 = arr.head

        dummy = Node(0)
        tail = dummy

        # Merge by re-linking existing nodes
        while ptr1 is not None and ptr2 is not None:
            if ptr1.value <= ptr2.value:
                tail.next = ptr1
                ptr1 = ptr1.next
            else:
                tail.next = ptr2
                ptr2 = ptr2.next
            tail = tail.next

        # Attach the remaining nodes
        if ptr1 is not None:
            tail.next = ptr1
        elif ptr2 is not None:
            tail.next = ptr2

        # Update head
        self.head = dummy.next

        # Update tail: find last node (tail may not be correct yet)
        t = self.head
        last = t
        count = 0
        while t is not None:
            last = t
            t = t.next
            count += 1

        self.tail = last
        # Update length: if lengths available on arr and self, sum them; else use counted length
        try:
            self.length = self.length + arr.length
        except Exception:
            self.length = count

        return self.head, self.tail, self.length
    
    
        
    


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""