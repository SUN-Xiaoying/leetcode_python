from typing import List

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, num in enumerate(numbers):
            if target-num in hashmap:
                return [hashmap[target-num], index+1]
            hashmap[num] = index+1

        return [-1, -1]