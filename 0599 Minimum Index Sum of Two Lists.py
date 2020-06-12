def findRestaurant(list1, list2):
    ind = 10000000
    res = []
    for i in list(set(list1) & set(list2)):
        if list1.index(i) + list2.index(i) < ind:
            ind = list1.index(i) + list2.index(i)
            res = []
            res.append(i)
        elif list1.index(i) + list2.index(i) == ind:
            res.append(i)
    return res

print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
                     ["KFC","Burger King","Tapioca Express","Shogun"]))

        