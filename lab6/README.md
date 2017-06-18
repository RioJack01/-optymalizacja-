Rozwiązanie Pracy Domowej nr 3. Autorzy: Mateusz Doliński, Katarzyna Głowacka, Michał Kozyra

Jest to funkcja generująca program pomocniczy dla algorytmu simplex, jeżeli punkt (0,...,0) nie jest dopuszczalnym rozwiązaniem oryginalnego programu. W przeciwnym wypadku program zwraca problem oryginalny. Program napisany w języku Sage z dodatkiem bibliotek NumPy oraz Itertools.

Wejście: użytkownik proszony jest o podanie liczby zmiennych, następnie liczby ograniczeń, współczynników kolejnych równań, wartości równań po prawej stronie oraz współczynników funkcji celu. Wymagane jest, aby wszystkie nierówności były w stronę: "<=".

Wyjście: na konsoli zostanie wypisany problem pomocniczy albo informacja o braku konieczności rozważania takowego. W takim przypadku zwracany jest problem oryginalny w postaci macierzowej.

Dla danych z zadania 4 z lab 3:

Maksymalizuj x1+x2
przy ograniczeniach
x1+4x2?1,
7x1+3x2?-1,
-6x1+3x2?1,

otrzymujemy:

max -x8 -x9 -x10 x1 -x2 +4x3 -4x4 +x5 +x8 <=4 7x1 -7x2 +3x3 - 3x4 +x6 +x9 <=-1 -6x1 +6x2 +3x3 -3x4 +x7 +x10 <=1 x_i >=0

Uwaga: zmienne z problemu nie pokrywają się ze zmiennymi z rozwiązania. x1 oraz x2 z rozwaiązania to odpowiednia cześć dodatnia i ujemna x1 z problemu.
