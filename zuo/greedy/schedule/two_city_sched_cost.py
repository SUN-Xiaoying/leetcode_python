# https://leetcode.com/problems/two-city-scheduling/description/
from typing import List


class Solution:
    # 0 ms Beats 100.00%
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sum = 0
        arr = []
        for cost in costs:
            arr.append(cost[1]- cost[0])
            sum += cost[0]
        arr.sort()
        for i in range(len(costs)/2):
            sum += arr[i]
        return sum