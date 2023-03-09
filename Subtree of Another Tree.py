# Description: Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
def isSameTree(root, subRoot):
    # check both root reached null or not
    if root == None and subRoot == None:
        # if both of them null or none return true
       return True
    # check one of the root reached null or not
    elif root == None or subRoot == None:
        # if one of them null and other one is not null return false
        return False
    # if both node value is equal, go on to recursion
    elif root.val == subRoot.val:
        # return the left child and right child
        return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
    else:
        # if the value of the nodes are not equal
        return False

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check the recursion is reached the base case or not
        if root is None:
            # if root node is reached the null return 0
            return False
        # if the root is equal to the subroot
        if isSameTree(root, subRoot):
            # return true
            return True
        # otherwise return the left child and right child
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)