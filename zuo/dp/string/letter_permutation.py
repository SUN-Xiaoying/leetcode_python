# https://leetcode.com/problems/letter-case-permutation/
# Med
from typing import List


class Solution:
    # 7 ms Beats 50.50%
    # No better than mine
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(i: int, path: List[str]):
            if i == len(s):
                result.append("".join(path))
                return

            if s[i].isdigit():
                path.append(s[i])
                backtrack(i+1, path)
                path.pop()
                """
                    You are making a choice.
                    Before trying a different choice, you must revert that change
                """
            else:
                path.append(s[i].lower())
                backtrack(i+1, path)
                path.pop()

                path.append(s[i].upper())
                backtrack(i+1, path)
                path.pop()

        backtrack(0,[])

        return result



    # How could this one be Med, it is pretty simple
    # Sacrifice space
    # 3ms Beats 88.89%
    def letterCasePermutation_mine(self, s: str) -> List[str]:
        result = []
        if s[0].isalpha():
            result.append(s[0].upper())
            result.append(s[0].lower())
        elif s[0].isdigit():
            result.append(s[0])
        for i in range(1, len(s)):
            temp=[]
            for path in result:
                if s[i].isalpha():
                    temp.append(path + s[i].upper())
                    temp.append(path + s[i].lower())
                elif s[i].isdigit():
                    temp.append(path+s[i])

            result = temp.copy()

        return result








s = Solution()
# ["a1b2","a1B2","A1b2","A1B2"]
print(s.letterCasePermutation("a1b2"))