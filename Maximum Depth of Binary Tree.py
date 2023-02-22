# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # check the recursion is reached the base case or not
        if root == None:
            # if root node is reached the null return 0
            return 0
        # otherwise take the maximum of left child and right child
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
