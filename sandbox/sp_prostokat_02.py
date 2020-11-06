# mamy prostokąt, podajemy jego wymiary, liczymy powierchnie

# za pomocą funkcji input wczytujemy dane z klawiatury
# za pomocą funkcji float zmieniamy na ułamek
# kropka rozdziela część całkowitą od ułamkowej
a = input("podaj długość boku a (liczba): ")
b = input("podaj długość boku b (liczba): ")
print("-------------------------------")

# sprawdzamy, czy użytkownik podał odpowiednie dane....
if a.replace('.', '', 1).isdigit():
    print("Dziękuję, podano prawidłowy typ danych dla 'a'.")
    a_ok = float(a)
else:
    print("Uwaga - dane wejściowe są nieporawne")
    a_ok = 10
    print("Przyjmuję 10 jako daną 'a'.")


if b.replace('.', '', 1).isdigit():
    print("Dziękuję, podano prawidłowy typ danych dla 'b'.")
    b_ok = float(b)
else:
    print("Uwaga - dane wejściowe są nieporawne")
    b_ok = 2.34
    print("Przyjmuję 2.34 jako daną 'b'.")

# obliczamy
pole = a_ok * b_ok
obwod = 2 * (a_ok + b_ok)

# wypisujemy wyniki
print("---[ Nasz wynik to]---")
print(f"Pole to {pole}, obwód = {obwod}")
