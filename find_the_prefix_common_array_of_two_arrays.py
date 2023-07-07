from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []

        for index, value in enumerate(A):
            if index == 0:
                if A[0] == B[0]:
                    C.append(1)
                else:
                    C.append(0)
            else:
                total = self.common_elements(A[0:index+1], B[0:index+1])
                C.append(total)
        return C

    def common_elements(self, A: List[int], B: List[int]):
        exist = 0

        for a in range(len(A)):
            if A[a] in B:
                exist += 1
        return exist


s = Solution()
print(s.findThePrefixCommonArray([9,1,3,2,4], [8,3,1,2,4]))
