def square_digits(num):

  
  convert = str(num)
  tab = ''

  for i in range(len(convert)): 
    tab += str(int(convert[i])**2) # On spécifie bien que ce sont des int qui seront enregistrés 

  return int(tab)

  """
  On convertit le int en parametre en string afin de la parcourir et d'ajouter à la x-éme valeur 
  sont carré. On oublie pas à la fin de spécifier qu'on retourne des valeurs "int".
  """
