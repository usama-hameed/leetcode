class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {')': '(', ']': '[', '}': '{'}
        check = []

        for i in s:
            if i in parenthesis.values():
                check.append(i)
            elif check:
                if check.pop() != parenthesis[i]:
                    return False
            elif not check and i not in parenthesis.values():
                return False
        if check:
            return False
        else:
            return True


s = Solution()
print(s.isValid('('))
