# https://leetcode.com/problems/reverse-pairs/description/
# Hard
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 754ms Beats 74.83%
        def mergesort(left: int, right: int) -> int:
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = mergesort(left, mid) + mergesort(mid + 1, right)

            # Count
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            temp.extend(nums[i:mid + 1])
            temp.extend(nums[j:right + 1])
            nums[left:right + 1] = temp
            return count

        return mergesort(0, len(nums) - 1)


    # 949ms Beats 34.21%
    def reversePairs_zuo(self, nums: List[int]) -> int:
        def counts(left:int, right:int)->int:
            if left==right: return 0
            mid = (left+right) // 2
            return counts(left, mid) + counts(mid+1, right) + merge(left, mid, right)

        def merge(left:int, mid:int, right:int)->int:
            # count
            i, j = left, mid + 1
            ans =0
            while i<=mid:
                while j<=right and nums[i]>nums[j]*2:
                    j+=1
                ans += j-mid-1
                i+=1
            # merge
            a, b = left, mid+1
            result=[]
            while a<=mid and b<=right:
                if nums[a] <= nums[b]:
                    result.append(nums[a])
                    a+=1
                else:
                    result.append(nums[b])
                    b+=1
            result.extend(nums[a:mid+1])
            result.extend(nums[b:right+1])
            # There is a simple way
            # nums[left:right+1] = result
            for i in range(left, right+1):
                nums[i]=result[i-left]
            return ans

        return counts(0, len(nums)-1)

s = Solution()
#3
print(s.reversePairs([2,4,3,5,1]))