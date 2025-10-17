# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def get_most_left(node):
            if node.left is None:
                return node.val
            else:
                return get_most_left(node.left)
        def get_most_right(node):
            if node.right is None:
                return node.val
            else:
                return get_most_right(node.right)
        def helper(node, current_minimum):
            if node.left is None and node.right is None:
                return current_minimum
            elif node.right is None:
                return helper(node.left, min(current_minimum, node.val - get_most_right(node.left)))
            elif node.left is None:
                return helper(node.right, min(current_minimum, get_most_left(node.right) - node.val))
            else:
                return min(helper(node.left, min(current_minimum, node.val - get_most_right(node.left))), helper(node.right, min(current_minimum, get_most_left(node.right) - node.val)))
        return helper(root, 99999999)