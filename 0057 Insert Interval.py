def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if not intervals:
        return [newInterval]
    if not newInterval:
        return intervals
    
    for i in range(len(intervals)):
        if newInterval[0] < intervals[i][0]:
            intervals.insert(i,newInterval)
            break
    else:
        intervals.append(newInterval)
    
    mreged = []
    for i in intervals:
        if not mreged or mreged[-1][1] < i[0]:
            mreged.append(i)
        else:
            mreged[-1][1] = max(i[1], mreged[-1][1])
    return mreged