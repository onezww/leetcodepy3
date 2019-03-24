class Solution:

    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ""

        min_str = min(strs, key=lambda x: len(x))

        result = ""
        for i, c in enumerate(min_str):

            for one in strs:
                if one[i] != min_str[i]:
                    return result

            result += min_str[i]
        return result
