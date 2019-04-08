# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:

        return self._handler(root, None, None)

    def _handler(self, root, min_val=None, max_val=None):
        if not root:
            return True

        if min_val is not None and root.val <= min_val:
            return False
        if max_val is not None and root.val >= max_val:
            return False

        return min(self._handler(root.left, min_val, root.val), self._handler(root.right, root.val, max_val))
