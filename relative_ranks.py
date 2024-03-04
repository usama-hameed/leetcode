from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_dict = {}
        medal_dict = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}
        for index, value in enumerate(score):
            score_dict[index] = value

        sorted_score_dict = sorted(score_dict.items(), key=lambda a: a[1], reverse=True)

        count = 1

        for index, value in sorted_score_dict:

            if count in medal_dict:
                score[index] = medal_dict[count]
            else:
                score[index] = str(count)
            count += 1

        return score


s = Solution()
print(s.findRelativeRanks([5, 4, 3, 2, 1]))
