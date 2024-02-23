from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        final = [[1], [1, 1]]


        count = 2
        inner_list = [1]
        index = 1
        while count < rowIndex+1:
            if index < len(final[-1]):
                inner_list.append(final[-1][index] + final[-1][index-1])
                index += 1
            else:
                inner_list.append(1)
                final.append(inner_list)
                count += 1
                inner_list = [1]
                index = 1

        return final[-1]

s = Solution()
print(s.getRow(2))
