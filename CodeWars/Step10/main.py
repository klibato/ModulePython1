def score(dice):
    score = 0 
    """
    i = 0 

    while i < len(dice):
    
        if dice.count(dice[i]) >= 3:        #nombre d'occurence de i 
            if dice[i]==1:
                score += 1000 
            else : 
                score += dice[i]*100
        
        dice.remove()

        if dice[i] == 1 and dice.count(i) == 1 or dice[i] == 5 and dice.count(i) == 5: 
            if dice[i] == 1: 
                score += 100 
            if dice[i] == 5: 
                score += 50
        
        i+=1 
    """
    """
    (#) // -> quotient 
    (#)  % -> reste 
    5 = 3(dividende) * 1(quotient) + 2(reste)

    """
    score+=(dice.count(1)//3)*1000+(dice.count(1)%3)*100 #si on a plus de trois 1 on ajoute 1000, et pour chaque 1 inutilisés on ajoute 100 
    for i in range(2,7): 
        if i==5: 
            score+=(dice.count(5)%3)*50
        score+=(dice.count(i)//3)*100*i

    return score

print(score([1, 1, 1, 1, 2]))