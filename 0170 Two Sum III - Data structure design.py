class TwoSum(object):
 
    def __init__(self):
        self.dic = {}
 
    def add(self, number):
        self.dic[number] = self.dic.get(number,0) + 1
 
    def find(self, value):
        dic = self.dic
        for num in dic:
            if value - num in dic and (value - num != num or dic[num] > 1):
                return True
        return False