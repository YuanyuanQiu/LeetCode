import math

def findRadius(houses, heaters):
    # 排序整理
    houses.sort()
    heaters.append(float("inf")) # 保证最终index不会越界
    heaters.sort()
    # 逐步往前逼近
    max_dist = 0
    index = 0
    for house in houses:
        while (house >= heaters[index]): # 当house大于heater时向右侧移动
            index += 1
        if index > 0: # house夹在了index-1和index之间
            curr_dist = min(heaters[index] - house, house - heaters[index-1])
        else: # index-1不合法，只需要比较一个值
            curr_dist = abs(heaters[index] - house)
        max_dist = max(max_dist, curr_dist) # 更新当前最大值
            
    return max_dist

print(findRadius([1,2,3,4],[1,4]))
        