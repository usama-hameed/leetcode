from typing import List
import string


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        main_dict = {}
        alphabets = list(string.ascii_lowercase)
        for key, value in enumerate(s):
            if value not in main_dict:
                main_dict[value] = [key]
            else:
                main_dict[value].append(key)
        print(main_dict)
        for key, value in main_dict.items():
            res = (value[1] - value[0]) - 1
            print(res)
            if alphabets[value[0]] in s:
                if distance[value[0]] != res:
                    return False
        return True


s = Solution()
print(s.checkDistances(s="zz", distance=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]))
