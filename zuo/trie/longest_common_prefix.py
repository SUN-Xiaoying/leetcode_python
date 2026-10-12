# https://leetcode.com/problems/longest-common-prefix/description/?envType=problem-list-v2&envId=trie
from typing import List


class Solution:
    # TODO: What is  s.startswith?
    # 0ms Beats 100.00%
    def longestCommonPrefix_best(self, strs: List[str]) -> str:
        if not strs: return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # shrink prefix from the end
                if not prefix:
                    return ""

        return prefix

    # 7ms Beats 4.61%
    def longestCommonPrefix_mine(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = strs[0]
        for string in strs[1:]:
            count = 0
            while count < len(result) and count < len(string) and result[count] == string[count]:
                count += 1
            if count == 0:
                return ""
            result = result[:count]

        return result

s = Solution()
# "fl"
# print(s.longestCommonPrefix(["flower","flow","flight"]))
# "aa"
print(s.longestCommonPrefix(["aaa","aa","aaa"]))