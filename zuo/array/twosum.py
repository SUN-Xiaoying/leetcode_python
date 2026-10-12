# https://leetcode.com/problems/two-sum/description/

from typing import List


class Solution:
    # HashMap (val: index)
    # 0ms Beats 100.00%
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, num in enumerate(nums):
            if target-num in hashmap:
                return [hashmap[target-num], index]
            hashmap[num]= index
        



    # 1969ms Beats 9.37%
    # O(n^2)
    def twoSum_bruteForce(self, nums: List[int], target: int) -> List[int]:
        i =0
        while i<len(nums)-1:
            for j, num in enumerate(nums[i+1:]) :
                if nums[i]+num==target : 
                    return [i, i+j+1]
            i+=1

        return [-1, -1]


solution = Solution()
nums : List[int]= [3,2,4]
target = 6
print(solution.twoSum(nums, target))