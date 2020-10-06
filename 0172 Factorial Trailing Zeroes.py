# fives = n/5^1 + n/5^2 + n/5^3 + .... till 5^x > n
def trailingZeroes(n):
    zero_count = 0
    current_multiple = 5 # Denominator
    
    while n >= current_multiple: # Numerator >= Denominator
        zero_count += n // current_multiple
        current_multiple *= 5
    
    return zero_count