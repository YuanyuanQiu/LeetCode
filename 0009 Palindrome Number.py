def isPalindrome(x):
        if x<0: #负数为False
            return False
        else:
            m,n = x,0 #m 表示原数字，n表示反转后数字
            while m:
                n = n*10 + m%10 #m取最后一位数字，逐步前推
                m = m//10 #m去除最后一位数字（//：返回整数部分
                # print(m,n)
                
            if x == n:
                return True
            else:
                return False

print(isPalindrome(121))