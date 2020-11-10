## Pętla – jedna z trzech podstawowych konstrukcji programowania strukturalnego (obok instrukcji warunkowej i instrukcji wyboru). Umożliwia cykliczne wykonywanie ciągu instrukcji określoną liczbę razy, do momentu zajścia pewnych warunków, dla każdego elementu kolekcji lub w nieskończoność.  [Definicja z Wikipedii](https://pl.wikipedia.org/wiki/P%C4%99tla_(informatyka))

----
W tym ćwiczeniu widzimy następujące elementy:
* działania wykonywane wewnątrz bloku kodu pętli mają wcięcie (standardowo *4 spacje*)
* w pętli możemy umieścić instrukcję warunkową
* nauczymy się stosować operator `%` - oblicza on *resztę z dzielenia*


Wersja pętli z użyciem funkcji `range`, która umożliwia wykonywanie bloku kodu określoną ilość razy

```python
# poniższy kod wypisze 10 cyfr, od 0 do 9
for x in range(10):
    print(x)
```

Instrukcja warunkowa

```python
# poniższy kod wypisze wszystkie informację o parzystości
z = 3
if z % 2 == 0:
    print(f"Zmienna {z} jest parzysta.")
else:
    print(f"Zmienna {z} jest nieparzysta.")

z = 4
if z % 2 == 0:
    print(f"Zmienna {z} jest parzysta.")
else:
    print(f"Zmienna {z} jest nieparzysta.")
```
