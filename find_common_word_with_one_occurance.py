from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        first_dict = {}
        count = 0

        for word in words1 + words2:
            if word not in first_dict:
                first_dict[word] = 1
            else:
                first_dict[word] += 1

        for key, value in first_dict.items():
            if first_dict[key] == 2 and key in words1 and key in words2:
                    count += 1

        return count


s = Solution()
print(s.countWords(words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]))
