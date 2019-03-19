
'''
    两个非空的链表，链表中每个节点是非负整型。数字是三反序进行存储的，让这两数相加，和用链表返回。
    注意:
        题目假设没有前导0，除了零本身。
    Solution:
        中规中矩，遍历一遍，两两相加，注意进位1
        时间复杂度O(n), 空间复杂度O(n)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        head = ListNode(0)
        previous = None
        current = head
        flag = 0
        while True:
            if not l1 and not l2:
                break

            if previous:
                previous.next = ListNode(0)
                current = previous.next

            tmp_sum = flag
            if(l1):
                tmp_sum += l1.val
                l1 = l1.next

            if(l2):
                tmp_sum += l2.val
                l2 = l2.next

            flag = tmp_sum // 10
            current.val = tmp_sum % 10
            previous = current
            if flag:
                previous.next = ListNode(1)

        return head
