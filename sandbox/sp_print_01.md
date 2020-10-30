# podstawowe polecenie - wypisywanie na ekran

Aby wypisać cokolwiek na ekranie, stosujemy funkcję `print()`. Posiada ona dosyć rozbudowaną składnię:

```
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
  ```

W Pythonie od wersji 3.6 możemy stosować także F-String - to interesujący sposób zapisu. Zapoznajmy się z przykładem w linii 16.

Nas interesują dwa możliwe parametry: `sep` oraz `end`.
Odpowiednie przykłady znajdziemy w liniach:
* sep - linia 18
* end - linia 20
* razem sep + end - linia 23 
