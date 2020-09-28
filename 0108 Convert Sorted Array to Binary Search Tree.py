def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    left = 0
    right = len(nums) - 1
    
    # len = 0
    if left > right:
        return None
    
    mid = (left + right + 1) // 2
    root = TreeNode(nums[mid])
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid+1:])
    
    return root