def getHint(secret, guess):
    bulls = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
            secret = secret.replace(secret[i],'x',1)
            guess = guess.replace(guess[i],'x',1)
   
    cows = 0
    for j in secret:
        if j in guess and j != 'x':
            cows +=1
            secret = secret.replace(j,'x',1)
            guess = guess.replace(j,'x',1)

    return str(bulls)+'A'+str(cows)+'B'

print(getHint('1122','2211'))
            
        