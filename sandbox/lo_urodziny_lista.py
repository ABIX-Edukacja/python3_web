# budujemy listę znajomych na urodziny
# kończymy wpisująć imię END

lista_znajomych = []

while True:
    zaproszona_osoba = input("Podaj imię (END-Koniec): ")
    if zaproszona_osoba == "END":
        break
    else:
        lista_znajomych.append(zaproszona_osoba)

print(f"Zaprosiliśmy osoby: {lista_znajomych}.")

# zliczamy ilość zaproszonych kobiet i mężczyzn
kobiet = 0
for imie in lista_znajomych:
    # sprawdzamy ostatnią literę
    if imie[-1:] == "a":
        print(f"{imie} to kobieta")
        kobiet += 1

print(f"Zaprosiliśmy {kobiet} kobiet i {len(lista_znajomych) - kobiet} mężczyzn.")
