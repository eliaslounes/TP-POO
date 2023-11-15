#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#exo2
import numpy as np

class Signal:
    def __init__(self, nombre_echantillons, vecteur_de_taille_nbr):
        self.nbr = nombre_echantillons
        self.tab = vecteur_de_taille_nbr

    def echantillons(self):
        return self.nbr

    def cal_moyenne(self):
        if self.nbr != 0:
            return sum(self.tab) / self.nbr
        else:
            print('erreur')
            return None

    def cal_correlation(self):
        if self.nbr <= 1:
            return None
        moy = self.cal_moyenne()
        somme_carres = sum((x - moy) ** 2 for x in self.tab)
        cor = somme_carres / (self.nbr - 1)
        return cor

    def display(self):
        print("Nombre d'échantillons :", self.nbr)
        print("Tableau :", self.tab)
        print("Moyenne:", self.cal_moyenne())
        print("Deuxième coefficient de corrélation:", self.cal_correlation())

class Aléatoire(Signal):
    def __init__(self, sigma, mean, nombre_echantillons, vecteur_de_taille_nbr):
        super().__init__(nombre_echantillons, vecteur_de_taille_nbr)
        self.sigma = sigma
        self.mean = mean

    def Init_Alea(self):
        if self.nbr <= 0:
            print("Le nombre d'échantillons doit être supérieur à zéro.")
            return
        self.tab = np.random.normal(loc=self.mean, scale=self.sigma, size=self.nbr)

    def correlation(self):
        puissance = sum(x ** 2 for x in self.tab)
        print("Puissance de tab:", puissance)
        print("Classe Aléatoire")
        return puissance

class Déterministe(Signal):
    def __init__(self, nombre_echantillons, amplitude):
        super().__init__(nombre_echantillons, [])
        self.amplitude = amplitude

    def valeurs(self):
        if self.nbr <= 0:
            print("Le nombre d'échantillons doit être supérieur à zéro.")
            return
        half_nbr = self.nbr // 2
        self.tab = [self.amplitude] * half_nbr + [-self.amplitude] * (self.nbr - half_nbr)
        
def Addition(objet_aleatoire, objet_deterministe):
    if objet_aleatoire.nbr != objet_deterministe.nbr:
        print("Les objets n'ont pas le même nombre d'échantillons.")
        return None
    objet_resultat = Déterministe(objet_aleatoire.nbr, 0)
    objet_resultat.tab = [a + b for a, b in zip(objet_aleatoire.tab, objet_deterministe.tab)]
    return objet_resultat

