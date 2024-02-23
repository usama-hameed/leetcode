from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g) < 1 or len(s) < 1:
            return 0
        done = []
        count = 0
        for x in g:
            for index,y in enumerate(s):
                if y >= x and index not in done:
                    count += 1
                    done.append(index)
                    break
        return count


s = Solution()
print(s.findContentChildren([1,2,3], [1,1]))

'''
input g = [1,1,3] s = [1,1]

[1,

g[i] >= s[i] =>> count++ 



'''