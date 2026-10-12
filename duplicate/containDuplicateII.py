# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    # 43 ms Beats 89.73%
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        mapping = {}
        for index, value in enumerate(nums):
            if value not in mapping:
                mapping[value] = index
            else:
                if abs(mapping[value] - index) <= k:
                    return True
                else:
                    mapping[value] = index
        return False

s= Solution()
# true
print(s.containsNearbyDuplicate([1,0,1,1], 1))
# false
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))