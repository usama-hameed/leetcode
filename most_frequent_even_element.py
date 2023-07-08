from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = {}
        max_key = -1
        max_value = -1
        for num in nums:
            if num % 2 == 0:
                if num not in count:
                    count[num] = 1
                else:
                    count[num] += 1

        # print(count)
        for key, value in count.items():
            if value > max_value:
                max_key, max_value = key, value
            if max_value == value:
                max_key = min(max_key, key)

        return max_key


s = Solution()
print(s.mostFrequentEven([0, 1, 2, 0, 0, 0, 2, 4, 4, 1]))
