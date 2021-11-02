import random


choices = ["pierre", "feuille", "ciseaux"]
blue = 0
red = 0


while  not blue + red == 3 :

    b = random.choice(choices)
    r =  random.choice(choices)
    #print ( r , b)

    if r == "feuille"  and b == "pierre" :
        red +=1
        #print(red)

    if b == "feuille" and r == "pierre" :
        blue += 1
        #print(blue)

    if b == "ciseaux" and r == "feuille" :
        blue +=1
        #print(blue)

    if r == "ciseaux" and b == "feuille" :
        red += 1
        #print(red)

    if r == "pierre" and b == "ciseaux" :
        red +=1
        #print(red)

    if b == "pierre"  and r == "ciseaux" :
        blue += 1
        #print(blue)
    
#print( red , blue)


if blue  >=2 :
    print ( "L'equipe rouge commence la phase de pick et ban. ")
    
elif red >=2:
    print ( " L'equipe rouge commence la phase de pick et ban. ")





































