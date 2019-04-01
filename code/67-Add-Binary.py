class Solution:

    def addBinary(self, a: 'str', b: 'str') -> 'str':
        if not a and not b:
            return '0'

        result = ''
        carry = 0
        a_index = len(a) - 1
        b_index = len(b) - 1
        while a_index >= 0 or b_index >= 0:

            sum = carry
            if a_index >= 0:
                sum += int(a[a_index])
            if b_index >= 0:
                sum += int(b[b_index])
            carry = sum // 2
            result += str(sum % 2)
            a_index -= 1
            b_index -= 1
        if carry:
            result += '1'
        return result[::-1]
