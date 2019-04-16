# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def sortedListToBST(self, head: 'ListNode') -> 'TreeNode':
        if not head:
            return None

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return self.handler(nums, 0, len(nums) - 1)

    def handler(self, nums, left_index, right_index):
        if left_index > right_index:
            return None

        if left_index == right_index:
            return TreeNode(nums[left_index])
        else:
            index = (left_index + right_index) // 2
            tmp = TreeNode(nums[index])
            tmp.left = self.handler(nums, left_index, index - 1)
            tmp.right = self.handler(nums, index + 1, right_index)
            return tmp
