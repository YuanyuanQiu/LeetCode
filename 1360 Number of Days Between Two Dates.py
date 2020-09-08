'''
公元年分为4的倍数但非100的倍数，为闰年，或
公元年分为400的倍数但非3200的倍数，为闰年
'''

def leap_year(self, year):
    return (year % 3200 != 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

# 由于题目中的日期不会早于 1971 年，我们可以将两个日期转化为距离 1971 年 1 月 1 日的天数
def date_to_int(self, year, month, day):
    ans = 0
    month_length = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    while year != 1971 or month != 1 or day != 1:
        ans += 1
        # 往前一天
        day -= 1
        # 往前一个月
        if day == 0:
            month -= 1
            day = month_length[month]
            # 判断闰年
            if month == 2 and self.leap_year(year):
                day += 1
        # 往前一年
        if month == 0:
            year -= 1
            month = 12
    return ans

def daysBetweenDates(self, date1: str, date2: str) -> int:
    date1 = [int(i) for i in date1.split('-')]
    date2 = [int(i) for i in date2.split('-')]
    return abs(self.date_to_int(*date1) - self.date_to_int(*date2))
