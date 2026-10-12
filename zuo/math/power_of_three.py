# https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/745/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Your runtime beats 13.96 % of python3 submissions.
        x=1
        i=0
        while x<n:
            if x==n: return True
            i+=1
            x=3**i

        return False

    # Your runtime beats 56.94 % of python3 submissions
    def isPowerOfThree_holy(self, n: int) -> bool:
        mx = 3**19
        return n>0 and mx%n==0