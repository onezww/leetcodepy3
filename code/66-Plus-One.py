class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:

        if not digits:
            return []

        index = len(digits) - 1
        carry = 1
        while index >= 0:
            if carry:
                digits[index] += carry

            carry = digits[index] // 10
            digits[index] = digits[index] % 10
            if carry:
                index -= 1
            else:
                return digits

        if carry:
            return [1] + digits
