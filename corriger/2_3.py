
stock = ["Ordinateur de bureau", "Ordinateur portable",100, "Camera",310.28,"Haut-parleurs", 27.00, "Television", 1000, "Cartes meres", "souris", "clavier", 500,"barrettes de memoire"]
print(stock)

nombres = []

first_number = stock[2]
del stock[2]
nombres.append(first_number)

first_number = stock[3]
del stock[3]
nombres.append(first_number)

first_number = stock[4]
del stock[4]
nombres.append(first_number)

first_number = stock[5]
del stock[5]
nombres.append(first_number)

first_number = stock[8]
del stock[8]
nombres.append(first_number)

print(stock)
print(nombres)


print("Tri Chaines")
stock.sort(key=str.lower)
print(stock)
stock.sort(key=str.lower, reverse=True)
print(stock)

print("Tri Nombres")
nombres.sort()
print(nombres)
nombres.sort(reverse=True)
print(nombres)
