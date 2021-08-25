# Given an integer n, return the largest number that contains exactly n digits

def largestNumber(n):
    largest = ''
    for i in range(n):
        largest += '9'
    
    return int(largest)
