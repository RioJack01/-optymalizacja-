Rozwiązanie Pracy Domowej nr 5. Autorzy: Mateusz Doliński, Katarzyna Głowacka, Michał Kozyra

Definiujemy macierz kwadratową "graf" o wymiarach 7x7 przedstawiającą zero-jedynkowo połączenia w grafie dwudzielnym z zad.1, gdzie i-ty wiersz oznacza możliwe krawędzie łączące i-ty wierzchołek z wiersza górnego z kolejnymi punktami wiersza dolnego.

Dla grafu zadanego w zad.1 i krawędziach o wadze 1 generujemy program liniowy skojarzenia maksymalnego - u nas tzw. "problem bazowy".

Następnie tworzymy "problem dualny" do wcześniej postawionego zadania. Generujemy go osobno - ze względu na użycie klasy Mixed Integer Problems nie możemy użyć "szybszej" opcji P.dual() dla P = InteractiveLPProblem(...).

Rozwiązanie programu dualnego jest pokryciem wierzchołkowym.

Uzyskujemy optymalne rozwiązania dla problemu bazowego i problemu dualnego:

7.0 {(5, 4): 0.0, (1, 3): 1.0, (5, 5): 1.0, (6, 6): 0.0, (3, 0): 0.0, (4, 6): 0.0, (2, 1): 0.0, (0, 2): 0.0, (0, 0): 0.0, (0, 5): 1.0, (3, 6): 0.0, (2, 2): 0.0, (6, 2): 1.0, (5, 1): 0.0, (1, 0): 0.0, (4, 1): 1.0, (2, 4): 1.0, (3, 3): 1.0}

7.0 {(1, 2): 1.0, (0, 1): 0.0, (0, 0): 0.0, (1, 5): 1.0, (1, 4): 1.0, (0, 2): 0.0, (0, 6): 0.0, (1, 3): 1.0, (1, 6): 1.0, (0, 4): 0.0, (0, 5): 0.0, (1, 0): 1.0, (0, 3): 0.0, (1, 1): 1.0}
