from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        main = {}
        count = 0
        for s in strs:
            for i, w in enumerate(s):
                if i not in main:
                    main[i] = [w]
                else:
                    main[i].append(w)

        for key, value in main.items():
            sample = value.copy()
            main[key].sort()
            if sample != main[key]:
                count += 1
        return count


s = Solution()
s.minDeletionSize(["cba", "daf", "ghi"])
