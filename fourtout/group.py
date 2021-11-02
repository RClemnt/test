import random



liste1 = [x for x in range ( 100 ) if x % 7 ==0]
print ( liste1)

liste2 = [ x**2 for x in range ( 10) if x**2 % 3==0]
print(liste2)


ab = str.split(" Faire un programme qui tient en une ligne donnant la liste des mots de longueur n dans une liste de mots donnée ")
liste3 = [ x for x in ab if len(x)>=5]

print ( liste3)

liste = str.split ["Alain Verse", "Harry Cover", "Marc Assin"]

liste4 =  [ word[:1] for word in liste  ]

print ( liste4)

