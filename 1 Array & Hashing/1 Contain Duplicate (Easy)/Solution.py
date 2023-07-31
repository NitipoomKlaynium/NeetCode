import re

def containsDuplicate(nums: list[int]) -> bool:
    nums.sort()
    for i in range(len(nums) - 1) :
        if (nums[i] == nums[i + 1]) :
            return True
    return False

if __name__ == "__main__" :
    print(containsDuplicate([1, 2, 3, 4]))