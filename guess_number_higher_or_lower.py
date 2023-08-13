# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pick = 1702766719

    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        # nums = [i for i in range(n+1)]
        start, end = 0, n
        while start < end:
            mid = (start + end) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                start = mid + 1
            elif res < 0:
                end = mid - 1
            # if mid == start:
            #     start += 1
            #
        return start


s = Solution()

print(s.guessNumber(2126753390))
