def maximumSwap(num):
    # 先将int转为ls，方便遍历
    ls = list(str(num))
    
    # last_ind[i] 表示最后出现的索引
    last_ind = [None for _ in range(10)]

    # 统计每个数字出现的最后的位置
    for i, digit in enumerate(ls):
        last_ind[int(digit)] = i

    # 从最高位开始，往后面寻找有没有比他大的最大元素
    for i, digit in enumerate(ls):
        # 从最低位开始寻找
        for index in range(9, int(digit), -1):
            if last_ind[index] and last_ind[index] > i:
                # last_ind[index] 和 i 位置的元素交换
                ls[last_ind[index]], ls[i] = ls[i], ls[last_ind[index]]
                return int(''.join(ls))
    # 已是最大值就返回原数字
    return num

print(maximumSwap(9937))