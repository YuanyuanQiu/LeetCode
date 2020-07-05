# 若向内移动短板，水槽的短板可能变大，因此水槽面积 S(i, j)S(i,j) 可能增大。
# 若向内移动长板，水槽的短板不变或变小，下个水槽的面积一定小于当前水槽面积。
def maxArea(height):
    i, j, res = 0, len(height) - 1, 0
    while i < j:
        if height[i] < height[j]:
            res = max(res, height[i] * (j - i))
            i += 1
        else:
            res = max(res, height[j] * (j - i))
            j -= 1
    return res

print(maxArea([1,8,6,2,5,4,8,3,7]))