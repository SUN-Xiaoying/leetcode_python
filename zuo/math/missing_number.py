#
# https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/722/
from typing import List


class Solution:
    # Your runtime beats 26.19 % of python3 submissions.
    # Runtime (ms)D
    def missingNumber_mine(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)

    # 0 ms beats 100 %
    # Sum faster than Sort
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)

if __name__ == '__main__':
    solution = Solution()
    result = solution.missingNumber([9,6,4,2,3,5,7,0,1])
    print(result)
    result = solution.missingNumber([0,1])
    print(result)