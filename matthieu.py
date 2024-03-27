from fltk import *
from random import *
from ntelombila import *
from florian import *


def affichage(liste_image, taille_case):
    """
    Prend en argument la matrice des cartes, et la taille des cases du plateau,
    puis les afficher en fonction de leur position dans la matrice.
    """
    # première boucle pour les lignes des cartes
    for lig in range(len(liste_image)):
        # deuxième boucles pour les colonnes des cartes
        for col in range(len(liste_image[lig])):
            #si la position est une cartes, alors l'affiche
            if liste_image[lig][col] != 0:
                x = (col * taille_case) + (0.5 * taille_case) + (2 * taille_case) # Calcul des coordonnées x en fonction de la taille de la case
                y = (lig * taille_case) + (0.5 * taille_case) + (3 * taille_case) # Calcul des coordonnées y en fonction de la taille de la case
                image(x, y, 
                      f'cartes/{liste_image[lig][col]}.ppm', 
                      largeur=taille_case, 
                      hauteur=taille_case, 
                      tag=f'{liste_image[lig][col]},{lig},{col}')
                

def quadrillage(x, y, taille_case):
    """
    Fonction permettant d'afficher un quadrillage pour mieux 
    visualiser les cases du plateau de jeu, sert essentiellement à la programation du jeu.
    """
    for i in range(1,x):
        ligne(i * taille_case, 0, i * taille_case, y * taille_case, couleur = 'blue')
        ligne(0, i * taille_case, x * taille_case, i * taille_case, couleur = 'blue')
                

def supprime(liste_sup):
    """
    Prend en argument une liste, et efface l'image des cartes de la liste grâce au nom de celle-ci.
    """
    for i in range(len(liste_sup)):
        efface(f'{liste_sup[i]}')


def board_score(coo, color):
    """
    Permet d'afficher un rectangle en fonction des coordonnées,
    mais pourrait être retiré.
    """
    rectangle(coo[0],coo[1],coo[2],coo[3], remplissage=color)


def tube(x, y, name_tage, inside = 'white'):
    """
    fonction recenvant en paramètre de coordonnées, et affiche
    un tube à ces coordonnées. Il prend également en paramètre une couleur pour le tube.
    """
    cercle(x, y, 15, couleur = inside , remplissage = inside, tag = name_tage)
    cercle(x + 70, y, 15, couleur = inside , remplissage = inside, tag = name_tage)
    rectangle(x, y - 15, x + 70, y + 15, couleur = inside, remplissage = inside, tag = name_tage)


def score(x, y, score, color, name = 'SCORE', inside = 'white'):
    """
    Fonction recevant en paramètre des coordonnées, et le score.
    Affiche ensuite un tube pour afficher clairement le score ainsi que le nom
    au dessus de celui-ci.
    """
    efface(f'{name}')
    efface(name)
    tube(x, y, f'{name}', inside)
    chaine=name
    police='Courier'
    taille=20
    texte(x + 35, y - 35, chaine, police = police, 
          taille = taille, couleur = inside, ancrage = 'center', tag = f'{name}')
    chaine=score
    texte(x + 35, y ,chaine, police = police, 
          taille = taille, couleur = color, ancrage = 'center', tag = f'{name}')


def temps(x, y, minutes, secondes, color, inside = 'white'):
    """
    Fonction recevant en paramètre des coordonnées, et le temps.
    Affiche ensuite un tube pour afficher clairement le temps ainsi que le nom
    au dessus de celui-ci.
    """
    efface('tt')
    efface('temps')
    efface('dure')
    tube(x, y, 'tt', inside)
    chaine = 'TEMPS'
    police = 'Courier'
    taille = 15
    texte(x + 35, y - 35, chaine, police = police,
          taille = taille, couleur = inside, ancrage = 'center', tag = 'temps')
    texte(x + 35, y, f'{minutes} : {secondes}', police = police,
          taille = taille, couleur = color, ancrage = 'center', tag = 'dure')


def verif_clic(etat, taille_case):
    """
    Fonction recenvant en paramètres l'état du clic,
    puis affiche si le joueur a déjà un clic d'activer ou non.
    """
    #rectangle(17 * taille_case, 0, 20 * taille_case, 2 * taille_case, couleur="black", remplissage='black')
    efface('verif')
    if etat is False:  # Le joueur n'a pas cliqué 
        text = 'cliqué sur\n une carte'
    else:  # Le joueur a cliqué
        text = 'cliqué sur\n une paire'
    texte(18.5 * taille_case, taille_case, text, police = 'Courier', taille = 15,
          couleur = 'white', ancrage = 'center', tag = 'verif')


def bouton(coo, text, color, taille_case):
    """
    Prend en paramètres des coordonnées, un texte, une couleur
    et affiche un rectangle avec le texte demandé à l'intérieur.
    """
    efface(f'{text}')
    x1, y1, x2, y2 = coo[0],coo[1],coo[2],coo[3]
    rectangle(x1 + 1, y1, x2 - 1, y2, couleur = 'white', remplissage = color, tag = f'{text}')
    texte(x1 + 90, y1 + 30, text, 
          police = 'Courier', taille = int(taille_case * 0.25),
          couleur = 'white', ancrage = 'center', tag = f'{text}')
    

def lire_meilleur_score(nom_fichier):
    """
    Fonction prenant en paramètres le nom d'un fichier,
    et renvoie le nombre qu'il y a à l'intérieur.
    """
    try:
        with open(nom_fichier, 'r') as fichier:
            meilleur_score = int(fichier.read())
    except FileNotFoundError:
        # Si le fichier n'existe pas, renvoyez un score initial de 0
        meilleur_score = 0
    return meilleur_score


def enregistrer_meilleur_score(nouveau_score, nom_fichier):
    """
    Fonction prenant en paramètres un nouveau score, et l'enregistre dans
    le fichier.
    """
    with open(nom_fichier, 'w') as fichier:
        fichier.write(str(nouveau_score))
