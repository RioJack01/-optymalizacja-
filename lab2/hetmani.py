# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 21:59:20 2017
@author: Mateusz
"""

def variable(i, j):
    '''Funkcja tworzaca zmienna znakowa
    o zadanych subskryptach i, j.'''
    result = "x"
    result += str(i)
    result += "."
    result += str(j)
    return result

def hetmani(n):
    '''Metaprogram tworzacy rozwiazanie problemu hetmanow
    na szachownicy o wymiarach n x n.'''
    result = "Maximize \nobj: "
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += variable(i, j)
            if(not(i == n and j == n)):
                result += " + "
            else:
                result += "\n"
    #Warunki w wiersze
    result += "Subject to \n"
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += variable(i, j)
            if(not(j == n)):
                result += " + "
            else:
                result += " <= 1\n"
    #Warunki w kolumny
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += variable(j, i)
            if(not(j == n)):
                result += " + "
            else:
                result += " <= 1\n"  
    #Warunki na przekatne
    k = 0
    for i in range(-n + 1, n):
        k += 1
        if (i <= 0):
            for j in range(1, k + 1):
                result += variable(j, j - i)
                if (j != k):    
                    result += " + "
        else:
            for j in range(i + 1, n + 1):
                result += variable(j, j - i)
                if (j != n):
                    result += " + "  
        result += " <= 1\n"
    #Warunki na antyprzekatne
    for i in range(2, 2 * n + 1):
        if (i <= n + 1):
            for j in range(1, i):
                result += variable(j, i - j)
                if (j != i - 1):    
                    result += " + "
        else:
            for j in range(i - n, n + 1):
                if (i - j >= 1):
                    result += variable(j, i - j)
                    if (i - j != i - n):
                        result += " + "  
        result += " <= 1\n"
    #Warunki na wartosci
    result += "Bounds \n"
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += "0 <= "
            result += variable(i, j)
            result += " <= 1\n"
    #nazwy zmiennych
    result += "Generals \n"
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += variable(i, j)
            result += "\n"
    result += "End"
    return result

n = int(input("Podaj rozmiar szachownicy: "), 10)
print(hetmani(n))
