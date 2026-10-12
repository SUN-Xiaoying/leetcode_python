# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
from typing import List


class Solution:
    def moveZeroes_wrong(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2: return
        p_zero = 0
        p_num = 1
        while p_zero < len(nums) and p_num < len(nums):
            while nums[p_zero]!=0:
                p_zero += 1
                if p_zero == len(nums): return
            p_num = p_zero + 1
            while nums[p_num] == 0:
                p_num += 1
                if p_num == len(nums): return

            nums[p_zero] = nums[p_num]
            nums[p_num] = 0
            p_zero += 1

def moveZeroes_fixed(nums: List[int]) -> None:
    if len(nums) < 2:
        return

    p_zero = 0
    p_num = 1

    while p_num < len(nums):
        # Move p_zero to the first 0
        while p_zero < len(nums) and nums[p_zero] != 0:
            p_zero += 1

        # Make sure p_num is always ahead of p_zero
        p_num = max(p_num, p_zero + 1)

        # Move p_num to the next non-zero
        while p_num < len(nums) and nums[p_num] == 0:
            p_num += 1

        # If both are valid, swap
        if p_zero < len(nums) and p_num < len(nums):
            nums[p_zero], nums[p_num] = nums[p_num], nums[p_zero]
            p_zero += 1

    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0

        # Move all non-zero elements to the front
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # Fill the rest with zeros
        for i in range(insert_pos, len(nums)):
            nums[i] = 0

if __name__ == "__main__":
    sol = Solution()
    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    print(nums1)
    nums2 = [0, 1]
    sol.moveZeroes(nums2)
    print(nums2)