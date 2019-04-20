# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True

        _, flag = self.handler(root)
        return flag

    def handler(self, root):
        if root is None:
            return 0, True

        left_depth, left_flag = self.handler(root.left)
        right_depth, right_flag = self.handler(root.right)

        if not left_flag or not right_flag:
            return max(left_depth, right_depth)+1, False

        flag = True if abs(left_depth - right_depth) <= 1 else False
        return max(left_depth, right_depth)+1, flag
