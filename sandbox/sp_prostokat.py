# mamy prostokąt, podajemy jego wymiary, liczymy powierchnie

# za pomocą funkcji input wczytujemy dane z klawiatury
# za pomocą funkcji float zmieniamy na ułamek
# kropka rozdziela część całkowitą od ułamkowej
a = float(input("podaj długość boku a (liczba): "))
b = float(input("podaj długość boku b (liczba): "))

# obliczamy
pole = a*b
obwod = 2*(a+b)

# wypisujemy wyniki
print(f"Pole to {pole}, obwód = {obwod}")
