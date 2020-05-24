# def licenseKeyFormatting(S, K):
#     S = S.upper()[::-1]
#     S = ''.join(e for e in S if e.isalnum())
#     n = len(S)//K
#     m = len(S)%K
#     ls = []
#     for i in range(n):
#         if i+1 <=n:
#             ls.append(S[i*K:(i+1)*K])
#     if m>0:
#         ls.append(S[-m:])
#     nS = '-'.join(ls)
#     return nS[::-1]

def licenseKeyFormatting(self, S: str, K: int) -> str:
    S = ''.join(S.upper().split('-'))
    m, n = len(S) % K, len(S) // K
    sl = '-'.join([S[m+i*K:m+(i+1)*K] for i in range(n)])
    if m == 0:
        return sl
    if n == 0:
        return S[:m]
    return S[:m] + '-' + sl


print(licenseKeyFormatting("5F3Z-2e-9-w", 4))
    