# Implement a function that, given an integer n, uses a specific method on 
# it and returns the number of bits in its binary representation.

# return n.bit_length()

# This is the easiest way to solve the challenge. but I preferred to use 
# my knowledge of computational math to solve it.

def countBits(n):
    total = n
    binario = []
    while (total != 1):
        
        restante = total % 2
        total = total // 2
        binario.append(str(restante))

    if (total == 1):
        binario.append("1")
        binario = reverseString(binario)

    return len(binario)

def reverseString(array):
    array = ''.join(array[::-1])
    print(array)
    return array


if __name__ == '__main__':
    while True:
        number = int(input('Enter a number: '))
        print(countBits(number))
