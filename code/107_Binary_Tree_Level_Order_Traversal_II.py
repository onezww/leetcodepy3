# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []

        height = self._height(root)
        result = [list() for i in range(height)]
        next_nodes = [root]
        while next_nodes:
            height -= 1
            tmp_nodes = []
            for node in next_nodes:
                result[height].append(node.val)
                if node.left:
                    tmp_nodes.append(node.left)
                if node.right:
                    tmp_nodes.append(node.right)
            next_nodes = tmp_nodes

        return result

    def _height(self, root):
        if root is None:
            return 0

        return max(self._height(root.left), self._height(root.right)) + 1
