def extrema(liste):
    mini = liste[0]
    maxi = liste[0]
    for i in range(len(liste)):
        for j in range(len(liste)):
            if i != j:
                if liste[j] >= liste[i] and liste[j] >= maxi:
                    maxi = liste[j]
                elif liste[j] < liste[i] and liste[i] <= mini:
                    mini = liste[j]
    return [mini, maxi]

def moyenne_sans_extrema(liste):
    extremas = extrema(liste)
    new_liste = [x for x in liste if x not in extremas]
    moyenne = sum(new_liste)/len(new_liste)
    return moyenne

def extrema_v2(liste):
    mini = liste[0]
    maxi = liste[0]
    for i in range(len(liste)):
        for j in range(len(liste)):
            if j != i:
                tmp = [liste[i], liste[j]]
                tmp.sort()
                if tmp[0] < mini:
                    mini = tmp[0]
                if tmp[1] > maxi:
                    maxi = tmp[1]
    return [mini, maxi]

def somme_prefixes(liste):
    somme = [sum(liste[:i+1]) for i in range(len(liste))]
    return somme

def moyenne_ponderee(notes, coeffs):
    moyenne = 0
    for note,coeff in zip(notes, coeffs):
        moyenne += note * coeff
    moyenne /= sum(coeffs)
    return moyenne

def prefixes(chaine):
    prefixes = [chaine[:i] for i in range(len(chaine) + 1)]
    return prefixes

def suffixes(chaine):
    suffixes = [chaine[i:] for i in reversed(range(len(chaine) + 1))]
    return suffixes

def facteurs(chaine):
    facteurs = [chaine[i:j] for i in range(len(chaine))
                            for j in range(i+1, len(chaine)+1)]
    return ['']+facteurs

import random

def melange(n):
    a_vider = list(range(n))
    liste_melangee = []
    while len(a_vider) > 0:
        elem = random.choice(a_vider)
        liste_melangee.append(elem)
        a_vider.remove(elem)
    return liste_melangee 

def gather(valeurs, indices):
    liste = []
    for index in indices:
        liste.append(valeurs[index])
    return liste

def liste_melangee(liste):
    indices = melange(len(liste))
    return gather(liste, indices)

def range_a_trous(maximum, absents):
    return [x for x in range(maximum) if x not in absents]

def decoupage(c, s):
    return s.split(c)

