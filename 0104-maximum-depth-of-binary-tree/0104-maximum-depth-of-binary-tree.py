# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def helper(node, current_count):
            if node.left is None and node.right is None:
                return current_count
            elif node.right is None:
                return helper(node.left, current_count + 1)
            elif node.left is None:
                return helper(node.right, current_count + 1)
            else:
                return max(helper(node.left, current_count + 1), helper(node.right, current_count + 1))
        return helper(root, 1)