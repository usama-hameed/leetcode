from typing import List
import string


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabets = list(string.ascii_lowercase)

        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
                 ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--",
                 "-..-","-.--","--.."]

        final = set()
        for word in words:
            main = ""
            for w in word:
                index = alphabets.index(w)
                main = main + codes[index]
            final.add(main)
        return len(final)


s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
