class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        start = 0
        end = len(s) - 1
        s = list(s)
        while start < end:
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            if s[start] not in vowels:
                start += 1
            if s[end] not in vowels:
                end -= 1

        return ''.join(s)


s = Solution()

print(s.reverseVowels('hello'))

'''
s = e o l l h
p1 = 0
p2 = s.length() - 1
p1++
p2 --
vo = aeiou
'''