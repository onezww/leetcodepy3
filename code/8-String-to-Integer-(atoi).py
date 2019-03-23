class Solution:

    def myAtoi(self, str: 'str') -> 'int':
        min_num = -2**31
        max_num = 2**31 - 1
        str = str.strip()
        if not str:
            return 0
        if str[0] not in ('+', '-') and not str[0].isdigit():
            return 0
        elif str[0] in ('+', '-') and (len(str) < 2 or not str[1].isdigit()):
            return 0

        tmp_str = str[0]
        i = 1
        while i < len(str):
            if str[i].isdigit():
                tmp_str += str[i]
                i += 1
            else:
                break
        result = int(tmp_str)
        if result < 0 and result < min_num:
            return min_num
        elif result > 0 and result > max_num:
            return max_num
        return result
