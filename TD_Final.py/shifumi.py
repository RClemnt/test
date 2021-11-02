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
    print ( "L'equipe rouge commence la phase de pick et ban. ")
    
elif winx >=2:
    print ( " L'equipe rouge commence la phase de pick et ban. ")























