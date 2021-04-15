def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    # 如果起始点相同则返回0
    if source==target:
        return 0
    # 下面构建字典 key=route value=可跳转到的routes列表
    n = len(routes)
    routes = [set(r) for r in routes]
    routes_dic = defaultdict(list)
    for r1 in range(n):
        for r2 in range(n):
            if r2!=r1 and len(routes[r1].intersection(routes[r2]))>0:
                routes_dic[r1].append(r2)                         
    # 起点/终点变成经过source/target的所有车次
    source_routes = [r for r in range(n) if source in routes[r]]
    target_routes = set([r for r in range(n) if target in routes[r]])
    # 开始层序遍历
    que = source_routes
    len_que = len(que)
    buses = 1
    visited = set(source_routes)
    while que: 
        for _ in range(len_que):
            r = que.pop(0)
            if r in target_routes: return buses #print(buses)
            for neibor in routes_dic[r]:
                if neibor not in visited:
                    que.append(neibor)
                    visited.add(neibor)
        buses+=1
        len_que=len(que)
    return -1