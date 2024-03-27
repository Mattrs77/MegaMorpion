import fltk as fl
import fonction as fn

class Morpion:
            

    def __init__(self, x_g, y_h, x_d, y_b):
        self.tab = [[None for _ in range(3)] for _ in range(3)]
        self.gagnant = None
        self.co = (x_g, y_h, x_d, y_b)

    def init_co(self, x_g, y_h, x_d, y_b):
        self.co = (x_g, y_h, x_d, y_b)

    def affiche(self):
        if self.gagnant == None:
            x_t = ((self.co[2] - self.co[0]) / 3)
            y_t = ((self.co[3] - self.co[1]) / 3)
            for i in range(2):
                fl.ligne(self.co[0] + x_t * (i + 1), self.co[1], self.co[0] + x_t * (i + 1), self.co[3], tag='morpion')
                fl.ligne(self.co[0], self.co[1] + y_t * (i + 1) ,self.co[2], self.co[1] + y_t * (i + 1), tag='morpion')
            for i in range(len(self.tab)):
                for j in range(len(self.tab[i])):
                    if self.tab[i][j] != None:
                        
                        fl.texte(self.co[0] + x_t * i, self.co[1] + y_t * j, self.tab[i][j], tag='morpion')

    def clic(self, symb, co_s: dict):
        if self.gagnant == None:
            if self.co[0] < co_s['ab'] < self.co[2]:
                if self.co[1] < co_s['or'] < self.co[3]:
                    x_t = ((self.co[2] - self.co[0]) / 3)
                    y_t = ((self.co[3] - self.co[1]) / 3)
                    for i in range(len(self.tab)):
                        if (self.co[0] + x_t * i) < co_s['ab'] < (self.co[0] + x_t * (i + 1)):
                            for j in range(len(self.tab[i])):
                                if (self.co[1] + y_t * j) < co_s['or'] < (self.co[1] + y_t * (j + 1)):
                                    if self.tab[i][j] is None:
                                        self.tab[i][j] = symb
                                        self.check_win(symb)
                                        if self.gagnant != None:
                                            self.affiche_win()

                                        return 1, (j, i)
        return 0, None
        
    def check_win(self, symb):
        if fn.check_winner(self.tab):
            self.gagnant = symb

    def affiche_win(self):
        self.tab = self.gagnant
        fl.rectangle(self.co[0], self.co[1], self.co[2], self.co[3], 'white', 'white', tag='morpion_2')
        centre = (self.co[0] + ((self.co[2] - self.co[0])/ 2), self.co[1] + ((self.co[3] - self.co[1]) / 2))

        fl.texte(centre[0], centre[1], self.gagnant, ancrage='center', tag='morpion_2')