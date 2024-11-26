from player import Player
from labyrinthe import Creer_labyrint
class Game:

    def __init__(self, NOIR, BLANC, VITESSE, TAILLE_GRILLE, ESPACEMENT, TAILLE_CARRE, TAILLE_GRILLE_HAUTEUR,
                 TAILLE_GRILLE_LARGEUR, MOVE_PLAYER, PRINT, STOP):
        self.is_playing = False
        self.is_genere = False
        self.NOIR = NOIR
        self.BLANC = BLANC
        self.VITESSE = VITESSE
        self.TAILLE_GRILLE = TAILLE_GRILLE
        self.ESPACEMENT = ESPACEMENT
        self.TAILLE_CARRE = TAILLE_CARRE
        self.TAILLE_GRILLE_HAUTEUR = TAILLE_GRILLE_HAUTEUR
        self.TAILLE_GRILLE_LARGEUR = TAILLE_GRILLE_LARGEUR
        self.MOVE_PLAYER = MOVE_PLAYER
        self.PRINT = PRINT
        self.STOP = STOP


    def update(self, screen):
        self.creer_labyrint = Creer_labyrint(self.NOIR, self.BLANC, self.VITESSE, self.TAILLE_GRILLE, self.ESPACEMENT,
                                             self.TAILLE_CARRE, self.TAILLE_GRILLE_HAUTEUR, self.TAILLE_GRILLE_LARGEUR,
                                             self.MOVE_PLAYER, self.PRINT,self.STOP, screen)

        # Remplir l'écran avec une couleur de fond (facultatif)
        screen.fill(self.BLANC)

        self.creer_labyrint.grid()

        self.entrer = self.creer_labyrint.entrer
        self.sorti = self.creer_labyrint.sorti

        # print(f"-élément : {element}-")

        self.running = self.creer_labyrint.generer()

        self.creer_labyrint.trouver_mur()

        self.chemin = self.creer_labyrint.chemin

        self.entrer_y = self.entrer * self.TAILLE_CARRE + self.ESPACEMENT

        self.player = Player(self.entrer_y, self.TAILLE_CARRE, self.ESPACEMENT, self.MOVE_PLAYER)

        self.is_genere = False
        self.is_playing = True
        