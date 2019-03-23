class Solution:

    def reverse(self, x: 'int') -> 'int':
        if x == 0:
            return 0
        result = 0
        if x < 0:
            result = int(str(-1 * x)[::-1])
        elif x > 0:
            result = int(str(x)[::-1])

        if x > 0 and result < 2**31:
            return int(result)
        if x < 0 and result <= 2**31:
            return -int(result)
        return 0
