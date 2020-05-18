def findDisappearedNumbers(nums):
    hash_table = {}
    for num in nums:
        hash_table[num] = 1
    if nums == []:
        return nums
    length = len(nums)
    ls = []
    for i in range(1, length+1):
        if i not in hash_table:
            ls.append(i)
    return ls

def findDisappearedNumbers(nums):
    
    # Iterate over each of the elements in the original array
    for i in range(len(nums)):
        
        # Treat the value as the new index
        new_index = abs(nums[i]) - 1
        
        # Check the magnitude of value at this new index
        # If the magnitude is positive, make it negative 
        # thus indicating that the number nums[i] has 
        # appeared or has been visited.
        if nums[new_index] > 0:
            nums[new_index] *= -1
    
    # Response array that would contain the missing numbers
    result = []    
    
    # Iterate over the numbers from 1 to N and add all those
    # that have positive magnitude in the array 
    for i in range(1, len(nums) + 1):
        if nums[i - 1] > 0:
            result.append(i)
            
    return result    

print(findDisappearedNumbers([1,1]))