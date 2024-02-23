from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for x_axis, value in enumerate(grid):
            land = 4
            for y_axis, _ in enumerate(value):
                if grid[x_axis][y_axis] == 1:
                    if x_axis - 1 >= 0 and grid[x_axis-1][y_axis] == 1:
                        land -= 1
                    if x_axis + 1 < len(grid) and grid[x_axis+1][y_axis] == 1:

                        land -= 1

                    if y_axis - 1 >= 0 and grid[x_axis][y_axis-1] == 1:

                        land -= 1

                    if y_axis + 1 < len(grid[0]) and grid[x_axis][y_axis+1] == 1:

                        land -= 1
                    count += land
                land = 4
        return count


s = Solution()
print(s.islandPerimeter([[1,1]]))

'''
(0,0)   (0,1)
       1

(0,0),(0,1),(0,2),(0,3)  
[0,     1,    0,  0]

(1,0),(1,1),(1,2),(1,3)  
[1,     1,    1,   0]

(2,0),(2,1),(2,2),(2,3)  
[0,     1,    0,   0]

(3,0),(3,1),(3,2),(3,3)  
[1,     1,    0,    0]]

[0,1,0,0],
[1,1,1,0],
[0,1,0,0],
[1,1,0,0]]
'''