class Solution:

    def generate(self, numRows: int) -> List[List[int]]:

        result = []
        for row in range(1, numRows + 1):
            result.append([1] * row)
            pre_levl, pre_levl_len = row - 2, row - 1
            level = row - 1
            for index in range(1, pre_levl_len):
                result[level][index] = result[pre_levl][index] + result[pre_levl][index - 1]

        return result
