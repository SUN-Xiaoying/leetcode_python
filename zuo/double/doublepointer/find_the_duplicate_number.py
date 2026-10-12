# https://leetcode.com/problems/find-the-duplicate-number/description/
from typing import List


class Solution:
    # 21ms Beats 85.45%
    def findDuplicate_slow_fast(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


    # TODO: not the best solution
    # 用 Array TLE， 必须用set
    # 42ms Beats 23.37%
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        i = 0

        while nums[i] not in seen:
            seen.add(nums[i])
            i=nums[i]
        return nums[i]


s = Solution()
# 3
print(s.findDuplicate_slow_fast([3,1,3,4,2]))
# 3
print(s.findDuplicate_slow_fast([3,3,3,3,3]))
