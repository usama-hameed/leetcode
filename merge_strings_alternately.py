class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1, len_words2 = len(word1), len(word2)
        final = ''
        for i in range(max(len_word1, len_words2)):
            if i < len_word1:
                final += word1[i]
            if i < len_words2:
                final += word2[i]
        return final


s = Solution()
print(s.mergeAlternately("ab", "pqrs"))
