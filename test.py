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

def find_duplicates(data):
    duplicates = []
    data_set = set()
    for num in data:
        if num in data_set:
            duplicates.append(num)
        else:
            data_set.add(num)
    return duplicates


class MyArray:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, indices):
        print(type(indices))
        print(indices)
        if isinstance(indices, tuple) and len(indices) == 2:
            row_indices, col_indices = indices
            if isinstance(row_indices, slice) and isinstance(col_indices, slice):
                # Extract start, stop, and step from slice objects
                row_start, row_stop, row_step = row_indices.indices(len(self.data))
                col_start, col_stop, col_step = col_indices.indices(len(self.data[0]))
                # Use built-in list slicing to get a 2D sub-array
                return [row[col_start:col_stop:col_step] for row in self.data[row_start:row_stop:row_step]]

        else:
            raise IndexError('Invalid index')

def waterContainer(walls: list) -> list:
    indices = list(range(0, len(walls)))
    
    walls_order = sorted(indices, key=lambda x: walls[x], reverse=True)
    waters = [-1] * (len(walls) - 1)
    remaining = len(walls)
    
    for i in range(1, len(walls_order)):
        a = walls_order[i - 1]
        b = walls_order[i]
        start = min(a, b)
        stop = max(a, b)
        for j in range(start, stop):
            if waters[j] == -1:
                waters[j] = walls[b]
                remaining -= 1
                
    for i in range(len(waters)):
        if waters[i] == -1:
            waters[i] = 0
    
    return waters

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # Into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def _decorator(f):
    
    def w(*arg, **kwargs):
        print("Start decorator")
        result = f(*arg, **kwargs)
        print("End decorator")
        return result
    
    return w

@_decorator
def greet():
    print("Hello")

if __name__ == '__main__':
    greet()