from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        check = {}
        for index, value in enumerate(arr):
            print(check)
            if (value * 2) in check and check[(value*2)] < index:
                return True
            check[value] = index
        return False


s = Solution()
print(s.checkIfExist([7,1,14,11]
))
