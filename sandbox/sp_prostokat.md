# W Pythonie możemy pobierać od użytkownika dane

Możemy za pomocą funkcji `input` pobierać od użytkownika dane z klawiatury. Poniżej opis funkcji:

```python
>>> help(input)
Help on built-in function input in module builtins:

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.	
```

Pamiętajmy, że funkcja input **zawsze** zwraca wartość typu `String`- nawet, jeśli wpiszemy cyfrę. Zatem musimy zadbać o konwersję (zmianę) typu, służą do tego celu funkcje:

* `int()`- zamienia na wartość liczby całkowitej
* `float()`- zamienia na wartość liczby zmiennoprzecinkowej

Liczbę zmiennoprzecinkową zapisujemy ze znakiem kropki rozdzielającej część całkowitą od ułamkowej, np. `3.14`.
