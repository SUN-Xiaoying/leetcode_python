# https://leetcode.com/problems/contains-duplicate-iii/description/
# Hard
# Sliding Window
# Sorted List???: https://www.youtube.com/watch?v=klCY3k70A50

class Solution:
    # Time Limit Exceeded
    # 38 / 58 testcases passed
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        mapping = {}
        for i,v in enumerate(nums):
            if mapping:
                for key, value in list(mapping.items()):
                    if i - key <= indexDiff and abs(v - value) <= valueDiff:
                        return True
                    if i - key > indexDiff:
                        mapping.pop(key)
            mapping[i]=v
        return False

    def containsNearbyAlmostDuplicate_mine(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        tail = 0
        head = 1
        diff = 0

        while head < len(nums):
            while head < len(nums) and head - tail <= indexDiff:
                if diff <= valueDiff:
                    return True
                maxValue = max(maxValue, nums[head])
                minValue = min(minValue, nums[head])
                head +=1
            if head - tail == len(nums) and diff<= valueDiff:
                return True
            removed = nums[tail]
            tail += 1
            if removed == maxValue:
                maxValue = max(nums[tail:head])
            if removed == minValue:
                minValue = min(nums[tail:head])

        return False

s = Solution()
# False
print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2,3))
# True
print(s.containsNearbyAlmostDuplicate([1,2,3,1], 3,0))
# False
print(s.containsNearbyAlmostDuplicate([-3,3], 2,4))
# True; indexDiff > len(nums)
print(s.containsNearbyAlmostDuplicate([4,1,6,3], 4,1))


            