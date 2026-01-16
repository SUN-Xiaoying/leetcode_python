# https://leetcode.com/problems/permutations/
# Med
from typing import List


class Solution:
    # 0 ms Beats 100.00%
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(i:int):
            if i==len(nums):
                ans.append(list(nums))
                return
            for j in range(i, len(nums), 1): # NOT i+1
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return ans


s = Solution()
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(s.permute([1,2,3]))
