# https://leetcode.com/problems/permutations-ii/description/
# Med
from typing import List


class Solution:

    # 7 ms Beats 51.61%
    # 空间换时间
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        '''
            my_set = set()
            my_set is shared across all recursion levels,
            once a value is used at any level, it is blocked everywhere
        '''
        def backtrack(i:int):
            if i == len(nums):
                result.append(nums.copy())
                return

            my_set = set()  # <-- move here

            for j in range(i, len(nums)):
                if nums[j] not in my_set:
                    my_set.add(nums[j])
                    nums[i], nums[j] = nums[j], nums[i]
                    backtrack(i + 1)
                    nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return result


    # 97 ms Beats 16.21%
    # 直接扔集合，表现并不是特别好
    def permuteUnique_set(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def backtrack(i:int):
            if i == len(nums):
                result.add(tuple(nums))
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return list(result)



s = Solution()
'''
[[1,1,2],
 [1,2,1],
 [2,1,1]]
'''
print(s.permuteUnique([1,1,2]))



