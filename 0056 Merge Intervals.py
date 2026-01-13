class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        # Sort based on start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If list is empty or current interval does not overlap with the previous, append it
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # Otherwise, there is overlap, so we merge strictly by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged