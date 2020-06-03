def findLUSlength(a, b):
    if a == b:
        return -1
    if len(a) > len(b):
        return len(a)
    elif len(a) < len(b):
        return len(b)

    for i in range(len(a)):
        if a[i] != b[i]:
            return len(a[i:])

print(findLUSlength("horbxeemlgqpqbujbdagizcfairalg", 
                    "iwvtgyojrfhyzgyzeikqagpfjoaeen"))