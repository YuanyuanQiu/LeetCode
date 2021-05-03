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


def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    left, right = newInterval
    placed = False
    ans = list()
    for li, ri in intervals:
        if li > right:
            # 在插入区间的右侧且无交集
            if not placed:
                ans.append([left, right])
                placed = True
            ans.append([li, ri])
        elif ri < left:
            # 在插入区间的左侧且无交集
            ans.append([li, ri])
        else:
            # 与插入区间有交集，计算它们的并集
            left = min(left, li)
            right = max(right, ri)
    
    if not placed:
        ans.append([left, right])
    return ans