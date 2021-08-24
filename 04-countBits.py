# Implement a function that, given an integer n, uses a specific method on 
# it and returns the number of bits in its binary representation.

def countBits(n):
    total = n
    binario = []
    while (total != 1):
        
        restante = total % 2
        total = total // 2
        binario.append(str(restante))

        if (total == 1):
            binario.append("1")
            
    binario = "".join(binario)
    return len(binario)
