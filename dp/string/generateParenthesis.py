# https://leetcode.com/problems/generate-parentheses/description/
# Med
from typing import List


class Solution:

    # TODO: Learn the ocndition
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(path: str):
            if len(path) == 2 * n:
                result.append(path)
                return

            open_used = path.count("(")
            close_used = path.count(")")

            if open_used < n:
                backtrack(path + "(")

            if close_used < open_used:
                backtrack(path + ")")

        backtrack("")
        return result

    # 4 ms Beats 13.87%
    # 你就说过没过吧？
    def generateParenthesis_mine(self, n: int) -> List[str]:
        result = set()
        limit = n*2

        def backtrack(i: int, path:str, rest_front: int, rest_back: int):
            if i == limit:
                result.add(path)
                return

            if rest_front == rest_back:
                path += "("
                rest_front -= 1
                backtrack(i+1, path, rest_front, rest_back)

            if rest_front > 0:
                path+= "("
                rest_front -= 1
                backtrack(i + 1, path, rest_front, rest_back)
                path = path[:-1]
                rest_front += 1
                path += ")"
                rest_back -= 1
                backtrack(i + 1, path, rest_front, rest_back)

            if rest_front == 0:
                path = path + ")" * (limit - len(path))
                result.add(path)
                return


        backtrack(1, "(", n-1, n)
        return list(result)




s = Solution()
# ["((()))","(()())","(())()","()(())","()()()"]
print(s.generateParenthesis(3))