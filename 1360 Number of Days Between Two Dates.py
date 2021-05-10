'''
公元年分为4的倍数但非100的倍数，为闰年，或
公元年分为400的倍数但非3200的倍数，为闰年
'''
def daysBetweenDates(self, date1: str, date2: str) -> int:
    def isLeap(year):
        return (year % 3200 != 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

    def date_to_int(date):
        y = date[:4]
        m = date[5:7]
        d = date[-2:]
        
        # from 1971 to y - 1
        years = 0
        for i in range(1971, int(y)):
            if isLeap(i):
                years += 366
            else:
                years += 365
        
        # from 01 to m - 1
        dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8:31, 9: 30, 10: 31, 11: 30, 12: 31}
        months = 0
        for i in range(1, int(m)):
            months += dic[i]
        if int(m) > 2 and isLeap(int(y)):
            months += 1

        # from 01 to d
        days = int(d)
        return years + months + days

    return abs(date_to_int(date2) - date_to_int(date1))
