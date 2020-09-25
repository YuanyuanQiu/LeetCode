def isRobotBounded(instructions):   
    pos = [0, 0] # current position
    d = [0, 1] # direction
    
    for i in instructions:
        if i == 'G':
            pos[0] += d[0]
            pos[1] += d[1]
        # (0,1),(-1,0),(0,-1),(1,0)
        elif i == 'L':
            d[0], d[1] = -d[1], d[0]
        # (0,1),(1,0),(0,-1),(-1,0)
        else:
            d[0], d[1] = d[1], -d[0]
    
    # 1）回到原地 或 2）方向变了（偏移量一致）
    return pos == [0, 0] or d != [0, 1]
