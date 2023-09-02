
class Solution:

    def traverseSubArray(self, nums: list, flag=0) -> int:
        n = len(nums)
        if n == 0:
            return nums
        if n == 1:
            if nums[0] > self.maxSub:
                self.maxSub = nums[0]
                self.maxSubArr = nums
            return nums
        mid = n // 2

        left = self.traverseSubArray(nums[:mid])
        right = self.traverseSubArray(nums[mid:])
        sum_left = sum(left)
        sum_right = sum(right)
        print(left, right)
        if sum_left < 0:
            if sum_right > self.maxSub:
                self.maxSub = sum_right
                self.maxSubArr = right
            return right
        else:
            sum_left_right = sum_left + sum_right
            left_right = left + right
            print("!!!")
            if sum_left_right > self.maxSub:
                print("@@@@", self.maxSub, self.maxSubArr, left_right)
                self.maxSub = sum_left_right
                self.maxSubArr = left_right
            return left_right

    def maxSubArray(self, nums: list[int]) -> int:
        self.maxSub = -0x80000000
        self.maxSubArr = []
        self.traverseSubArray(nums)
        return self.maxSubArr
    
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))