class Solution:
    def climbStairs(self, n: int) -> int:
        result = [1, 1, 2]
        if n < 3:
            return result[n]
        itr = 2
        for i in range(2, n):
            # print(itr, result, end=" -> ")
            if itr == 0:
                itr = 1
                result[1] = result[0] + result[2]
            elif itr == 1:
                itr = 2
                result[2] = result[0] + result[1]
            else:
                itr = 0
                result[0] = result[1] + result[2]
            # print(itr, result)

        return result[itr]
            