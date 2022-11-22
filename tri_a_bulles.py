### exo 1 ###


### création du tableau ###
myTable = [7,12,56,3]

### création valeurs entier ###
v = 0

### permutaion de la valeur 0 et la valeur 1 ###
v = myTable[0]
myTable[0] = myTable[1]
myTable[1] = v

### print du tableau ###
print(myTable)          



### exo 2 ###

### création du tableau ###
myTable = [7,12,56,3]

### création valeurs ###
plusGrandeValeur = myTable[0]   ### valeur prend premiere valeur du tableau ###
v = 0


for i in range(len(myTable)):                 ### pour i allant du debut à la fin du tableau ###
    if(plusGrandeValeur < myTable[i]):         ### si plusGrandeValeur est plus petite que myTable[i] faire ###
        plusGrandeValeur= myTable[i]
        myTable[i] = v
        myTable.pop(i)                        ### retire l'element à la position(i) ###
        myTable.append(plusGrandeValeur)      ### mets plusGrandeValeur à la fin du tableau ###

### print du tableau ###
print (myTable)                               ### ne marche pas me mets  pas plusGrandeValeur en position 1 du tableau ###



### exo 3 ###

### création du tableau ###
myTable = [7,12,56,3]

### création valeurs ###
plusGrandeValeur = myTable[0]   ### valeur prend premiere valeur du tableau ###
v = 0


for k in range(len(myTable)):                      ### pour k allant du debut à la fin du tableau faire : ###
    for i in range(len(myTable)):                  ### pour i allant du debut à la fin du tableau faire : ###
        if(plusGrandeValeur < myTable[i]):         ### si plusGrandeValeur est plus petite que myTable[i] faire ###
            plusGrandeValeur = myTable[i]
            myTable[i] = v
            myTable.pop(i)                         ### retire l'element à la position(i) ###
            myTable.append(plusGrandeValeur)       ### mets plusGrandeValeur à la fin du tableau ###


### print du tableau ###
print (myTable)                                    ### ne marche pas sur les valeurs 0 et 1 du tableau à la fin du tri ###
   


### exo 4 ###

"""car le programme doit regardé à chaque fois toute les valeurs du tableau une à une et recommencé pour chaque (boucle)"""