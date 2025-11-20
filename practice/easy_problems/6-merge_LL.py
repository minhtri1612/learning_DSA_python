# # https://leetcode.com/problems/merge-two-sorted-lists/description/

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):

# if __name__ == "__main__":
#     # Example usage:
#     node1 = ListNode(1)
#     node2 = ListNode(2)
#     node3 = ListNode(4)
#     node1.next = node2
#     node2.next = node3

#     node4 = ListNode(1)
#     node5 = ListNode(3)
#     node6 = ListNode(4)
#     node4.next = node5
#     node5.next = node6

#     merged_head = Solution().mergeTwoLists(node1, node4)
#     # Print merged list
#     current = merged_head
#     while current:
#         print(current.val)  # Output: 1 1 2 3 4 4
#         current = current.next  
