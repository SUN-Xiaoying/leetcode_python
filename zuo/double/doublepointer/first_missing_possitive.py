# https://leetcode.com/problems/first-missing-positive/description/
from typing import List


class Solution:
    # TODO: IndexError: list assignment index out of range
    def firstMissingPositive(self, nums: List[int]) -> int:
        l, r = 0, len(nums)

        while l < r:
            if nums[l] == l + 1:
                l += 1
            elif nums[l] <= l or nums[l] > r or  nums[nums[l] - 1] == nums[l]:
                r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            else:
                nums[l], nums[nums[l] - 1] = nums[nums[l] - 1], nums[l]

        return l + 1



s = Solution()
# 3
print(s.firstMissingPositive([1,2,0]))
# 2
print(s.firstMissingPositive([3,4,-1,1]))

print(s.firstMissingPositive([100000, 3, 4000, 2, 15, 1, 99999]))
