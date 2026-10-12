# https://leetcode.com/problems/sort-array-by-parity-ii/description/
from typing import List


class Solution:

    # TODO: Best Solution, 对的就不换
    # while even_index < length and odd_index < length:
    #     if nums[even_index] % 2 == 0:
    #         even_index += 2
    #     elif nums[odd_index] % 2 == 1:
    #         odd_index += 2
    #     else:
    #         nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]

    # 7ms Beats 68.67%
    # Wow Easy不在话下
    def sortArrayByParityII_mine(self, nums: List[int]) -> List[int]:

        even, odd = 0,1
        len_nums = len(nums)

        while even<len_nums and odd<len_nums:
            if nums[-1] % 2 ==0:
                nums[even], nums[-1] = nums[-1], nums[even]
                even+=2
            else:
                nums[odd], nums[-1] = nums[-1], nums[odd]
                odd += 2

        return nums

s = Solution()
# [4,5,2,7]
print(s.sortArrayByParityII([4,2,5,7]))