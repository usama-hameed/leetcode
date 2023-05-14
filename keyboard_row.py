from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        inputs = ('qwertyuiop', 'asdfghjkl', 'zxcvbnm')
        final = []
        for word in words:
            for inp in inputs:
                if word[0].lower() in inp:
                    if self.is_exist(word, inp):
                        final.append(word)
        return final

    def is_exist(self, word, inp):
        for w in word:
            if w.lower() not in inp:
                return False
        return True


s = Solution()
print(s.findWords(["omk"]))
