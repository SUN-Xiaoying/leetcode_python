# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

from typing import List


class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        result: List[int] = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1

        return result




nums1: List[int] = [4, 9, 5]
nums2: List[int] = [9, 4, 9, 8, 4]
solution = Solution()
result = solution.intersect(nums1, nums2)
for num in result:
    print(num)