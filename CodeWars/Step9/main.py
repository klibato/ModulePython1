def tribonacci(signature, n):

    if n <= 3: 
        return signature[:n] 

    else : 

        for j in range(n-3):
            signature+= [signature[-1] + signature[-2] + signature [-3]]

    return signature

"""
Juste de l'arithmétique avec une condition avant pour couper la signature 
"""
print(tribonacci([1,1,1], 1))