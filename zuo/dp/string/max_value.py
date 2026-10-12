from typing import List

class Solution:

    def maxValue(self, arr: List[int]) -> int:
        def f(l: int, r: int) -> int:
            if l == r:
                return arr[l]
            m = (l + r) // 2
            return max(f(l, m), f(l + 1, r))

        return f(0, len(arr)-1)

s = Solution()
print(s.maxValue([4, 2, -1, 6, 0]))
