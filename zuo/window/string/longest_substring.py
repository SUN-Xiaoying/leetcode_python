# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    # 左 = Max{左, 上次位+1}
    # 23ms Beats 30.40%
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        hm = {}
        head = 0
        result = -1
        for i in range(len(s)):
            if s[i] in hm:
                head = max(head, hm[s[i]]+1)

            hm[s[i]]=i
            result = max(result, i - head + 1)

            print("TEMP: " + s[head:i+1] + "  RESULT: " + str(result))

        return result

s = Solution()
# # 3
# print(s.lengthOfLongestSubstring("pwwkew"))
# 4
print(s.lengthOfLongestSubstring("abcabcbb"))




