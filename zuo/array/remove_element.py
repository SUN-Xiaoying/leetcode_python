# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150


# Runtime 0ms Beats 100.00%
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

solution = Solution()
nums = [3, 2, 2, 3]
val = 3
print(solution.removeElement(nums, val))
