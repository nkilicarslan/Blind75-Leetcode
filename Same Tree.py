# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check both root reached null or not
        if p == None and q == None:
            # if both of them null or none return true
            return True
        # check one of the root reached null or not
        elif p == None or q == None:
            # if one of them null and other one is not null return false
            return False
        # if both node value is equal, go on to recursion
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
        # if the value of the nodes are not equal return false
            return False
