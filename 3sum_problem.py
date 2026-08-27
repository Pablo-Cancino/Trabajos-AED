#se tiene una lista de numeros enteros, en donde el sistema devuelve todos los grupos de 3 que suman 0.
#input arreglo de Z
#entrega combinaciones que dan 0
"""
def three_sum(numbers: list[int]):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            for k in range(j+1,len(numbers)):
                if (numbers[i] + numbers[j] + numbers[k] == 0):
                    print (f"[{numbers[i]},{numbers[j]},{numbers[k]}]")
        
#numbers_input = [0, -2, 4, 2, -6, -1] --> desordenado
numbers_input = [-6, -2, -1, 0, 2, 4]
three_sum(numbers_input)
"""

def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()  # Step 1: Sort the array
    
    for i in range(len(nums) - 2):
        # Early termination optimization
        if nums[i] > 0:
            break
            
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        # Two-pointer initialization
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                
                # Move pointers and skip duplicates to avoid identical triplets
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
            elif total < 0:
                left += 1  # Need a larger sum
            else:
                right -= 1  # Need a smaller sum
                
    return res
