# https://leetcode.com/problems/subsets-ii/description/
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
            temp.pop()
            last = temp[-1]
            dfs(i+1)

        dfs(0)

        return list(result)

s = Solution()
print(s.subsetsWithDup([1,2,2]))