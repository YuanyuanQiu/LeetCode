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

print(compress(["a","a","b","b","c","c","c"]))