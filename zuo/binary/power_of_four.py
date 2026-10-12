# https://leetcode.com/problems/power-of-four/description/



class Solution:
    # 0 ms Beats 100.00%
    def isPowerOfFour(self, n: int) -> bool:
        mx = 1073741824
        return n>0 and mx%n == 0 and (n & 0x55555555) != 0