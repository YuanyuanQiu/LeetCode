def canPlaceFlowers(flowerbed, n):
    flowerbed = [0] + flowerbed + [0]

    for i in range(1,len(flowerbed)-1):
        if  flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            n = n-1
            flowerbed[i] = 1
    return n <= 0


print(canPlaceFlowers(flowerbed = [1,0,0,0,0,1], n = 2))