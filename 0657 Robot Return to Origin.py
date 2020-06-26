# def judgeCircle(moves):
#     dic = {}
#     for i in moves:
#         dic[i] = dic.get(i,0)+1

#     for j in 'UDLR':
#         dic[j] = dic.get(j,0)

#     if dic['U'] == dic['D'] and dic['L'] == dic['R']:
#         return True
#     else:
#         return False

def judgeCircle(moves):
    return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")


print(judgeCircle('LL'))