# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return None

        previous = head

        l = head.next
        while l:
            if l.val == previous.val:
                l = l.next
                previous.next = l
            else:
                previous = l
                l = l.next

        return head
