# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create two pointer, one of them is for iteration the other one will be head of the new linkedlist
        current_node = temp_node = ListNode()
        # iterate over the list to one of them will be None
        while list1 and list2:
            # if the list1 value is smaller one
            if list1.val < list2.val:
                # adjust the pointers
                temp_node.next = list1
                list1 = list1.next
            # if the list2 value is smaller one
            else:
                # adjust the pointers
                temp_node.next = list2
                list2 = list2.next
            # move the pointer to the right
            temp_node = temp_node.next
        # if the list1 is not None
        if list1:
            # adjust the pointers
            while list1:
                temp_node.next = list1
                list1 = list1.next
                temp_node = temp_node.next
        # if the list2 is not None
        else:
            # adjust the pointers
            while list2:
                temp_node.next = list2
                list2 = list2.next
                temp_node = temp_node.next
        # return the head of the new linkedlist
        return current_node.next