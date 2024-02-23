from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        simple_case = {1: [[1]], 2: [[1], [1, 1]]}
        if numRows in simple_case:
            return simple_case[numRows]

        final = [[1], [1, 1]]
        count = 2
        inner_list = []
        index = 1
        while count < numRows:
            if index < len(final[-1]):
                inner_list.append(final[-1][index] + final[-1][index-1])
                index += 1
            else:
                inner_list.insert(0, 1)
                inner_list.insert(len(inner_list), 1)
                final.append(inner_list)
                count += 1
                inner_list = []
                index = 1

        return final


s = Solution()
print(s.generate(1))
