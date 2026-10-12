# https://leetcode.com/problems/contains-duplicate/description/
# Easy

class Solution:
    # 45 ms Beats 11.69%
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        last_num = nums[0]
        for num in nums[1:]:
            if num == last_num:
                return True
            last_num = num
        return False


s = Solution()
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(s.containsDuplicate([1,2,3,4]))