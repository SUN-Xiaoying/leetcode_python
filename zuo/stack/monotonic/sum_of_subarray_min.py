# https://leetcode.com/problems/sum-of-subarray-minimums/description/
# Hard
# 不可能用枚举，太慢了
from typing import List


class Solution:

    # 55ms Beats 91.07%
    def sumSubarrayMins_allInOne(self, arr: List[int]) -> int:
        result = 0
        stack = []
        MOD = 10 ** 9 + 7
        n = len(arr)

        for i in range(n + 1):
            # Treat arr[n] as -∞ to flush the stack
            cur_val = arr[i] if i < n else -1
            while stack and arr[stack[-1]] >= cur_val:
                cur = stack.pop()
                left = stack[-1] if stack else -1
                count = (cur - left) * (i - cur)
                result = (result + arr[cur] * count) % MOD
            stack.append(i)

        return result



    # 80 / 88 testcases passed, result%=MOD
    # 59ms Beats 84.60%
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = 0
        stack = []
        MOD = 10**9+7
        # iter
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                cur = stack.pop()
                left = stack[-1] if stack else -1
                result += ((cur-left)*(i-cur)*arr[cur]) % MOD
                result%=MOD

            stack.append(i)

        # clear
        while stack:
            cur = stack.pop()
            left = stack[-1] if stack else -1
            result += ((cur-left)*(len(arr)-cur)*arr[cur]) % MOD # result = (result + arr[cur] * count) % MOD
            result %= MOD

        return result


    def sumSubarrayMins_wrong(self, arr: List[int]) -> int:
        result=0

        stack=[]
        min_num = float('inf')

        for item in arr:
            if not stack:
                stack.append(item)
                min_num = min(min_num, item)
            elif item >= stack[-1]:
                result += min_num
                stack.append(item)
            else:
                result += stack.pop()
                result += stack[-1] if stack else 0
                min_num = min(min_num, item)
                result += min_num
                stack.append(item)

        result+=min_num
        while stack:
            result += stack.pop()
            result += stack[-1] if stack else 0

        return result%( 10**9 + 7)

if __name__ == '__main__':
    s = Solution()
    # 17
    print(s.sumSubarrayMins([3,1,2,4]))
    # 444
    print(s.sumSubarrayMins([11,81,94,43,3]))
