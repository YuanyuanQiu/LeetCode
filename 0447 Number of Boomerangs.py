def numberOfBoomerangs(points):
    def distance(x,y):
        dis = pow(pow(x[0]-y[0],2)+pow(x[1]-y[1],2),0.5)
        return dis
    count = 0
    for i in range(len(points)):
        dic = {}
        for j in range(len(points)):
            if i != j:
                dis = distance(points[i],points[j])
                dic[dis] = dic.get(dis,0)+1
        for k in dic:
            if dic[k]>=2:
                count+= dic[k]*(dic[k]-1)

    return count
            
print(numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))