from typing import List

# https://leetcode.com/problems/3sum/description/
class Solution:
    # duplicate
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = dict()
        for num in nums:
            if target-num in hashmap:
                return 
    
    # duplicate
    def threeSum_bruteforce(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        for i, v1 in enumerate(nums[:len(nums)-2]):
            for j, v2 in enumerate(nums[i+1:len(nums)-1]):
                for k, v3 in  enumerate(nums[j+1:]):
                    if v1 + v2 + v3 == 0: 
                        result.append([v1, v2, v3])

        return result
    

solution = Solution()
nums : List[int]= [-1,0,1,2,-1,-4]
results = solution.threeSum(nums)
for result in results:
    print(result)
    
