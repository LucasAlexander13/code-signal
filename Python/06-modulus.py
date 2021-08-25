# Your task is to implement a function that, given a number n, 
# returns -1 if this number is not an integer and n % 2 otherwise. 
# It is guaranteed that if the number represents an integer, it 
# will be written without a decimal point.

def modulus(n):
    if int(n) - n == 0:
        return n % 2
    else:
        return -1

if __name__ == '__main__':
    while True:
        number = float(input('Enter a number: '))
        print(modulus(number))