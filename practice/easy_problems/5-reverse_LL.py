# # https://leetcode.com/problems/reverse-linked-list/

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def reverseList(self, head):

    
# if __name__ == "__main__":
#     # Example usage:
#     node1 = ListNode(1)
#     node2 = ListNode(2)
#     node3 = ListNode(3)
#     node4 = ListNode(4)
#     node5 = ListNode(5)
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node5

#     reversed_head = Solution().reverseList(node1)
#     # Print reversed list
#     current = reversed_head
#     while current:
#         print(current.val)  # Output: 5 4 3 2 1
#         current = current.next