# Zadanie - tworzymy program, w którym zbudujemy listę osób zaproszonych na nasze urodziny.

W naszym programie wykorzystamy kilka konstrukcji programistycznych:

Pętla `while` - to pętla, która działa tak długo, jak długo warunek jest spełniony. W tej pętli stosujemy również instrukcję warunkową, aby w określonym przypadku przerwać jej wykonywanie instrukcją `break`.

Następnie wykorzystujemy pętlę `for`, aby iterować po wszystkich elementach (imionach). Dla każdego z nich wykonujemy porównanie, czy ostatni znak to litera "a"

```python
if imie[-1:] == "a":
```

Taki zapis nazywamy `slice` lub `wycinkiem`. W języku Python możemy odnosić się do typu `string` tak jak do innych kolekcji. Więcej na ten temat [https://docs.python.org/3/tutorial/introduction.html#strings](https://docs.python.org/3/tutorial/introduction.html#strings)

Ogólnie o pętlach możemy przeczytać: [https://pl.wikipedia.org/wiki/P%C4%99tla_(informatyka)](https://pl.wikipedia.org/wiki/P%C4%99tla_(informatyka))

----

Przykładowe wywołanie naszego programu może wyglądać następująco:

```python
Podaj imię (END-Koniec): Adam
Podaj imię (END-Koniec): Ela
Podaj imię (END-Koniec): Beata
Podaj imię (END-Koniec): Krzysztof
Podaj imię (END-Koniec): Anna
Podaj imię (END-Koniec): Jarosław
Podaj imię (END-Koniec): Szymon
Podaj imię (END-Koniec): Magda
Podaj imię (END-Koniec): END
Zaprosiliśmy osoby: ['Adam', 'Ela', 'Beata', 'Krzysztof', 'Anna', 'Jarosław', 'Szymon', 'Magda'].
Ela to kobieta
Beata to kobieta
Anna to kobieta
Magda to kobieta
Zaprosiliśmy 4 kobiet i 4 mężczyzn.
```

[ABIX Edukacja](https://abixedukacja.eu) - Python dla nauczycieli
