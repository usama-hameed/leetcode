from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = [[1], [1, 1]]
        if numRows < 3:
            return final[numRows:]

        count = 2
        inner_list = [1]
        index = 1
        while count < numRows:
            if index < len(final[-1]):
                inner_list.append(final[-1][index] + final[-1][index-1])
                index += 1
            else:
                inner_list.append(1)
                final.append(inner_list)
                count += 1
                inner_list = [1]
                index = 1

        return final


s = Solution()
print(s.generate(5))
