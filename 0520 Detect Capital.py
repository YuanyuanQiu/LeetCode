def detectCapitalUse(word):
    if word == word.upper() or word == word.lower():
        return True
    if word[0] == word[0].upper() and word[1:] == word[1:].lower():
        return True
    return False

print(detectCapitalUse('FlaG'))