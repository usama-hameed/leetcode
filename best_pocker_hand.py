from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        card_rank = {}
        if len(set(suits)) == 1:
            return 'Flush'
        else:
            for i in ranks:
                if i not in card_rank:
                    card_rank[i] = 1
                else:
                    card_rank[i] += 1

        max_value = max(list(card_rank.values()))
        if max_value >= 3:
            return "Three of a Kind"
        elif max_value >= 2:
            return "Pair"
        return "High Card"


s = Solution()
print(s.bestHand([2,1,2,1,1], ["d","b","a","a","d"]))
