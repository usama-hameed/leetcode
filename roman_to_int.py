class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        add = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sub = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        done = False
        for i, j in enumerate(s):
            if done:
                done = False
                continue
            if i + 1 < len(s):
                if s[i] + s[i+1] in sub:
                    print(s[i] + s[i+1])
                    total = total + sub[s[i] + s[i+1]]
                    done = True

                elif not done and j in add:
                    total = total + add[j]
            else:
                total = total + add[j]

        return total


s = Solution()
print(s.romanToInt('MCDLXXVI'))
