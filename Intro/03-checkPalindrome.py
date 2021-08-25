# Given the string, check if it is a palindrome.

def checkPalindrome(inputString):
    return inputString == inputString[::-1]

if __name__ == '__main__':
    while True:
        print(checkPalindrome(input('Enter a string to check if it is a palindrome: ')))
