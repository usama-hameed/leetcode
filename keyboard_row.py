from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        return list(filter(self.is_possible, words))

    def is_possible(self, word):
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        for row in rows:
            if word[0].lower() in row:
                for ch in word:
                    if ch.lower() not in row:
                        return False
        return True


s = Solution()
print(s.findWords(["adsdf","sfd"]))


'''
[cba] -> abc -> 'asdfghjkl'(sorted) -> r

'''