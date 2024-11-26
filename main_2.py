import pygame
import random
import pyautogui
import time
from player import Player
from game import Game

start = True

def nombre_pair(num, pair):
    print(f"nombre = {num}")
    modulo = num % pair
    print(f"modulo = {modulo}")
    if modulo != 0:
        if modulo >= pair / 2:
            print(f"1 : num {num - modulo + pair}")
            return num - modulo + pair
        else:
            print(f"2 : num {num - modulo}")
            return num - modulo
    else:
        print(f"3 : num : {num}")
        return num




def main():

    def rafrechir():

        screen.fill(BLANC)

        if game.is_playing:
            for value in chemin.values():
                pygame.draw.rect(screen, value["color"], (
                    value["x"] * TAILLE_CARRE + ESPACEMENT, value["y"] * TAILLE_CARRE + ESPACEMENT, TAILLE_CARRE,
                    TAILLE_CARRE))

            # appliquer l'image du joueur
            screen.blit(game.player.image, game.player.rect)


    def avancer_Y_or_N(direction_x, direction_y):
        player_x = (game.player.rect.x - ESPACEMENT) // TAILLE_CARRE
        player_y = (game.player.rect.y - ESPACEMENT) // TAILLE_CARRE
        #print(player_x, ",", player_y)
        for key, value in chemin.items():
            if value["x"] == player_x + direction_x and value["y"] == player_y + direction_y:
                if value["color"] == (NOIR):
                    '''---------------------------ici False----------------------------------------'''
                    return False
                elif value["color"] == (BLANC):
                    return True
                else:
                    print("----------------ERREUR----------------")
                    print(f"la couleur n'est ni blanche ni noire elle est : {value["color"]}")
                    return False

    '''creer_labyrint = Creer_labyrint()

    # Remplir l'écran avec une couleur de fond (facultatif)
    screen.fill(BLANC)

    creer_labyrint.grid()

    #print(f"-élément : {element}-")

    running = creer_labyrint.generer()

    creer_labyrint.trouver_mur()

    entrer_y = entrer * TAILLE_CARRE + ESPACEMENT

    player = Player(entrer_y, TAILLE_CARRE, ESPACEMENT, MOVE_PLAYER)'''

    game = Game(NOIR, BLANC, VITESSE, TAILLE_GRILLE, ESPACEMENT, TAILLE_CARRE, TAILLE_GRILLE_HAUTEUR, TAILLE_GRILLE_LARGEUR, MOVE_PLAYER, PRINT, STOP)




    running = True
    # Boucle principale
    while running:

        rafrechir()

        # vérifier si la jeu à commencer
        if game.is_genere:
            game.update(screen)
            chemin = game.chemin
        else:
            # ajouter la bannière
            # screen.blit(banner, (0, 0))
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game.is_genere = True
            '''
            elif event.type == pygame.KEYDOWN:
                # quelle touche à été utiliser ?
                if event.key == pygame.K_d:
                    if avancer_Y_or_N(1, 0):
                        for i in range(player.rep):
                            player.move_right()
                            time.sleep(time_player)
                            rafrechir()

                elif event.key == pygame.K_q:
                    if avancer_Y_or_N(-1, 0):
                        for i in range(player.rep):
                            player.move_left()
                            time.sleep(time_player)
                            rafrechir()
                elif event.key == pygame.K_z:
                    if avancer_Y_or_N(0, -1):
                        for i in range(player.rep):
                            player.move_up()
                            time.sleep(time_player)
                            rafrechir()
                elif event.key == pygame.K_DOWN or pygame.K_s:
                    if avancer_Y_or_N(0, 1):
                        for i in range(player.rep):
                            player.move_down()
                            time.sleep(time_player)
                            rafrechir()'''



        keys = pygame.key.get_pressed()
        if game.is_playing:
            if keys[pygame.K_LEFT]:
                if avancer_Y_or_N(-1, 0):
                    for i in range(game.player.rep):
                        game.player.move_left()
                        time.sleep(time_player)
                        rafrechir()
            elif keys[pygame.K_RIGHT]:
                if avancer_Y_or_N(1, 0):
                    for i in range(game.player.rep):
                        game.player.move_right()
                        time.sleep(time_player)
                        rafrechir()
            elif keys[pygame.K_UP]:
                if avancer_Y_or_N(0, -1):
                    for i in range(game.player.rep):
                        game.player.move_up()
                        time.sleep(time_player)
                        rafrechir()
            elif keys[pygame.K_DOWN]:
                if avancer_Y_or_N(0, 1):
                    for i in range(game.player.rep):
                        game.player.move_down()
                        time.sleep(time_player)
                        rafrechir()

        # Mettre à jour l'affichage
        pygame.display.flip()


        timer.tick(FPS)

    # Quitter Pygame
    pygame.quit()

if start:

    #  appuyé sur 's' pour commencer

    width, height = pyautogui.size()
    print(width)
    print(height)

    FPS = 60

    timer = pygame.time.Clock()

    # Définir les couleurs
    NOIR = (0, 0, 0)  # (200, 200, 200)
    BLANC = (150, 150, 150)

    # 1 : le plus vite
    # 2 : mise à jour à chaqque trajet tracé
    # 3 : voir la colorisation 1 à 1
    # 4 : indication du carré remplacer
    # prend aussi toute les condition en dessous (sauf le 1)
    VITESSE = 4
    FULL_SCREEN = True
    STOP = False
    PRINT = False  # peut causer des problèmes si il est à True
    TAILLE_GRILLE = 10
    ESPACEMENT = 20
    TAILLE_CARRE = 100
    TAILLE_GRILLE_HAUTEUR = 10
    TAILLE_GRILLE_LARGEUR = 10
    time_player = 0.006

    if STOP:
        VITESSE = 4

    if FULL_SCREEN:
        if height <= width:
            TAILLE_CARRE = (height - (ESPACEMENT * 2) - 80) // TAILLE_GRILLE

        else:
            TAILLE_CARRE = (width - (ESPACEMENT * 2) - 80) // TAILLE_GRILLE

        TAILLE_GRILLE_HAUTEUR = (height - (ESPACEMENT * 2) - 120) // TAILLE_CARRE
        TAILLE_GRILLE_LARGEUR = (width - (ESPACEMENT * 2) - 80) // TAILLE_CARRE
        print(width, ",", height)
        LARGEUR_FENETRE = width
        HAUTEUR_FENETRE = height - 73
    else:
        LARGEUR_FENETRE = TAILLE_CARRE * TAILLE_GRILLE_LARGEUR + ESPACEMENT * 2
        HAUTEUR_FENETRE = TAILLE_CARRE * TAILLE_GRILLE_HAUTEUR + ESPACEMENT * 2

    MOVE_PLAYER = int(TAILLE_CARRE / 10)
    print(f"move playe not int {TAILLE_CARRE / 15}")
    print(f"TAILLE_CARRE = {TAILLE_CARRE}")
    if TAILLE_CARRE >= 70:
        MOVE_PLAYER = 4
    elif TAILLE_CARRE >= 50:
        MOVE_PLAYER = 3
    elif TAILLE_CARRE >= 30:
        MOVE_PLAYER = 2
    elif TAILLE_CARRE >= 15:
        MOVE_PLAYER = 1
    else:
        MOVE_PLAYER = 1


    if MOVE_PLAYER == 0:
        MOVE_PLAYER = 2



    TAILLE_CARRE = nombre_pair(TAILLE_CARRE, MOVE_PLAYER)
    print(f"TAILLE CARRE : {TAILLE_CARRE}")
    # Configuration de la fenêtre

    print(LARGEUR_FENETRE)
    print(HAUTEUR_FENETRE)

    if HAUTEUR_FENETRE > height:
        print(f"la hauteur de la fenètre est trop grande de {HAUTEUR_FENETRE - height} pixel")
        print("veillez baisser la taille des carré ou le nombre de carré")
        start = False
    elif LARGEUR_FENETRE > width:
        print(f"la largeur de la fenètre est trop grande de {LARGEUR_FENETRE - width} pixel")
        print("veillez baisser la taille des carré ou le nombre de carré")
        start = False

    if TAILLE_GRILLE_HAUTEUR % 2 == 0:
        print("--- ATENTION TAILLE DE LA GRILLE INVALIDE ---")
        TAILLE_GRILLE_HAUTEUR += 1
        print(f"La taille de la grille a été corrigée pour : {TAILLE_GRILLE} car elle ne doit pas être paire ")

    if TAILLE_GRILLE_LARGEUR % 2 == 0:
        print("--- ATENTION TAILLE DE LA GRILLE INVALIDE ---")
        TAILLE_GRILLE_LARGEUR += 1
        print(f"La taille de la grille a été corrigée pour : {TAILLE_GRILLE} car elle ne doit pas être paire ")

    chemin = {}




    if start:
        # Initialisation de Pygame
        pygame.init()

        screen = pygame.display.set_mode((width, height - 73))
        pygame.display.set_caption("labyrinthe game")

        banner = pygame.image.load('image/labyrinthe_game.png')

        # Obtenir les dimensions de l'image
        largeur_image, hauteur_image = banner.get_size()

        # Calculer les nouvelles dimensions pour que l'image soit 4 fois plus petite que la fenêtre
        nouvelle_largeur = LARGEUR_FENETRE // 100
        nouvelle_hauteur = LARGEUR_FENETRE // 100

        # Calculer le facteur de redimensionnement pour conserver le rapport d'aspect
        facteur_redimensionnement = min(nouvelle_largeur / largeur_image, nouvelle_hauteur / hauteur_image)
        # Calculer les dimensions finales de l'image redimensionnée
        dimensions_finales = (int(largeur_image * facteur_redimensionnement), int(hauteur_image * facteur_redimensionnement))
        print(dimensions_finales)
        #banner = pygame.transform.scale(banner, dimensions_finales)

        main()


