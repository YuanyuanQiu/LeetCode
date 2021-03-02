'''
可以发现这样一个规律，如24的因子为1，2，3，4，6，8，12，24，我们只需要找到1，2，3，4
这四个数，就可以通过num/i的方式找出所有的因子，称这四个因子为小因子，称num/i得到的因
子为大因子，那么大因子和小因子的分割线正好是num**0.5，所以通过这个规律可以大幅度减小
时间复杂度。
'''
def checkPerfectNumber(num):
    if num<=1:
        return False
    
    count = 1
    
    for i in range(2,int(num**0.5)+1):
        # print(l,r,count)
        if num % i == 0:
            count += i
            count += num/i
        if count > num:
            return False

    return count == num

print(checkPerfectNumber(28))