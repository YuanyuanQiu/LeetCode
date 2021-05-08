def monotoneIncreasingDigits(self, N: int) -> int:
    s = str(N)
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            new = int(s[:i] + str(int(s[i]) - 1) + '9' * len(s[i+1:]))
            break
    else:
        return N
    return self.monotoneIncreasingDigits(new)