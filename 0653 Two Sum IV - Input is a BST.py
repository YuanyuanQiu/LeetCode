def findTarget(self, root: TreeNode, k: int) -> bool:
    # 集合记录寻找目标
    d = set()
    ans = False
    
    def f(r):
        nonlocal ans # 全局变量
        # 树不为空且ans为False
        if r and not ans:
            # 已配对
            if r.val in d:
                ans = True
                return # 中断
            
            # 未配对，寻找目标加入集合
            d.add(k - r.val)
            
            # 寻找子集
            f(r.left)
            f(r.right)
            
    f(root)
    return ans

