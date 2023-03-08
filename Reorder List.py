# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle of the linked list with slow and fast approach
        slow, fast = head, head
        # while fast.next and fast.next.next is not None move the pointer
        while fast.next and fast.next.next:
            # move slow pointer one step
            slow = slow.next
            # move fast pointer two steps
            fast = fast.next.next

        # in order to reverse the second list do the following:

        # create a pointer to keep track of the information of the previous pointer
        previous_ptr = None
        # create a pointer to store the instant node information and assign it to beginning of the second list
        curr_ptr = slow.next
        # while current pointer is not None
        while curr_ptr:
            # store the next pointer of the instant node
            next_ptr = curr_ptr.next
            # assign the previous pointer to the current pointer next
            curr_ptr.next = previous_ptr
            # assign the previous pointer with current
            previous_ptr = curr_ptr
            # assign the current pointer with next
            curr_ptr = next_ptr
        # assign the next pointer of the slow pointer to None
        slow.next = None

        # in order to merge the two lists do the following:

        # create a pointer to keep track of the first list
        head_of_first_list = head
        # create a pointer to keep track of the second list
        head_of_second_list = previous_ptr
        # while the second list is not None
        while head_of_second_list:
            # store the next pointer of the first list
            next_ptr = head_of_first_list.next
            # assign the second list to the next pointer of the first list
            head_of_first_list.next = head_of_second_list
            # assign the second list to the first list
            head_of_first_list = head_of_second_list
            # assign the next pointer of the first list to the second list
            head_of_second_list = next_ptr

