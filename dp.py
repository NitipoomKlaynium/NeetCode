def binaryInsert(nums: list, n: int) -> None:
    left = 0
    right = len(nums) - 1
    if right == -1:
        nums = [n]
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == n:
            nums.insert(mid, n)
            return
        elif nums[mid] < n:
            left = mid + 1
        else:
            right = mid - 1

    nums.insert(left, n)

class Solution:
    def canPartition(self, nums: list) -> bool:
        sum_all = sum(nums)
        nums = sorted(nums)
        if sum_all & 1 == 1 or nums[-1] > sum_all:
            return False
        n = len(nums)

        i = 0
        while i < n:
            if nums.count(nums[i]) >= 4:
                temp = nums[i]
                del nums[i]
                del nums[i]
                binaryInsert(nums, temp << 1)
                n -= 1
            else:
                i += 1
        target = sum_all >> 1
        print(nums)
        subsets = [0]
        
        for n in nums:
            cur_len = len(subsets)
            for i in range(cur_len):
                subsets.append(subsets[i] + n)
                if subsets[-1] == target:
                    return True
        
        left = 1
        right = len(subsets) - 2

        return False
    
if __name__ == "__main__":
    solution = Solution()
    nums = [4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,12,12,12,12,12,12,12,12,16,16,16,16,16,16,16,16,20,20,20,20,20,20,20,20,24,24,24,24,24,24,24,24,28,28,28,28,28,28,28,28,32,32,32,32,32,32,32,32,36,36,36,36,36,36,36,36,40,40,40,40,40,40,40,40,44,44,44,44,44,44,44,44,48,48,48,48,48,48,48,48,52,52,52,52,52,52,52,52,56,56,56,56,56,56,56,56,60,60,60,60,60,60,60,60,64,64,64,64,64,64,64,64,68,68,68,68,68,68,68,68,72,72,72,72,72,72,72,72,76,76,76,76,76,76,76,76,80,80,80,80,80,80,80,80,84,84,84,84,84,84,84,84,88,88,88,88,88,88,88,88,92,92,92,92,92,92,92,92,96,96,96,96,96,96,96,96,97,99]
    print(solution.canPartition(nums))