def distributeCandies(candies):
    u = len(set(candies))
    return int(min(len(candies)/2,u))

print(distributeCandies([1,1,2,3]))