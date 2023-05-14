class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        substring = ''
        count_substring = {}

        for sub in s:
            if sub not in substring:
                substring += sub
            else:
                count_substring[substring] = len(substring)
                if substring[-1] == sub:
                    substring = ''

                elif substring[0] == sub:
                    substring = substring.replace(sub, "")

                else:
                    index = substring.index(sub)
                    substring = substring[index+1:]
                substring += sub
        #         print(substring)
        # print(count_substring)
        if substring not in count_substring:
            count_substring[substring] = len(substring)
        sorted_count_substring = dict(sorted(count_substring.items(), key= lambda item: item[1], reverse=True))

        return list(sorted_count_substring.values())[0]


s = Solution()
print(s.lengthOfLongestSubstring("asljlj"))
# dvdf
