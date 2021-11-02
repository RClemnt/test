nbrListe  = [1, 2, 3, 3, 2, 4, 5]
new_list = [] 
for i in nbrListe : 
    if i not in new_list: 
        new_list.append(i) 
print(new_list)
