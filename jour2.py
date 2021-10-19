list = [ "orange", "banane", "fraise" ]

#print ( type [list] )

a = 25

list.append (a)

#print (list) 

list.remove ("banane")

#print (list)

list2 = [" kiwi", "pomme"], 

list2 = list[:]

#print ( list )

b = 35

list2.append (b)

#print (list)
#print (list2)

elist = list[1]

#print (elist)

list[1] = "fruit"
#print (list)

del list[1]
#print (list)

list3 = ["ball", "boule" ,"bille"]

string = ";".join(list3)

#print("Tranformation de list3 to string")
#print(string)

list3 = string.split(";")

#print(" tranformation string to list")
#print(list3)

#Exercice 1

#x = "billy"

#if x == "Jean" :
#    x = str("bonjour Jean")
#else :
#    print ("Bonjour")


#x = input(  )
#print("bonjour, jean")

#print("annee de naissance ")
#x = input()

#print (2021-int(x))

#Exercice 2

list4 = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

print (list4)
print (list4[4])

list4[0] = list4[-1]

print (list4)

#list4[-1] = list4[0]
# Exercice 4

#numList = [1,2,3,4,5]
#alphaList =["a","b","c","d","e"]

#print(numList is alphaList)

#print(numList == alphaList)

#numList = alphaList 

#print(numList is alphaList) 

#print(numList == alphaList) 

#print(numList)

#Exercice 5

#1
list5 =[17,38,10,25,72]

#2
list5.sort()
#print (list5)

#3 
list5.append (12)
#print(list5)

#4
list5.reverse()
#print(list5)

#5 
list5[4]
#print(list5)

#6 
list5.remove (38)
#print (list5)

#7
#print(list5[2:3])

#8
#print(list5[2:-1])

#cours 

dico ={}
dico = {"prenom":"Clement","nom":"Roualin"}
print (type)
print (dico)

dico ={}
dico ["nom"] ="Wayne"

print (dico)

dico ={"nom":"Wayne"}
dico.get("nom")

print(dico)

del dico ["nom"]

print (dico)

dico["age"] = 25

print (dico)

def indique_nom() :
     return print("Bruce")

indique_nom()

def augmente_moi(a, b ) :
    return print ( 30+a+b)

augmente_moi(5, 10)

v = 0
w = 5
try :
    x = w/v
except :
    print("ERROR")

print ("neh")



def condition(nombre) :

    if nombre == 11 :

        return print ("je vaux 11")

    elif nombre == 20 :

        return print ("je vaux 20")

    else :

        return print ("je ne sais pas")

condition(20)

def exemple(number) :

    if (number) == "je vaux 11" :

        return "exemple"

    else :
        return "je ne vaux pas 11"

exemple(11)

print(exemple)

servi





