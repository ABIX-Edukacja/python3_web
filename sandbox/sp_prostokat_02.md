# W Pythonie możemy pobierać od użytkownika dane

W poprzednim przykładzie obliczaliśmy różne rzeczy, ale nasz program był wrażliwy na dane wejściowe. Jeśli podaliśmy tekst, program przerywał swoje działanie. W tej lekcji dodamy sprawdzenie typu wprowadzonych danych i jeśli będą złe (nie takie, jakich oczekujemy), poprawimy i jeszcze wypiszemy odpowiedni komunikat.

Do tego celu użyjemy instrukcji warunkowych. Przykładowa konstrukcja wygląda następująco:

```python
if a.replace('.', '', 1).isdigit():
    print("Dziękuję, podano prawidłowy typ danych dla 'a'.")
    a_ok = float(a)
else:
    print("Uwaga - dane wejściowe są nieporawne")
    a_ok = 10
    print("Przyjmuję 10 jako daną 'a'.")
```

Czytamy taką instrukcję:

**Jeśli (`if`) dana `a` składa się tylko z cyfr, wówczas wykonujemy `blok kodu`, a w przeciwnym wypadku (`else`) wykonujemy inny `blok kodu`**

Musimy wyjaśnić tutaj skomplikowany zapis:
```python
a.replace('.', '', 1).isdigit()
```

Najpierw wykonywany jest kod : `a.replace('.', '', 1)` - dla zmiennej `a` wykonywane jest zamienienie pierwszego wystąpienia znaku `. (kropka)` na nic, a więc w praktyce usunięcie znaku kropki z napisu, np.: `3.14` zostanie zmienione na `314`. Następnie wykonywana jest metoda `isdigit()`, która zwraca wartość `True` jeśli są tylko cyfry - wówczas mamy pewność, że dane wczytane z klawiatury będą mogły być zmienione na liczbę.

Dokumentacja dla metody `replace()` :

```python
>>> help("".replace)
Help on built-in function replace:

replace(...) method of builtins.str instance
    S.replace(old, new[, count]) -> str

    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.
```

Dokumentacja dla metody `isdigit()` :

```python
>>> help("".isdigit)
Help on built-in function isdigit:

isdigit(...) method of builtins.str instance
    S.isdigit() -> bool

    Return True if all characters in S are digits
    and there is at least one character in S, False otherwise.
```
----

Pamiętajmy, że funkcja input **zawsze** zwraca wartość typu `String`- nawet, jeśli wpiszemy cyfrę. Zatem musimy zadbać o konwersję (zmianę) typu, służą do tego celu funkcje:

* `int()`- zamienia na wartość liczby całkowitej
* `float()`- zamienia na wartość liczby zmiennoprzecinkowej

Liczbę zmiennoprzecinkową zapisujemy ze znakiem kropki rozdzielającej część całkowitą od ułamkowej, np. `3.14`.
