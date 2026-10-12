# https://leetcode.com/problems/third-maximum-number/description/
import random
from typing import List


class Solution:

    # Greedy
    # 0ms Beats 100.00%
    def thirdMax(self, nums: List[int]) -> int:
        first, second, third = None, None, None
        nums = list(set(nums))
        for num in nums:
            if first is None or num>first:
                first, second, third = num, first, second
            elif second is None or num>second:
                second, third = num, second
            elif third is None or num > third:
                third = num
            else:
                continue

        return third if third is not None else first


    # 23ms Beats 5.02%
    def thirdMax_mine(self, nums: List[int]) -> int:

        def quciksort(left: int, right: int):
            if left >= right: return
            x = left + int(random.random() *(right - left + 1)) # Mistake int()

            a, b = partition(left, right, nums[x])

            quciksort(left, a-1)
            quciksort(b+1, right)

        def partition(left:int, right:int, x:int):
            a = left
            b = right
            i = left
            while i<=b: # Mistake
                if nums[i]<x:
                    nums[a], nums[i]= nums[i], nums[a]
                    a+=1
                    i+=1
                elif nums[i] == x:
                    i+=1
                else:
                    nums[b], nums[i] = nums[i], nums[b]
                    b-=1

            return a, b

        quciksort(0, len(nums)-1)
        return nums[-3] if len(nums) >= 3 else nums[-1] # Mistake if len(nums)>=3


s = Solution()
print(s.thirdMax([2,2,3,1]))

