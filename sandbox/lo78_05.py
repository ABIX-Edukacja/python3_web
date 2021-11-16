def szyfr(litera):
    # GA DE RY PO LU KI
    # zadanie -> zmień odpowiednio listy na nowe wartości
    # PO LI TY KA RE NU DG 1# 2$ 3% 4! 5) 6& 7^ 8( 9* 0@ :> ;< .? ,/
    lista_a = ["G","D","R","P","L","K"]
    lista_b = ["A","E","Y","O","U","I"]
    if litera in lista_a:
        pos = lista_a.index(litera)
        return lista_b[pos]
    if litera in lista_b:
        pos = lista_b.index(litera)
        return lista_a[pos]
    return litera


jawny_tekst = input("Podaj tekst:")
# przypisujemy wersję o wielkich literach - metoda S.upper()
jawny_tekst = jawny_tekst.upper()
szyfrowana = ""
# wykorzystujemy pętlę iteracyjną
for lit in jawny_tekst:
    # w bloku kodu zwiększamy ciąg znaków
    # o kolejne przetworzone litery
    szyfrowana += szyfr(lit)

print(f"Szyfrowany tekst: {szyfrowana}")
