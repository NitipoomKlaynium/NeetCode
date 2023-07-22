import re

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

def search(self, nums: list[int], target: int) -> int:
    center = len(nums) // 2

    if nums[center] == target :
        return center
    elif nums[center] < target :
        return search(nums[:center], target)
    else :
        return search(nums[center + 1:], target)
        
    
                    
if __name__ == "__main__" :
    print(isValid("]"))