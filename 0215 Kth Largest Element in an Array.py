class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def merge_sort(alist):
            n = len(alist)
            if n <= 1:
                return alist
            mid = n//2
            left = merge_sort(alist[:mid])
            right = merge_sort(alist[mid:])

            left_point,right_point = 0,0
            result = []
            while left_point < len(left) and right_point < len(right):
                if left[left_point] <= right[right_point]:
                    result.append(left[left_point])
                    left_point += 1
                else:
                    result.append(right[right_point])
                    right_point += 1

            result += left[left_point:]
            result += right[right_point:]
            return result
        result = merge_sort(nums)
        return result[-k]