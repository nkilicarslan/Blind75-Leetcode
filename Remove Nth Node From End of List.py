# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create two pointer and assign them to head
        current_node = temp_node = ListNode()
        current_node = temp_node = head
        # create a variable to keep track of how many modes are in the linkedlist
        how_many_nodes = 0
        # iterate over the linkedlist and count the nodes
        while temp_node:
            how_many_nodes += 1
            temp_node = temp_node.next
        # if just one node return None
        if how_many_nodes == 1:
            return current_node.next
        # calculate the index from beginning
        deleted_node_index = how_many_nodes - n
        # iterate over the linkedlist
        while current_node:
            # decrease the index in every iteration
            deleted_node_index -= 1
            # if the deleted node is the head of the linkedlist
            if deleted_node_index == -1:
                head = head.next
                break
            # check the node will be deleted or not
            if deleted_node_index == 0:
                current_node.next = current_node.next.next
                break
            # move the pointer to the left
            current_node = current_node.next
        # return the head of the list
        return head