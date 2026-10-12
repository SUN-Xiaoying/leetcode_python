# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return True

class Solution:
    # Your runtime beats 81.81 % of python3 submissions.
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        mid = (left + right) // 2
        # mid = left + (right - left) // 2
        # Your runtime beats 97.43 % of python3 submissions.
        while left < right :
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1 # Forgot +1 Timeout
            mid = (left + right) // 2

        return mid

