import math

def constructRectangle(area):
    n = math.ceil(math.sqrt(area))
    for i in range(n,area+1):
        if area % i == 0:
            return [i,int(area/i)]

print(constructRectangle(4))