# https://leetcode.com/problems/single-number/
from typing import List


class Solution:
    # 0 ms Beats 100.00%

    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        return result