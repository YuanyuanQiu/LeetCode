def getRow(rowIndex: int):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        result = [1,1]
    else:
        i = 2
        begin = [1,1]
        while i <= rowIndex:
            result = []
            for j in range(len(begin)-1):
                result.append(begin[j]+begin[j+1])
            result.insert(0,1)
            result.append(1)
            i+=1
            begin = result
    return result

print(getRow(4))