# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if not l1 and not l2:
            return None

        head = None
        while l1 or l2:
            if not l1:
                if not head:
                    head = l2
                    break
                else:
                    current.next = l2
                    break
            elif not l2:
                if not head:
                    head = l1
                    break
                else:
                    current.next = l1
                    break

            if l1.val <= l2.val:
                choose_node = l1
                l1 = l1.next
            else:
                choose_node = l2
                l2 = l2.next

            if not head:
                head = choose_node
                current = head
            else:
                current.next = choose_node
                current = choose_node

        return head
