class Solution:

    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1
        flag = True
        while i < j:
            left, right = '', ''
            while i <= j:
                flag = False
                left, ok = self.get_c(s[i])
                if ok:
                    break

                i += 1

            while i <= j:
                right, ok = self.get_c(s[j])
                if ok:
                    break

                j -= 1

            if left == right:
                i += 1
                j -= 1
                flag = True
            else:
                return False

        return flag

    def get_c(self, c):
        if c.isdigit() or c.isalpha():
            return c.lower(), True
        else:
            return "", False
