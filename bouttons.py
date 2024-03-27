from fltk import *

class bouton:
    def __init__(self, x_g, x_d, y_h, y_b, name):
        self.x_gauche = x_g
        self.x_droit = x_d
        self.y_haut = y_h
        self.y_bas = y_b
        self.nom = name

    def clic(self, x_clic, y_clic):
        if self.x_gauche < x_clic < self.x_droit:
            if self.y_haut < y_clic < self.y_bas:
                return self.nom
            
    def affiche_bouton(self, largeur):
        u, v, w, x = self.x_gauche, self.y_haut, self.x_droit, self.y_bas
        rectangle(u, v, w, x, remplissage= 'white'
                , tag='pause')
        texte(largeur / 2.5 + 25, v + 10, f"{self.nom}",
              couleur="black", taille=20, police='Courier', tag = 'txt')