# https://leetcode.com/problems/divide-two-integers/description/?envType=problem-list-v2&envId=bit-manipulation


class Solution:

    # 2ms Beats 22.89%
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  # handle overflow

        ans = 0
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            temp, multiple = divisor, 1
            '''
            The best solution: skip more iterations to 
            potentially reduce the number of loop cycles.
                while dividend >= (tmp_divisor << 2):
                    tmp_divisor <<= 2
                    tmp_mult <<= 2
            '''
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            ans += multiple

        return max(INT_MIN, min(INT_MAX, sign * ans))


    # 3ms Beats 18.74%
    # Python会自动进位，手动去余太痛苦了
    # Do not use & 0xFFFFFFFF if you want signed results.
    def divide_zuo(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  # handle overflow

        ans = 0
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        '''Iterates all 32 bits, even if the dividend is small.'''
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                ans |= (1 << i)
                dividend -= divisor << i
        return max(INT_MIN, min(INT_MAX, sign * ans))


s = Solution()
# 2147483647
print(s.divide(-2147483648, -1))
