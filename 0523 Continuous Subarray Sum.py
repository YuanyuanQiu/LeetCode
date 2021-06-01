def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    '''
    同余定理：如果两个整数m、n满足n-m能被k整除，那么n和m对k同余
    即 ( pre(j) - pre (i) ) % k == 0 则 pre(j) % k == pre(i) % k
    '''
    # Key：pre(i) % k, Value: i
    cnt = defaultdict(int)
    cnt[0] = -1
    pre = 0
    for i,num in enumerate(nums):
        pre += num
        pre %= k
        if pre in cnt:
            if i - cnt[pre] >= 2:
                return True
        else:
            cnt[pre] = i
    return False