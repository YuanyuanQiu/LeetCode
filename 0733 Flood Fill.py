def floodFill(image, sr, sc, newColor):
    row = len(image)
    col = len(image[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    origin = set()
    filled = {(sr,sc)}
    old_color = image[sr][sc]
    image[sr][sc] = newColor

    for i in range(row):
        for j in range(col):
            if image[i][j] == old_color:
                origin.add((i,j))
    
    while origin:
        if not filled:
            return image
        temp = set()
        for i,j in filled:
            for di,dj in directions:
                if (i+di,j+dj) in origin:
                    temp.add((i+di,j+dj))
                    image[i+di][j+dj] = newColor
        filled = temp
        origin -= filled
    
    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))