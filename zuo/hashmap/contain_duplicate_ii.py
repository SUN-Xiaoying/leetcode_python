# https://leetcode.com/problems/contains-duplicate-ii/description/

from typing import List


class Solution:
    # 23ms Beats 94.65%
    # First Try: I'm so good
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_map = {}
        for i, num in enumerate(nums):
            if num in my_map and i - my_map[num] <= k:
                return True
            my_map[num] = i
        return False




s = Solution()
# false
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))
# True
print(s.containsNearbyDuplicate( [1,0,1,1], 1))
