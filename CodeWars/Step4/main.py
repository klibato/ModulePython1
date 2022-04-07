def shortcut( s ):
    vowels = ['a','e','i','o','u']
    
    tmp = ""
    
    for i in s: 
        if i not in vowels: 
            tmp += i
    return tmp 

"On parcourt le string donné en parametre en stockant la lettre si elle n'appartient pas au tableau vowels"