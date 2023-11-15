#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class employé:
    def __init__(self, nom, id, point_indiciaire=500):
        self.nom = nom
        self.id = id
        self.pin = point_indiciaire

    def prime(self, a):
        if a:
            self.prime = self.pin * 2
        else:
            self.prime = self.pin * 0.5
        return self.prime

    def salaire(self):
        return self.pin * self.prime

    def affichage(self, a):
        prime = self.prime(a)
        salaire = self.salaire()
        print('---------------------------------')
        print('\033[92mLes informations de l\'employé:\033[0m')
        print('---------------------------------')
        print('Nom:', self.nom)
        print('ID:', self.id)
        print('Point indiciaire:', self.pin)
        print('Salaire:', salaire)
        print('Statut : Employé')

class ingenieur(employé):
    def __init__(self, etat, nom, id, point_indiciaire=500 ):
        self.etat = etat
        super().__init__(nom, id, point_indiciaire)
        if self.etat == 'titulaire':
            self.pin = self.pin * 6
        elif self.etat == 'stagiaire':
            self.pin = self.pin * 4
        else:
            print('Il y a une erreur')

    def affichage(self, a):
        if self.etat== 'titulaire' or self.etat=='stagiaire':
            prime = self.prime(a)
            salaire = self.salaire()
            print('---------------------------------')
            print('\033[92mLes informations de l\'ingénieur:\033[0m')
            print('---------------------------------')
            print('etat:', self.etat)
            print('Nom:', self.nom)
            print('ID:', self.id)
            print('Point indiciaire:', self.pin)
            print('Salaire:', salaire)
            print('Statut: ingenieur', self.etat)  
        else: 
            return
        
class technicien(employé):
    def __init__(self, etat, nom, id, point_indiciaire=500 ):
        self.etat = etat
        super().__init__(nom, id, point_indiciaire)
        if self.etat == 'titulaire':
            self.pin = self.pin * 6
        elif self.etat == 'stagiaire':
            self.pin = self.pin * 4
        else:
            print('Il y a une erreur')
        

    def affichage(self, a):
        if self.etat== 'titulaire' or self.etat=='stagiaire':
            prime = self.prime(a)
            salaire = self.salaire()*2
            print('---------------------------------')
            print('\033[92mLes informations du technicien:\033[0m')
            print('---------------------------------')
            print('etat:', self.etat)
            print('Nom:', self.nom)
            print('ID:', self.id)
            print('Point indiciaire:', self.pin)
            print('Salaire:', salaire)
            print('Statut: technicien', self.etat)  
        else: 
            return      

