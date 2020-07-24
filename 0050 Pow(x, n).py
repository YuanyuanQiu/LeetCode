def myPow(x, n):
    
    # 递归
    def quickMul(N):
        
        # 边界为0
        if N == 0:
            print('return',1)
            return 1.0
        
        y = quickMul(N // 2)

        if N % 2 == 0:
            print('return',y * y)
            return y * y
        else:
            print('return',y * y * x)
            return y * y * x
    
    # 判断正负
    return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

print(myPow(3, 5))
    