class Solution:
    def add(self, a:int, b:int)->int:
        ans = a
        while b != 0:
            ans = (a ^ b) & 0xFFFFFFFF
            b = (( a & b ) << 1) & 0xFFFFFFFF # 进位
            a = ans
        # convert to signed
        return a if a < 0x80000000 else a - 0x100000000

    def neg(self, x:int)->int:
        return self.add(~x, 1)

    def minus(self, a:int, b:int)->int:
        return self.add(a, self.neg(b))

    # def multiple(self, a:int, b:int) -> int:


s = Solution()
a=14
b=11
print(s.add(a,b))
print(s.neg(b))
print(s.minus(a,b))