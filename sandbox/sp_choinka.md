## Pętla – jedna z trzech podstawowych konstrukcji programowania strukturalnego (obok instrukcji warunkowej i instrukcji wyboru). Umożliwia cykliczne wykonywanie ciągu instrukcji określoną liczbę razy, do momentu zajścia pewnych warunków, dla każdego elementu kolekcji lub w nieskończoność.  [Definicja z Wikipedii](https://pl.wikipedia.org/wiki/P%C4%99tla_(informatyka))

----
W tym ćwiczeniu widzimy następujące elementy:
* działania wykonywane wewnątrz bloku kodu pętli mają wcięcie (standardowo *4 spacje*)
* ten sam efekt możemy uzyskać w różny sposób

Pętlę w języku python zapisujemy w następujący sposób:

1) Wersja z użyciem funkcji `range`, która umożliwia wykonywanie bloku kodu określoną ilość razy

```python
# poniższy kod wypisze 10 cyfr, od 0 do 9
for x in range(10):
    print(x)
```

2) Wersja z użyciem opratora `in`, który pozwala iterować elementy kolekcji, np. listy lub napisu

```python
# poniższy kod wypisze wszystkie litery słowa
for lit in "Python":
    print(lit)
```

