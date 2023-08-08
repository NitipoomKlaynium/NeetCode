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
    print(search([2, 3, 5, 6, 7, 12, 44, 56, 57], 12))