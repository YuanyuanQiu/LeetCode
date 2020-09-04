def gcdOfStrings(str1, str2):
    # 从大到小
    for i in range(min(len(str1), len(str2)), 0, -1):
        # 判断是否公因子
        if (len(str1) % i) == 0 and (len(str2) % i) == 0:
            # 判断是否符合
            if str1[: i] * (len(str1) // i) == str1 and str1[: i] * (len(str2) // i) == str2:
                return str1[: i]
    return ''

print(gcdOfStrings("ABCABCABC", "ABCAAA"))