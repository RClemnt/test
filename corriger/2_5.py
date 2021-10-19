liste = [17, 38, 10, 25, 72]

print("Liste Triée")
liste.sort()

print(liste)

print("Ajouter 12 à liste")
liste.append(12)

print(liste)

print("Supprimer le nombre 38 de la liste")
liste.remove(38)

print(liste)

print("Affichier du 2éme au 3éme élément")
second_liste = liste[1:3]

print(second_liste)


print("Affichier du début au 2éme élément")
second_liste = liste[:2]

print(second_liste)

print("Affichier 3éme élément à la find e la liste")
second_liste = liste[-3:]

print(second_liste)

print("Affichier le dernier élément")
second_liste = liste[-1:]

print(second_liste)

print("Transformer la liste en string")

value = ":".join([str(i) for i in liste])

print(value)

print("Concatenez :175 à la nouvelle chaine de caractere")
value += ":175"

print(value)

print("Transformez le string en liste")
liste = value.split(":")


print(liste)


