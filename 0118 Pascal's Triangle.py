# '''
# numRows = 0/1/2特例
# numRows > 3：首尾加1，第二位开始遍历上一层相加
# '''

# def generate(numRows: int):
#     if numRows == 0:
#         return []
#     elif numRows == 1:
#         result = [[1]]
#     elif numRows == 2:
#         result = [[1],[1,1]]
#     else:
#         result = [[1],[1,1]]
#         i=1
#         while i <=numRows-2:
#             result.append([])
#             for j in range(len(result[-2])-1):
#                 result[-1].append(result[-2][j]+result[-2][j+1])
#             result[-1].insert(0,1)
#             result[-1].append(1)
#             i+=1
#     return result


def generate(num_rows):
    triangle = []

    for row_num in range(num_rows):
        # The first and last row elements are always 1.
        row = [None for _ in range(row_num+1)]
        row[0], row[-1] = 1, 1

        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right.
        for j in range(1, len(row)-1):
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

        triangle.append(row)

    return triangle

print(generate(0))
    