def plusOne(self, digits: List[int]) -> List[int]:
    n = len(digits)
    carry = 1
    for i in range(n-1, -1, -1):
        if digits[i] + carry >= 10:
            carry = 1
            digits[i] = (digits[i] + carry) % 10
        else:
            digits[i] = digits[i] + carry
            carry = 0
            break
    if carry != 0:
        digits = [1] + digits
    return digits