def removeDuplicates(S):
    output = []
    for ch in S:
        if output and ch == output[-1]: 
            output.pop()
        else: 
            output.append(ch)
    return ''.join(output)

print(removeDuplicates("abbaca"))