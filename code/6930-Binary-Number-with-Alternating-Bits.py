
class Solution:
    '''
    我的答案
    '''
    def hasAlternatingBits(self, n):
        flag = n & 0x1
        n = n >> 1
        while n:
            if not (n & 0x1) ^ flag:
                return False
            flag = n & 0x1
            n = n >> 1
        return True


class Solution:
    '''
    这个答案是在讨论区看到的时间复杂度O(1)
    数值在右移后与原值异或所有位都会变为1
    '''
    def hasAlternatingBits(self, n):
        if not n:
            return False
        num = n ^ (n >> 1)
        return not (num & (num + 1))


if __name__ == '__main__':
    s = Solution()
    s.hasAlternatingBits(90)
    import sys
    print(sys.path)
