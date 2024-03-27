import morpion as mp
import fonction as fn
import fltk as fl

class Megamorpion:

    def __init__(self, co):
        self.plateau = [[mp.Morpion( None, None, None, None) for _ in range(3)] for _ in range(3)]
        self.co = co
        self.play = None


        x_t = ((self.co[2] - self.co[0]) / 3)
        y_t = ((self.co[3] - self.co[1]) / 3)
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i])):
                self.plateau[i][j].init_co(self.co[0] + x_t * i, self.co[1] + y_t * j, self.co[0] + x_t * (i + 1), self.co[1] + y_t * (j + 1))

    def affiche(self):

        x_t = ((self.co[2] - self.co[0]) / 3)
        y_t = ((self.co[3] - self.co[1]) / 3)
        for i in range(2):
            fl.ligne(self.co[0] + x_t * (i + 1), self.co[1], self.co[0] + x_t * (i + 1), self.co[3], couleur='red', epaisseur = 5, tag='morpion')
            fl.ligne(self.co[0], self.co[1] + y_t * (i + 1) ,self.co[2], self.co[1] + y_t * (i + 1), couleur='red', epaisseur = 5, tag='morpion')
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i])):
                self.plateau[i][j].affiche()

    def clic(self, symb, co_s: dict):
        if self.co[0] < co_s['or'] < self.co[2]:
            if self.co[1] < co_s['ab'] < self.co[3]:        
                x_t = ((self.co[2] - self.co[0]) / 3)
                y_t = ((self.co[3] - self.co[1]) / 3)
                for i in range(len(self.plateau)):
                    if (self.co[0] + x_t * i) < co_s['or'] < (self.co[0] + x_t * (i + 1)):
                        for j in range(len(self.plateau[i])):
                            if (self.co[1] + y_t * j) < co_s['ab'] < (self.co[1] + y_t * (j + 1)):
                                #rajoute si le joueur lui a obligé a joué la :
                                if self.play is None or (i, j) == self.play or self.plateau[self.play[1]][self.play[0]].gagnant != None:
                                    if self.plateau[j][i].gagnant is None:
                                        retour, self.play = self.plateau[j][i].clic(symb, co_s)
                                        return retour
                                return 0


    def check_win(self):
        plateau_f = []
        for i in range(len(self.plateau)):
            ligne = []
            for j in range(len(self.plateau[i])):
                ligne.append(self.plateau[i][j].gagnant)
            plateau_f.append(ligne)
        if fn.check_winner(plateau_f):
            print('Partie fini')