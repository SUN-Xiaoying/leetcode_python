# https://leetcode.com/problems/house-robber-ii/description/
from typing import List


class Solution:
    # 只有两种可能性，包括nums【0】和不包括nums【0】
    # 0 ms Beats 100.00%
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2: return max(nums)
        n=len(nums)
        def best(l:int, r:int)->int:
            if l>r: return 0
            if l==r: return nums[l]
            if l+1 == r: return max(nums[l], nums[r])

            prepre = nums[l]
            pre = max(nums[l], nums[l+1])

            for i in range(l+2, r+1): # Careful, not l+2 ~ r
                cur = max(nums[i]+prepre, pre)
                prepre = pre
                pre = cur

            return pre

        return max(nums[0]+best(2,n-2), best(1,n-1))



    # 知识迁移是很稀缺的能力
    def rob_wrong(self, nums: List[int]) -> int:
        if len(nums)<=2: return max(nums)
        n = len(nums)
        dp_max = [0]*n
        dp_min = [0]*n

        dp_min[0], dp_min[1] = nums[0], min(nums[0], nums[1])
        dp_max[0], dp_max[1] = nums[0], max(nums[0], nums[1])

        max_sum, min_sum = dp_min[1], dp_max[1]
        all_sum = nums[0] + nums[1]

        for i in range(2, n):
            all_sum += nums[i]
            dp_min[i] = min(dp_min[i-1], nums[i]+dp_min[i-2])
            min_sum = min(min_sum, dp_min[i])
            print("min_sum: ", min_sum)

            dp_max[i] = max(dp_max[i-1], nums[i]+dp_max[i-2])
            max_sum = max(max_sum, dp_max[i])
            print("max_sum: ", max_sum)

        return max(all_sum - min_sum, max_sum) # 错了，不可以all_sum只能跳家打劫

s =Solution()
# 3
print(s.rob([2,3,2]))
# 4
print(s.rob([1,2,3,1]))