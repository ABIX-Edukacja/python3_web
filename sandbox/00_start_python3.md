# Pusty plik.

W tym miejscu możesz spokojnie testować dowolne swoje projekty. Pamiętajmy o najważniejszych zasadach:

* Python rozróżnia małe i DUŻE litery
* nazwy zmiannych zapisujemy z małych liter i używamy znaków podkreślenia, np: `zmienna_1` lub `pole_powierzchni`
* bloki kodu oznaczamy jako 4 spacje (edytor ACE wspomaga nas w tym)
* znaki dwukropka oznaczają, że nastąpi blok kodu, np. dla definicji funkcji, instrukcji warunkowej, pętli

----
## Python – interpretowany język programowania

Języki interpretowane ułatwiają pisanie aplikacji przenośnych, zgodnych z wieloma platformami sprzętowymi i systemowymi. Programy takie mają często postać kodu źródłowego, który jest
uruchamiany za pośrednictwem interpretera. Dla odmiany, programy kompilowane są zamieniane z zapisu w kodzie źródłowym na kod maszynowy. Jest on specyﬁczny dla konkretnego systemu
operacyjnego oraz sprzętu (dotyczy to zwłaszcza procesorów).

**Python to język programowania ogólnego przeznaczenia**, jego składnia jest zbliżona do naturalnego języka. Jest często używany jako język skryptowy (gdzie wykonywany program jest w wersji źródłowej) i uruchamiany na serwerach. Python jest dostępny na wiele systemów operacyjnych; często wykorzystywany jest w urządzeniach gromadzących i przetwarzających dane, jak np. inteligentny budynek czy stacje pogodowe.

----

Zawsze możemy pobrać i zainstalować lokalnie Pythona i w środowisku IDLE sprawdzić szybką pomoc, np.:

```python
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```