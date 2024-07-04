def minWindow(self, s: str, t: str) -> str:
    # ans_left设为-1以排除不存在的极端情况
    ans_left, ans_right = -1, len(s)
    left = 0
    cnt_s = Counter()  # s 子串字母的出现次数
    cnt_t = Counter(t)  # t 中字母的出现次数
    for right, c in enumerate(s):  # 移动子串右端点
        cnt_s[c] += 1  # 右端点字母移入子串
        while cnt_s >= cnt_t:  # 涵盖
            if right - left < ans_right - ans_left:  # 找到更短的子串
                ans_left, ans_right = left, right  # 记录此时的左右端点
            cnt_s[s[left]] -= 1  # 左端点字母移出子串
            left += 1  # 移动子串左端点
    return "" if ans_left < 0 else s[ans_left: ans_right + 1]