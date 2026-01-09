from typing import List


class Solution:
    def allSubString(self, s: str) -> List[str]:
        result = set()
        path = ""

        def dfs(s: str, i: int) :
            nonlocal path
            if i >= len(s) :
                result.add(path)
            else:
                path += s[i]
                dfs(s, i + 1)
                path = path[:-1]
                dfs(s, i + 1)

        dfs(s, 0)


        return list(result)


s = Solution()
print(s.allSubString("abbc"))