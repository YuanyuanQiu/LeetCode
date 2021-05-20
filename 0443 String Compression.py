def compress(chars):
    # anchor为起始位置
    anchor = write = 0
    for read, c in enumerate(chars):
        # 当读到最后一个字符，或者下一个下一个字符与当前不同时
        if read + 1 == len(chars) or chars[read + 1] != c: 
            chars[write] = chars[anchor] # write character
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit # write digits
                    write += 1
            anchor = read + 1
    return write


def compress(self, chars: List[str]) -> int:
    n = len(chars)
    if n == 1:
        return 1
    fast, slow = 0, 0
    
    while fast < len(chars):
        if chars[fast] == chars[slow]:
            fast += 1
        elif chars[fast] != chars[slow]:
            if fast - slow != 1:
                length = str(fast - slow)
                tmp = [chars[slow]]
                for i in length:
                    tmp.append(i)
                chars[slow:fast]= tmp
                slow += len(tmp)
            else:
                chars[slow:fast]= [chars[slow]]
                slow += 1
            fast = slow + 1
    
    if fast - slow != 1:
        length = str(fast - slow)
        tmp = [chars[slow]]
        for i in length:
            tmp.append(i)
        chars[slow:fast]= tmp
    else:
        chars[slow:fast]= [chars[slow]]
    return len(chars)