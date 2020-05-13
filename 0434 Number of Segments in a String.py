# def countSegments(s):
#     return(len(s.split()))

def countSegments(s):
    segment_count = 0

    for i in range(len(s)):
        if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
            segment_count += 1

    return segment_coun

print(countSegments("Hello, my name is John"))