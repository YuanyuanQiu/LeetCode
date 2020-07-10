def letterCombinations(digits: str):
    conversion={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs',
                '8':'tuv','9':'wxyz'}
    
    if len(digits)==0:
        return []
    
    product=['']
    result = []
    k = 0
    while k<len(digits):
        for i in product:
            for j in conversion[digits[k]]:
                result.append(i+j)
        product = result
        result = []
        k+=1
    
    # for k in digits:
    #     product=[i+j for i in product for j in conversion[k]]
    return product
        
print(letterCombinations('234'))




