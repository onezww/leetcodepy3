# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        next_nodes = [root]
        while next_nodes:
            if len(next_nodes) != 1:
                right = len(next_nodes) // 2
                left = right - 1
                while left >= 0 and right < len(next_nodes):
                    if (next_nodes[left] is None and next_nodes[right] is not None):
                        return False
                    if (next_nodes[left] is not None and next_nodes[right] is None):
                        return False
                    if next_nodes[left] is not None and next_nodes[left].val != next_nodes[right].val:
                        return False
                    left -= 1
                    right += 1

            tmp_nodes = []
            for node in next_nodes:
                if node:
                    tmp_nodes.append(node.left)
                    tmp_nodes.append(node.right)

            if len(tmp_nodes) % 2 != 0:
                return False
            next_nodes = tmp_nodes
        return True
