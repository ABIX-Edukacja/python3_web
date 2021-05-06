## Przykładowe ćwiczenie dla uczniów maturalnych.

Naszym zadaniem jest policzenie unikatowych wystąpień liczb w liście (tablicy) i podanie, która liczba występuje najwięcej, a która najmniej razy.

Przede wszystkim musimy sprawdzić unikatowe liczby występujące w liście - wykonamy to za pomocą stworzenia zbioru w Pythonie:
```
lista = [1,6,3,4,3,2,2,2,2,3,5,5,3,3,3,1,1,1,5,5,5,5,5,5,54,54,6,6,6,6,6,3,3,
        3,3,4,4,4,4,44,4,2,2,3,3,3,2,2,23,3,1,1,1,5,5,1,6,3,4,3,2,2,2,2,3,5,5,
        3,3,3,1,1,1,1,6,3,4,3,23,2,2,2,3,5,5,3,3,3,1,1,1,1,6,3,4,3,2,2,2,2,3,5,
        5,3,3,3,1,1,1,1,6,3,4,3,2,2,2,2,3,5,5,3,3,3,1,1,1,1,]

zbior = set(lista)
print(zbior)

# efekt działania
{1, 2, 3, 4, 5, 6, 44, 54, 23}
```

Następnie iterujemy przez elementy naszego zbioru i wykorzystując metodę `count()` zliczamy ilości naszych elementów. Jeśli zliczona wartość jest większa niż aktualne maksimum, dodajemy do listy maksimum jako pierwszą pozycję naszą liczbę, a jako drugą zliczoną ilość. Analogicznie postępujemy z obliczanym minimum, ale tu na początku ustawiamy wartość `999` jako pierwszą, z którą będziemy porównywać nasze zliczenia - czy wiesz, dlaczego?
Na końcu po prostu wyświetlamy na ekranie wynik.

[ABIX Edukacja](https://abixedukacja.eu) - Python dla nauczycieli
