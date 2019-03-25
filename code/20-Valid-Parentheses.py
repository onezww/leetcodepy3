class Solution:

    def isValid(self, s: 'str') -> 'bool':
        start_brackets = {'{', '(', '['}
        big_brackets = {'{', '}'}
        midle_brackets = {'[', ']'}
        little_brackets = {'(', ')'}
        stack_list = list()
        s = s.strip()
        for v in s:
            if v == " ":
                continue
            if v in start_brackets:
                stack_list.append(v)
            else:
                if not len(stack_list):
                    return False

                tmp_set = {v, stack_list[-1]}
                if tmp_set == big_brackets or tmp_set == midle_brackets or tmp_set == little_brackets:
                    stack_list.pop(-1)
                else:
                    return False

        return False if len(stack_list) else True
