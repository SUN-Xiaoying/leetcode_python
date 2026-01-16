# https://leetcode.com/problems/subsets-ii/description/
from typing import List


class Solution:

    # 难道我是backtrack的天才吗？
    # 0ms Beats 100.00%
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # IMPORTANT
        result = set()

        def backtrack(i: int, path: list[int]):
            if i == len(nums):
                result.add(tuple(path))
                return

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            backtrack(i + 1, path)

        backtrack(0,[])

        return list(result)

    def subsetsWithDup_first(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        temp = []
        last = -1

        def dfs(i: int):
            nonlocal last
            if i == len(nums):
                result.add(tuple(temp))
                return
            while nums[i] == last and i < len(nums):
                i+=1

            temp.append(nums[i])
            last = temp[-1]
            dfs(i+1)
            temp.pop() # backtrack
            last = temp[-1]
            dfs(i+1)

        dfs(0)

        return list(result)

s = Solution()
print(s.subsetsWithDup([1,2,2]))