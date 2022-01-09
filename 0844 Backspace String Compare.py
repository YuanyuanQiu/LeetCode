def backspaceCompare(self, s: str, t: str) -> bool:
    def backspace(s):
        s.lstrip('#')
        temp = ''
        for i in s:
            if i != '#':
                temp += i
            else:
                temp = temp[:-1]
        return temp
    return backspace(s) == backspace(t)