# https://leetcode.com/problems/power-of-two/description/

class Solution:
    # 0 ms Beats 100.00%
    def isPowerOfTwo(self, n: int) -> bool:
        # 二进制，只有一位是 1
        # 提取最右侧的 1
        return n>0 and n == (n & -n)