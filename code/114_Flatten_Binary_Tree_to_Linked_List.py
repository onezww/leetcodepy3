# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        nodes = []
        self._dp(root, nodes)
        head = root
        for i in range(1, len(nodes)):
            head.left = None
            head.right = nodes[i]
            head = nodes[i]

    def _dp(self, root, list_node):
        if not root:
            return None

        list_node.append(root)
        self._dp(root.left, list_node)
        self._dp(root.right, list_node)
        return
