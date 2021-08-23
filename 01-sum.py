# Write a function that returns the sum of two numbers.

def add(param1, param2):
    if param1 >= -1000 and param1 <= 1000:
        if param2 >= -1000 and param2 <= 1000:
            return param1 + param2
    else:
        return "input too long"

if __name__ == '__main__':
    while True:
        print(add(int(input('Enter a number: ')), int(input('Enter another one: '))))
