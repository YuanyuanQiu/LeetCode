def findMinArrowShots(self, points: List[List[int]]) -> int:
    points = sorted(points, key=lambda x: x[0])
    # list of overlapping [start, end]
    ls = []
    for point in points:
        if not ls or ls[-1][1] < point[0]:
            ls.append(point)
        else:
            # start
            ls[-1][0] = max(ls[-1][0], point[0])
            # end
            ls[-1][1] = min(ls[-1][1], point[1])
    return len(ls)