def containsDuplicate(nums):
    if len(set(nums))==len(nums):
        return False
    else:
        return True
    
print(containsDuplicate([3,1]))