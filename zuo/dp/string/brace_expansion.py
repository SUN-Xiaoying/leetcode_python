# https://neetcode.io/problems/brace-expansion/question
from typing import List


class Solution:
    # Memory: 8.4 MB Time: 0.029s
    def expand(self, s: str) -> List[str]:
        result=[]
        def backtrack(i:int, path:List[str]):
            if i == len(s):
                result.append("".join(path))
                return

            if s[i] == "{":
                i+=1
                options = []
                while s[i] != "}":
                    if s[i].isalpha():
                        options.append(s[i])
                    i+=1
                for opt in options:
                    path.append(opt)
                    backtrack(i+1, path)
                    path.pop()
            elif s[i].isalpha():
                path.append(s[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0,[])

        return result




s = Solution()
# ["acdf", "acef", "bcdf", "bcef"]
print(s.expand("{a,b}c{d,e}f"))






