class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_for_s = {}
        dict_for_t = {}

        for i, j in zip(s, t):
            dict_for_s[i] = 1 + dict_for_s.get(i, 0)
            dict_for_t[j] = 1 + dict_for_t.get(j, 0)

        # checking anagrams
        for key, value in dict_for_t.items():
            if key not in dict_for_s or dict_for_s[key] != value:
                return False
        return True


s = Solution()
print(s.isAnagram(s = "rat", t = "car"))
