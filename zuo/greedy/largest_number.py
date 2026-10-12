# https://leetcode.com/problems/largest-number/
from functools import cmp_to_key
from typing import List


class Solution:

    # 3 ms Beats 53.71%
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b) -> int:
            if str(a) + str(b) > str(b) + str(a):
                return -1
            return 1
        nums.sort(key=cmp_to_key(compare))
        result = "".join(str(num) for num in nums)
        return "0" if nums[0] == 0 else result


    # 35ms Beats 5.89%
    def largestNumber_two_loop(self, nums: List[int]) -> str:
        for _ in range(len(nums)):
            for i in range(len(nums) - 1):
                str1 = str(nums[i])
                str2 = str(nums[i + 1])
                if str2 + str1 > str1 + str2:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        result = ""
        for num in nums:
            result += str(num)
        return "0" if nums[0] == 0 else result

s = Solution()
print(s.largestNumber([3,30,34,5,9]))