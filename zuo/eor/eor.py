
class Solution:
    def flip(self, n: int):
        return n ^ 1

    # non-negative == 1
    # negative == 0
    def sign(self, n: int):
        if n & 0x80000000:  # cannot use return flip(n>>31)
            return 0
        return 1

    def get_max(self, a: int, b: int) -> int:
        c = (a - b) & 0xFFFFFFFF
        sign_a = self.sign(a)
        sign_b = self.sign(b)
        diff_ab = sign_a ^ sign_b
        return_a = diff_ab * sign_a + self.flip(diff_ab) * self.sign(c)

        return a * return_a + b * self.flip(return_a)

s = Solution()
print(s.get_max(-1, -2))
print(s.get_max(1, -2))