# Moduł Turtle to żółw w środowisku Python

Moduł Turtle napisany przy użyciu biblioteki Tkinter i umożliwia pisanie programów wykorzystujących ideę grafiki Logo, gdzie każdy może zobaczyć efekty działania swoich procedur. Standardowy zestaw poleceń pozwala na rozwiązywanie zarówno prostych, jak i trudniejszych zadań. Polecenia  języka Python oraz komendy dla żółwia wpisujemy w języku angielskim, co  może być traktowane jako zaleta lub wada.

| Polecenie | Tłumaczenie            | Wyjaśnienie                                                  |
| --------- | ---------------------- | ------------------------------------------------------------ |
| fd(n)     | forward – naprzód      | Przesuwa żółwia w aktualnym kierunku o n kroków. W zależności  od stanu pisaka żółw rysuje kreskę (pisak opuszczony) lub nie rysuje  (pisak podniesiony). |
| bk(n)     | backward – wstecz      | Przesuwa żółwia przeciwnie do aktualnego kierunku o n kroków. W zależności od stanu pisaka żółw rysuje kreskę (pisak opuszczony) lub  nie rysuje (pisak podniesiony). |
| rt(alfa)  | right – prawo          | Obraca żółwia w prawo o kąt alfa.                            |
| lt(alfa)  | left – lewo            | Obraca żółwia w lewo o kąt alfa.                             |
| pu()      | pen up – podnieś pisak | Żółw podnosi pisak – nie rysuje podczas przemieszczania się. |
| pd()      | pen down – opuść pisak | Żółw opuszcza pisak – rysuje podczas przemieszczania się.    |

----

Pamiętamy, że słowo kluczowe `import` powoduje wczytanie do Pythona zewnętrznych funkcji.


Pętla `for` pozwala *iterować* po elementach kolekcji, np. listy.