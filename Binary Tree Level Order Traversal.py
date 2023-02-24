# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def PostorderTraverse(root, depth, level_by_node_value):
    # if the root is not None
    if root:
        # call left child with depth + 1 value
        PostorderTraverse(root.left, depth +1, level_by_node_value)
        # call right child with depth + 1 value
        PostorderTraverse(root.right, depth +1, level_by_node_value)
        # append the value to appropriate position in the list
        level_by_node_value[depth].append(root.val)

def maxDepth(node):
    # if the node value is Null just return 0
    if node is None:
        return 0

    else:
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # calculate the depth value of the given tree
        depth_value = maxDepth(root)
        # create a list to store every level node value
        level_by_node_value = [[] for i in range(depth_value)]
        # call a helper function to fill that list
        PostorderTraverse(root, 0 , level_by_node_value)
        # return that list
        return level_by_node_value
