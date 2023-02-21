# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a previous pointer to keep the previous information
        prev = None
        # iterate over the linked list
        while head:
            # store the next pointer in the temporary variable
            tmp = head.next
            # change the orders
            head.next = prev
            # store the head pointer in the prev variable
            prev = head
            # move the pointer one point right
            head = tmp
        # return the new head of the linked list
        return prev