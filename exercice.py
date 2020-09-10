#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    dist_entre_lettre_min_maj = ord('a') - ord('A')
    for lettre in mot:
        if ord
        lettre=chr(ord(lettre)- dist_entre_lettre_min_maj)
        

        # TODO completer la fonction ici
        
        resultat += lettre
    return resultat


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
