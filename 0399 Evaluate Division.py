def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    from collections import defaultdict
    graph = defaultdict(int) # (a, b): value，不存在则返回0
    set1 = set() # 存储每一个点set(a, b, c, ...)
    for i in range(len(equations)):
        a, b = equations[i]
        graph[(a, b)] = values[i]
        graph[(b, a)] = 1/values[i]
        set1.add(a)
        set1.add(b)

    # Floyd算法 求图中任意2点距离，补足dic
    arr = list(set1)
    for k in arr:
        for i in arr:
            for j in arr:
                if graph[(i, k)] and graph[(k, j)]:
                    graph[(i, j)] = graph[(i, k)] * graph[(k, j)]
    
    res = []
    for x, y in queries:
        if graph[(x, y)]:
            res.append(graph[(x, y)])
        else:
            res.append(-1)
    return res