import statistics
import random

 

#service = {"nom" : "Dupuis", "prenom": "Jacques", "age": "30"}

#service[" prenom "] = "Jacques"

#print(service.keys())

#print(service.values())




#print( service.get(" prenom")+ service.get(" nom")+" a "+ service.get("age")+"ans")

a= "p"

first_loop = "hello " 

first_loop2= " hi "

for a in first_loop :
    if a == "e" :
        print (a)
    

dico = {"prenom":"Clement","nom":"Roualin"}

for a in dico :

    print (a)

list4 = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]



for sunach in range (0,50) :
    print (sunach)

i = 0 
while i < 10 : 
    print (" toujours pas a 10")
    i+=1

list_prenom = ["jean", "paul", "eric"]
list_nom = ["roualin", "sagne", "sennepin"]

for a in list_prenom :
    print(a)
    
    for a in list_nom :
        print(a)



# Exercices 

    # Exercice 1

exe = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# 1
def somme(exe) :
    
    return print (sum(exe))

somme(exe)

# 2
def moy(exe) :

    return print (statistics.mean(exe))

moy(exe)

# 4



20

# 3

def index_max(exe) :

    return print ( max(exe))

index_max(exe)

# 5

texte = "salut comment cela va pour vous ce matin"

print ( texte.count ("e"))

# 6

n = 1

def check_positive(n) : 

    if n > 0 : 
        print ( "Positie" )

    elif n < 0 :
        print ( "Negative" )   

    else :
        
        return    print ( "Neutre" )


# 7

croissant =  [ 2, 4, 6, 8, 10]
decroissant = [ 10, 8, 6, 4, 2]

def testCroissant (croissant):
   
    elementPrecedent=croissant[0]
    
    for element in croissant:
       
        if elementPrecedent>element :
         
            return print(False)
        
        elementPrecedent=element   

    return print(True)
 

testCroissant(croissant)

#   Exercice 2

# 1

list10 = [10, 9 , 8, 7, 6, 5, 4, 3, 2]

def somme_start (list10) :
    
     print ( sum ( list10 [ 0 : 2]))

somme_start (list10)

# 2

n = int(input( "Entrer un entier n : "))
somme_paire = 0
somme_impaire = 0

def count_pair(n) :
    for i in range ( 0, n + 2) :
        
        if ( i % 2 == 0 ) :
             somme_paire.append ( +1 )
             return print ( " La somme des entiers pairs de 1 à ", n ,"est = " , somme_paire)
        
        else :
            somme_impaire ==somme_impaire + i 
            return print ( " La somme des entiers pairs de 1 à ", n ,"est = " , somme_impaire)

#  exercice 3

nbrListe  = [1, 2, 3, 3, 2, 4, 5]
new_list = [] 
for i in nbrListe : 
    if i not in new_list: 
        new_list.append(i) 
print(new_list)

# exercice 4 

x = []

def multipl (x) :
    
    tuile = [23, 60 , 45, 17, 27, 81] :

    if x % 9 == 0 :

       x = x/9 
    
    else :

        x = x-9
     
print (multipl(x))

# exercice 5 


    







# 6

classe = [ "Alexandre", "Clement ", "Adriane", "Bastien"," Leo", "romuald" ]

def select_random (classe) :

    return random.choice(classe)

print ( "le nom choisi est ", select_random(classe))

    













