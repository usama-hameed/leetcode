class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = '123456789'
        negative_number = False
        new_str = ''
        for i in s.strip():
            if i not in '+-' and i not in numbers:
                break
            elif i == '-':
                negative_number = True
            elif i and i in numbers:
                new_str += i

        if not new_str:
            return 0
        if negative_number:
            value = int(new_str) * (-1)
            value = min(value, 2 ** 31 - 1)
            value = max(-(2 ** 31), value)
            return value
        else:
            value = min(int(new_str), 2 ** 31 - 1)
            value = max(-(2 ** 31), value)
            return value


s = Solution()
print(s.myAtoi("-91283472332"))
