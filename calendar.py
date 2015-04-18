__author__ = 'Sergey Churyukin'

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_till_year(year):
    num = 0
    for y in range(1, year):
        if is_leap_year(y):
            num += 366
        else:
            num += 365
    return num

def calendar(year):
    num = days_till_year(year)
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days[1] = 29
    days_of_week = ["Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"]

    print("Year %s" % year)

    for month in range(0, 12):
        print (months[month])                       # print month
        for day in range(1, days[month] + 1):
            print(days_of_week[num % 7], end = " ")
            num += 1
        print()
        for day in range(1, days[month] + 1):
            if day < days[month]:
                print(day, end = "  ")
                if int(day / 10) == 0:
                    print(" ", end = "")
            else:
                print(day)

calendar(2017)

#This is a test comment

