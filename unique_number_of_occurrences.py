from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = dict()
        for a in arr:
            if a in count:
                count[a] += 1
            else:
                count[a] = 1

        to_list = list(count.values())
        to_set = set(to_list)

        if len(to_set) != len(to_list):
            return False
        return True


s = Solution()
print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
