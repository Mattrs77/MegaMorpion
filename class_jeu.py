import fltk as fl
import mega_morpion as mp
import creat_bouton as cb

class Jeu:

    def __init__(self):
        self.joueur = ["X", "O"]


    def jeu(self):
        fl.cree_fenetre(800, 800)
        fl.efface_tout()
        princ = True
        while princ:
            fl.efface('morpion')
            j = 0
            morpion = mp.Megamorpion((100, 100, 600, 600))
            morpion.affiche()
            jeu = True
            while jeu:
                ev = fl.donne_ev()
                tev = fl.type_ev(ev)
                if tev == 'Touche': 
                    jeu = False
                    princ = False
                elif tev == 'Quitte':
                    jeu = False
                elif tev == 'ClicGauche':
                    changement_j = morpion.clic(self.joueur[j], {'ab' : fl.abscisse_souris(),'or' : fl.ordonnee_souris()})
                    if changement_j != None:
                        j += changement_j
                    j = j%2
                    fl.efface('morpion')
                    morpion.affiche()
                    morpion.check_win()
                fl.mise_a_jour()
        fl.ferme_fenetre()

    def menu(self):
        larg = 800
        haut = 800
        liste_boutons = []
        liste_boutons.append(cb.Boutons)
        fl.cree_fenetre(larg, haut)
