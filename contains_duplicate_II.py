from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        save_index = dict()

        for index, value in enumerate(nums):
            if value in save_index:
                if abs(save_index[value] - index) <=k:
                    return True
            save_index[value] = index
        return False


s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))
