# Given a year, return the century it is in. The first century spans 
# from the year 1 up to and including the year 100, the second from 
# the year 101 up to and including the year 200, etc.

def centuryFromYear(year):
    sec = year / 100
    if (year % 100) == 0:
        sec = (int(sec))
        return sec
    else:
        sec = int(sec + 1)
        return sec
