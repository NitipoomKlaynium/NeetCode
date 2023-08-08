def twoSum(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)) :
            if (nums[i] <= target) :
                for j in range(i + 1, len(nums)) :
                    print(nums[i], nums[j])
                    if (nums[i] + nums[j] == target) :
                        return [i, j]
                    
if __name__ == "__main__" :
    print(twoSum([1, 2, 3, 4, 5, 6], 6))