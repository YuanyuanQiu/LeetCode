def generatePossibleNextMoves(self, currentState: str) -> List[str]:
    ans=[]
    for i in range(len(currentState)-1):
        if currentState[i]==currentState[i+1]=='+':
            ans.append(currentState[:i]+'--'+currentState[i+2:])
    return ans