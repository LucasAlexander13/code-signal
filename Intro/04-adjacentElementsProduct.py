# Given an array of integers, find the pair of adjacent elements 
# that has the largest product and return that product.

def adjacentElementsProduct(inputArray):
    high_value = -1000
    
    for i in range(len(inputArray)):
        if i == len(inputArray) - 1:
            break
        else:    
            value_one = inputArray[i]
            value_two = inputArray[i + 1]
            product = value_one * value_two
            
            if product > high_value:
                high_value = product
    return high_value
