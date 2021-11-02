
from random import *

import random



choices = ["pierre", "feuille", "ciseaux"]
watigang = 0
winx = 0


while  not watigang + winx == 3 :

    b = random.choice(choices)
    r =  random.choice(choices)
    #print ( r , b)

    if r == "feuille"  and b == "pierre" :
        winx +=1
        #print(winx)

    if b == "feuille" and r == "pierre" :
        watigang += 1
        #print(watigang)

    if b == "ciseaux" and r == "feuille" :
        watigang +=1
        #print(watigang)

    if r == "ciseaux" and b == "feuille" :
        winx += 1
        #print(winx)

    if r == "pierre" and b == "ciseaux" :
        winx+=1
        #print(winx)

    if b == "pierre"  and r == "ciseaux" :
        watigang += 1
        #print(watigang)
    
#print( winx , watigang)


if watigang  >=2 :
    print ( "L'equipe WatiGang commence la phase de pick et ban. ")
    
elif winx >=2:
    print ( " L'equipe Winx commence la phase de pick et ban. ")




champions =[
{"name" :"kratos", "point de vie" :80, "attaque" : 12, "vitesse" : 8, "defense" : 4},
{"name" :"Bond", "point de vie" :50, "attaque" : 10, "vitesse" : 12, "defense" : 5},
{"name" :"wejdene", "point de vie" :120, "attaque" : 8, "vitesse" : 5, "defense" : 5},
{"name" :"Cpt_Falcon", "point de vie" :100, "attaque" : 11, "vitesse" : 15, "defense" : 7},
{"name" :"marwa_loud", "point de vie" :100, "attaque" : 15, "vitesse" : 10, "defense" : 3},
{"name" :"Djidane", "point de vie" : 70, "attaque" : 12, "vitesse" : 14, "defense" : 3},
{"name" :"Samus", "point de vie" :110, "attaque" : 10, "vitesse" : 7, "defense" : 7},
{"name" :"Sonic", "point de vie" :60, "attaque" : 15, "vitesse" : 16, "defense" : 2},
{"name" :"Pikachu", "point de vie" :60, "attaque" : 12, "vitesse" : 15, "defense" : 4},
{"name" :"Mario", "point de vie" :75, "attaque" : 9, "vitesse" : 9, "defense" : 4},
{"name" :"Zemmour", "point de vie" :90, "attaque" : 12, "vitesse" : 7, "defense" : 4},
{"name" :"Elsa", "point de vie" :70, "attaque" : 8, "vitesse" : 11, "defense" : 5},
{"name" :"Link", "point de vie" :110, "attaque" : 13, "vitesse" : 9, "defense" : 6},
{"name" :"Kirby", "point de vie" :65, "attaque" : 7, "vitesse" : 7, "defense" : 4},
{"name" :"Sora", "point de vie" :85, "attaque" : 11, "vitesse" : 12, "defense" : 4},
{"name" :"roland_cristal", "point de vie" :50, "attaque" : 18, "vitesse" : 12, "defense" : 2},
{"name" :"Diablo", "point de vie" :135, "attaque" : 12, "vitesse" : 4, "defense" : 7},
{"name" :"Mickey", "point de vie" :70, "attaque" : 8, "vitesse" : 13, "defense" : 4},
{"name" :"Red_Sorcerer", "point de vie" :55, "attaque" : 16, "vitesse" : 10, "defense" : 2}]

watigang1= []
winx1 = []


copie_champ = list(champions)



select_ban = []




def select_random (copie_champ) :

    return random.choice(copie_champ)
print ( "le champion choisi est ", select_random(copie_champ))





def ban() :

    copie_champ = list(champions)

    if watigang or winx >= 2 :
        

        for i in range (3) :
            #print ( "entrer")

            select_ban.append ( select_random ( copie_champ) )

            
        copie_champ = [elem for elem in champions if elem not in select_ban]

        #print (copie_champ)
        #print ( len(copie_champ))

    if watigang or winx <= 1 :

        for i in range (3) :
            #print ( "entrer")

            select_ban.append ( select_random ( copie_champ) )
            
        copie_champ = [elem for elem in champions if elem not in select_ban]

        #print (copie_champ)
        #print ( len(copie_champ))

    return print ( " fin de la phase des bans. ")

ban()

#












