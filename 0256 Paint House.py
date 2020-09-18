# 递归
# def minCost(costs):
#     # Calculate minimum total cost since n house
#     def paint_cost(n, color):
#         total_cost = costs[n][color]
        
#         # 最后一层不操作
#         if n == len(costs) - 1:
#             pass
        
#         elif color == 0: # Red
#             total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
#         elif color == 1: # Green
#             total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
#         else: # Blue
#             total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            
#         return total_cost

#     if costs == []:
#         return 0
    
#     return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))


# 动态规划
def minCost(costs):
    #  returns a reversed iterator object.
    for n in reversed(range(len(costs) - 1)):
        # Total cost of painting nth house red.
        costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])
        # Total cost of painting nth house green.
        costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])
        # Total cost of painting nth house blue.
        costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])
    
    if len(costs) == 0:
        return 0
    
    return min(costs[0]) # Return the minimum in the first row


print(minCost([[17,2,17],[16,16,5],[14,3,19]]))