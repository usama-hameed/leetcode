from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        main_dict = {}

        for index_l1, value_l1 in enumerate(list1):
            for index_l2, value_l2 in enumerate(list2):
                if value_l1 == value_l2:
                    main_dict[value_l1] = index_l1 + index_l2

        sorted_dict = dict(sorted(main_dict.items(), key=lambda item: item[1]))
        first_key = next(iter(sorted_dict))
        final=[]
        final.append(first_key)
        val = sorted_dict[first_key]
        del sorted_dict[first_key]
        for key, value in sorted_dict.items():
            if value == val:
                final.append(key)
        return final


s = Solution()
print(s.findRestaurant(list1=["happy", "sad", "good"],
                       list2=["sad", "happy", "good"]))
