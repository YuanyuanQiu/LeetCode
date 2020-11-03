def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
    ls1 = []
    ls2 = []

    for i, word in enumerate(words):
        if word == word1:
            ls1.append(i)

        if word == word2:
            ls2.append(i)

    dist = []
    for i in ls1:
        for j in ls2:
            dist.append(abs(i-j))
    
    return min(dist)