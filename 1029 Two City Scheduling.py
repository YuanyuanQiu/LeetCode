# def twoCitySchedCost(costs):
#     n = len(costs)
    
#     gaps = []
#     for i in range(n):
#         gaps.append((i,abs(costs[i][0] - costs[i][1])))
    
#     def takeSecond(elem):
#         return elem[1]
    
#     gaps.sort(reverse=True,key=takeSecond)

#     a = []
#     b = []
#     while len(a) < n/2 and len(b) < n/2:
#         ind = gaps[0][0]
#         if costs[ind][0] <= costs[ind][1]:
#             a.append(costs[ind][0])
#         else:
#             b.append(costs[ind][1])
#         gaps = gaps[1:]
    
#     if len(a) > len(b):
#         for i in gaps:
#             ind = i[0]
#             b.append(costs[ind][1])
#     else:
#         for i in gaps:
#             ind = i[0]
#             b.append(costs[ind][0])
    
#     return sum(a)+sum(b)

#         # Sort by a gain which company has 
#         # by sending a person to city A and not to city B
#         costs.sort(key = lambda x : x[0] - x[1])


def twoCitySchedCost(costs):
    # Send all to city B
    # Sort by a gain which company has 
    # by sending a person to city A and not to city B
    costs.sort(key = lambda x : x[0] - x[1])
    
    total = 0
    n = len(costs) // 2
    # To optimize the company expenses,
    # send the first n persons to the city A
    # and the others to the city B
    for i in range(n):
        total += costs[i][0] + costs[i + n][1]
    return total

print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))