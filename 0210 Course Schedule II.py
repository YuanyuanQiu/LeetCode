def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # pre: [cur]
    dic = collections.defaultdict(list)
    # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
    visited = [0] * numCourses
    # 用数组来模拟栈，下标 0 为栈底，n-1 为栈顶
    stack = []
    # 判断有向图中是否有环
    nocircle = True

    for info in prerequisites:
        dic[info[1]].append(info[0])
    
    def dfs(u: int):
        nonlocal nocircle
        visited[u] = 1 # 搜索中
        # 搜索其相邻节点，只要发现有环，立刻停止搜索
        for v in dic[u]:
            if visited[v] == 0: # 如果「未搜索」那么搜索相邻节点
                dfs(v)
                if not nocircle:
                    return
            # 如果「搜索中」说明找到了环
            elif visited[v] == 1:
                nocircle = False
                return
        visited[u] = 2 # 已完成
        # 将节点入栈
        stack.append(u)
    
    # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
    for i in range(numCourses):
        if nocircle and not visited[i]:
            dfs(i)
    
    if not nocircle:
        return []
    
    # 如果没有环，那么就有拓扑排序
    # 注意下标 0 为栈底，因此需要将数组反序输出
    return stack[::-1]