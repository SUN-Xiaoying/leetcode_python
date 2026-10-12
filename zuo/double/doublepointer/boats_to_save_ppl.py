# https://leetcode.com/problems/boats-to-save-people/
# Mid
from typing import List

class Solution:
    # 43ms Beats 88.74%
    # 20251011 挺好的感觉境界提升了
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people)-1
        people.sort()
        result = 0
        while l<=r:
            if people[l]+people[r]>limit:
                result+=1
                r-=1
            else:
                result+=1
                l+=1
                r-=1
        return result

    # Best Solution
    # while l<r: ...
    # if l==r:
    #     rere+=1
    # 省掉一种必然比较


s = Solution()
# 3
print(s.numRescueBoats([3,2,2,1], 3))
# Output: 4
print(s.numRescueBoats([3,5,3,4], 5))