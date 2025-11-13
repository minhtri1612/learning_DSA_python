# https://leetcode.com/problems/merge-two-sorted-lists/description/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = current = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return dummy.next

if __name__ == "__main__":
    # Example usage:
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    merged_head = Solution().mergeTwoLists(node1, node4)
    # Print merged list
    current = merged_head
    while current:
        print(current.val)  # Output: 1 1 2 3 4 4
        current = current.next  
