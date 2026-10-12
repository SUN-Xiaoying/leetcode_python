from typing import List

# https://www.nowcoder.com/practice/92e6247998294f2c933906fdedbc6e6a
class Solution:

    def generatePermutation_simple(self, s: str) -> List[str]:
        """
            The empty string "" is considered a substring of every string.
        """
        result = set()
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                result.add(s[i:j])

        return list(result)

    def generatePermutation(self , s: str) -> List[str]:
        result = set()
        path = ""

        def dfs(i: int) :
            nonlocal path
            if i >= len(s) :
                result.add(path)
            else:
                path += s[i]
                dfs(i + 1)
                path = path[:-1]
                dfs(i + 1)

        dfs(0)

        return list(result)


s = Solution()
print(s.generatePermutation("abbc"))
print(s.generatePermutation_simple("abbc"))