# https://leetcode.com/problems/missing-number/description/
from typing import List


class Solution:
    # 7ms Beats 35.78%
    def missingNumber(self, nums: List[int]) -> int:
        expect_res, actual_res =0, 0
        for i in range(len(nums)):
            expect_res = expect_res ^ i
            actual_res = actual_res ^ nums[i]

        expect_res = expect_res ^ len(nums)
        return expect_res ^ actual_res


s = Solution()
# 2
print(s.missingNumber([3, 4, 0, 1]))
