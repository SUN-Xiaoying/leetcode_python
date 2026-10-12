# https://leetcode.com/problems/heaters/
from typing import List


class Solution:
    # 39 ms Beats 63.88%
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        j, ans = 0, 0
        def is_best(a:int, b:int) -> bool:
            return b==len(heaters)-1 or abs(a-heaters[b]) < abs(a-heaters[b+1])
        # Why you use enumerate?
        for i in houses:
            while not is_best(i,j):
                j+=1
            ans = max(ans, abs(i - heaters[j]))

        return ans

    # 39ms Beats 63.88%
    def findRadius1(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        j, ans = 0, 0
        def is_best(a:int, b:int) -> bool:
            return b==len(heaters)-1 or abs(houses[a]-heaters[b]) < abs(houses[a]-heaters[b+1])
        # Why you use enumerate?
        for i, house in enumerate(houses):
            while not is_best(i,j):
                j+=1
            ans = max(ans, abs(houses[i] - heaters[j]))

        return ans

s = Solution()
# 3
print(s.findRadius([1,5],[2]))
# 1
print(s.findRadius([1,2,3,4], [1,4]))