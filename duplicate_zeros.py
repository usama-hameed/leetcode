from  typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        if 0 in arr:
            actual_length = len(arr)
            pointer = 0
            while len(arr) == actual_length and pointer < len(arr):
                if arr[pointer] == 0:
                    arr.pop()
                    arr.insert(pointer + 1, 0)
                    pointer += 1

                pointer += 1




s = Solution()
s.duplicateZeros([1,0,2,3,0,4,5,0])
