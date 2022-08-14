def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    t = TreeNode()
    if not nums:
        return None
    mid = len(nums)//2
    t.val = nums[mid]
    t.left = self.sortedArrayToBST(nums[:mid])
    t.right = self.sortedArrayToBST(nums[mid+1:])
    return t