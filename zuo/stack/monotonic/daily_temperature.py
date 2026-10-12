# https://leetcode.com/problems/daily-temperatures/description/
# Middle
from typing import List

class Solution:
    # Your solution Beats 60.11%
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]]= i - stack[-1]
                stack.pop()
            stack.append(i)

        return ans

    def dailyTemperatures_mine(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        count = 0

        # 遍历
        for i in range(n):
            if count==0 or temperatures[i] < temperatures[stack[count-1]]:
                stack.append(i)
                count+=1
            elif temperatures[stack[count-1]] == temperatures[i]:
                count-=1
                ans[stack[count]] = -i
                stack.pop()
                stack.append(i)
            else:
                count -= 1
                ans[stack[count]] = i - stack[count] if count >= 0 else 0
                stack.pop()
                stack.append(i)
                count+=1
        # 清算
        while count>0:
            count-=1
            ans[stack[count]]=0

        # # 验证
        for i in range(len(temperatures)-2, 0, -1):
            if ans[i] < 0:
                ans[i] = ans[-ans[i]] -ans[i] -i

        return ans


if __name__ == '__main__':
    s = Solution()
    # Ans [1,1,4,2,1,1,0,0]
    # Mine [0, 1, 0, 3, 0, 5, 0, 7]
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
