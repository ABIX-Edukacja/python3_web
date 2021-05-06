# zadanie maturalne - oblicz ilość wystąpień unikatowych liczb naturalnych w liście
# podaj liczbę, która występuje największą oraz najmniejsza ilość razy
lista = [1,6,3,4,3,2,2,2,2,3,5,5,3,3,3,1,1,1,5,5,5,5,5,5,54,54,6,6,6,6,6,3,3,
        3,3,4,4,4,4,44,4,2,2,3,3,3,2,2,23,3,1,1,1,5,5,1,6,3,4,3,2,2,2,2,3,5,5,
        3,3,3,1,1,1,1,6,3,4,3,23,2,2,2,3,5,5,3,3,3,1,1,1,1,6,3,4,3,2,2,2,2,3,5,
        5,3,3,3,1,1,1,1,6,3,4,3,2,2,2,2,3,5,5,3,3,3,1,1,1,1,]

zbior = set(lista)
maximum = [0, 0]
minimum = [0, 999] # tutaj zaczynamy od absurdalnie dużej liczby wystąpień
                   # dla nieistniejącego elementu
for element in zbior:
    zlicz = lista.count(element)
    print(f"Liczba {element} występuje {zlicz} razy.")
    if zlicz > maximum[1]:
        maximum[0] = element
        maximum[1] = zlicz
    if zlicz < minimum[1]:
        minimum[0] = element
        minimum[1] = zlicz

print(f"Najwięcej {maximum[1]} jest liczb {maximum[0]}.")
print(f"Najmniej {minimum[1]} jest liczb {minimum[0]}.")
