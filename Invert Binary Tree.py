# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if this is the base case, just return None
        if root is None:
            return None
        # Create class object to store left child of that root
        left_node = TreeNode()
        left_node = self.invertTree(root.left)
        # Create class object to store right child of that root
        right_node = TreeNode()
        right_node = self.invertTree(root.right)
        # In order to invert the left and right child, assign them in reverse order
        root.left = right_node
        root.right = left_node
        # Return the root
        return root