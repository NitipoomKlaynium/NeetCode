import re

class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1) :
            if (nums[i] == nums[i + 1]) :
                return True
        return False
    
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)) :
            if (nums[i] <= target) :
                for j in range(i + 1, len(nums)) :
                    print(nums[i], nums[j])
                    if (nums[i] + nums[j] == target) :
                        return [i, j]
                    
    def isPalindrome(s: str) -> bool:
        return s == s[::-1]
    
def isValid(s: str) -> bool:
    def check(l: str, r: str) :
        return (l == "(" and r == ")") or (l == "{" and r == "}") or (l == "[" and r == "]")
        
    stack = ""
    for i in range(len(s)) :
        print(stack)
        if stack == "" and s[i] in ")}]" :
            return False
        elif (s[i] in "({[") :
            stack += s[i]
        elif check(stack[-1], s[i]) :
            stack = stack[:-1]
        else :
            return False
    if stack != "" :
        return False
    return True

# def binarySearch(nums: list[int], target: int, left_count = 0) -> int:
#     center = len(nums) // 2

#     if nums[center] == target :
#         return center + left_count
#     elif len(nums) == 1 :
#         return -1
#     elif nums[center] > target :
#         temp = binarySearch(nums[:center], target, 0)
#         return -1 if temp == -1 else temp + left_count
#     else :
#         temp = binarySearch(nums[center:], target, left_count = center)  
#         return -1 if temp == -1 else temp + left_count

def search(nums: list[int], target: int) -> int:
    center = len(nums) // 2
    left_count = 0
    
    while nums[center] != target :
        if (len(nums) == 1) :
            return -1
        elif nums[center] > target :
            nums = nums[:center]
        else :
            nums = nums[center:]
            left_count += center
        center = len(nums) // 2
        
    return center + left_count

if __name__ == "__main__" :
    print(search([-1,0,3,5,9,12], 9))