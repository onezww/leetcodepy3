class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        result = 0
        tmp = x
        while tmp:
            result = result * 10 + tmp % 10
            tmp = tmp // 10

        return True if result == x else False
