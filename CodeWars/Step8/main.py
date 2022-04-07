"""
# [1000, 100, 50, 10, 5, 1]
# ['M', 'D', 'C', 'L', 'X', 'V', 'I']
"""  

def solution(n):
    
    dico = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
    
    res = ""

    for key in dico: 
        while n >= key: 
            res += dico[key]
            n = n - key 
            # print(n)
    print(res)

"""
On crée un dictionnaire avec toutes les clés valeurs, on le parcours, et on soustrait la clé pour enregistrer 
dans une variable son équivalent "romain". 
"""
solution(2000)

































        # if n > value[i]: 
        #     n - value[i]
        # print(value[i])     
        # i+=1

    # for i in range(len(symbol)): 
    #     print(symbol)


    # return