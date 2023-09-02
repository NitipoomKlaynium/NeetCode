class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = sorted(stones, reverse=True)
        while len(stones) > 1:
            if stones[0] > stones[1]:
                stones[0] = stones[0] - stones[1]
                del stones[1]
            elif stones[1] > stones[0]:
                stones[1] = stones[1] - stones[0]
                del stones[0]
            else:
                del stones[:2]
            stones = sorted(stones, reverse=True)
            print(stones)

        if stones:
            return stones[0]
        else:
            return 0