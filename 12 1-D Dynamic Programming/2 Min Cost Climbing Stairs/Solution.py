class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        
        temp = [-1] * len(cost)
        def minCost(_cost, _temp=[]):
            n = len(_cost) - 1
            if n < 1:
                return 0
            else:
                if _temp[n] == -1:
                    a = minCost(_cost[:-1], _temp)
                    b = minCost(_cost[:-2], _temp)
                    temp[n] = min(_cost[-1] + a, _cost[-2] + b)
                    return _temp[n]
                else:
                    return _temp[n]

        return minCost(cost, temp)