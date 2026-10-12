# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
import random
from typing import List


class Solution:
    # 99ms Beats 36.78%
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quicksort(left: int, right: int) -> int:
            if left >= right: return nums[left]
            key = len(nums)-k

            x = left + int(random.random() * (right - left +1))
            a, b = partition(left, right, nums[x])

            if a <= key <= b:
                return nums[key]
            elif key < a:
                return quicksort(left, a-1)
            else:
                return quicksort(b+1, right)

        def partition(left: int, right: int, x:int):
            a, b, i = left, right, left
            while i<=b:
                if nums[i] < x:
                    nums[a], nums[i] = nums[i], nums[a]
                    a+=1
                    i+=1
                elif nums[i] == x:
                    i+=1
                else:
                    nums[b], nums[i]=nums[i], nums[b]
                    b-=1
            return a, b

        return quicksort(0, len(nums)-1)

s= Solution()
# 4
# print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
# 5
print(s.findKthLargest([3,2,1,5,6,4], 2))