from typing import List
from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        char_checnk = {}
        for lp in licensePlate:
            if lp.isalpha():
                if lp.lower() not in char_checnk:
                    char_checnk[lp.lower()] = 1
                else:
                    char_checnk[lp.lower()] += 1

        return self.check(words, char_checnk)

    def check(self, words, char_checnk):
        final = []
        words.sort(key=len)
        for word in words:
            exist = True
            count_word = Counter(word)
            for key, value in count_word.items():
                if key in char_checnk:
                    if char_checnk[key] != value:
                        exist = False
            if exist:
                final.append(word)

        return final[0]


s = Solution()
print(s.shortestCompletingWord(licensePlate="1s3 PSt", words=["step", "steps", "stripe", "stepple"]))
