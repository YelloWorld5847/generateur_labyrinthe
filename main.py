import pygame
import random
import pyautogui
import time
start = True


width, height = pyautogui.size()
print(width)
print(height)



# Définir les couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)

# Dimensions des carrés
TAILLE_CARRE = 40

# Position des carrés
POSITION_NOIR = (5, 5)
POSITION_BLANC = (150, 50)

# Dimensions du Labyrinthe
TAILLE_GRILLE = 9

if TAILLE_GRILLE % 2 == 0:
    print("--- ATENTION TAILLE DE LA GRILLE INVALIDE ---")
    TAILLE_GRILLE += 1
    print(f"La taille de la grille a été corrigée pour : {TAILLE_GRILLE} car elle ne doit pas être paire ")

# Distance de marge entre la fenetre et la grille
ESPACEMENT = 20

# Configuration de la fenêtre
LARGEUR_FENETRE = TAILLE_GRILLE * TAILLE_CARRE + ESPACEMENT * 2
HAUTEUR_FENETRE = TAILLE_GRILLE * TAILLE_CARRE + ESPACEMENT * 2
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


chemin_test = {
    1: {
        "x": 0,
        "y": 0,
        "color": (0, 0, 0),
        "id": 1,
        "valide": 0
    },
    2: {
        "x": 1,
        "y": 0,
        "color": (0, 0, 0),
        "id": 2,
        "valide": 3
    },
    3: {
        "x": 2,
        "y": 0,
        "color": (0, 0, 0),
        "id": 2,
        "valide": 2
    }
}

chemin = {}

element = 0

def grid():
    x_ = 0
    def colonne1(x, num_grid):
        nonlocal x_
        global element

        y_ = 0

        if num_grid == 1:
            for y in range(TAILLE_GRILLE):
                pygame.draw.rect(screen, NOIR, (x * TAILLE_CARRE + ESPACEMENT, y * TAILLE_CARRE + ESPACEMENT, TAILLE_CARRE, TAILLE_CARRE))
        else:
            for y in range(TAILLE_GRILLE):
                if y % 2 == 0:
                    color = NOIR
                else:
                    element += 1
                    print(f"elemnt = {element}")
                    aleatoir = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                    color = aleatoir
                    print(f"x : {x_} ; y : {y_}")
                    print(f"couleur aléatoir = {color}")
                    chemin[element] = {"x": x_, "y": y_, "color": color, "id": element, "valide": 0}
                    print(f"**********  {x_ * 2 + 1} = {x}  ***************")
                    y_ += 1

                pygame.draw.rect(screen, color, (x * TAILLE_CARRE + ESPACEMENT, y * TAILLE_CARRE + ESPACEMENT, TAILLE_CARRE, TAILLE_CARRE))
        pygame.display.flip()

    for x in range(TAILLE_GRILLE):
        if x % 2 == 0:
            colonne1(x, 1)
        else:
            colonne1(x, 2)
            x_ += 1
    for num, x_y_color_id in chemin.items():
        print(f"id = {num}")
        print(f"x = {x_y_color_id["x"]}; y = {x_y_color_id["y"]}; couleur = {x_y_color_id["color"]}; id = {x_y_color_id["id"]}; valide = {x_y_color_id["valide"]}")
        print(" ")

    pygame.display.flip()

def generer():
    liste = [1,2,3,4,16,12]
    liste_direct = [3,3,3,2,4,4]
    for i in range(len(liste)):
        print(f"-----elemnt = {element}")
        #position_aleatoir = random.randint(1, element)
        position_aleatoir = liste[i]
        print(position_aleatoir)
        x, y, color, id, valide = chemin[position_aleatoir].values()
        print("chemin de x :", chemin[position_aleatoir]["x"])
        print(f"{x}; {y}; {color}; {id}")

        num1 = chemin[position_aleatoir]["id"]
        print(f"num1 = {num1}")
        # 1 haut | 2 droite | 3 bas | 4 gauche
        possibiliter = [1, 2, 3, 4]

        if x == 0:
            possibiliter.remove(4)
        elif x == (TAILLE_GRILLE - 1) / 2 - 1:
            possibiliter.remove(2)

        if y == 0:
            possibiliter.remove(1)
        elif y == (TAILLE_GRILLE - 1) / 2 - 1:
            possibiliter.remove(3)

        print(f"possibiliter : {possibiliter}")

        direction = liste_direct[i]  #random.choice(possibiliter)

        print(f"direction = {direction}")

        position_x = 0
        position_y = 0

        match direction:
            case 1:
                position_x = 0
                position_y = -1
            case 2:
                position_x = 1
                position_y = 0
            case 3:
                position_x = 0
                position_y = 1
            case 4:
                position_x = -1
                position_y = 0

        x2 = x + position_x
        y2 = y + position_y

        print("\n")
        print("chemin :")
        for num, x_y_color_id in chemin.items():
            print(f"id = {num}")
            print(f"x = {x_y_color_id["x"]}; y = {x_y_color_id["y"]}; couleur = {x_y_color_id["color"]}; id = {x_y_color_id["id"]}; valide = {x_y_color_id["valide"]}")

        print(f"x2 : {x2} ; y2 : {y2}")

        num2 = None

        # Récupérer un numéro par raport à ses coordonner
        for numero, coordonnees in chemin.items():
            if coordonnees["x"] == x2 and coordonnees["y"] == y2:
                num2_element = numero
                num2 = coordonnees["id"]
                color2 = coordonnees["color"]
                break


        if num2 == None:
            print("\n--------------erreur-----------------\n")
            return False

        elif num1 != num2:
            x_1 = x * 2 + 1
            y_1 = y * 2 + 1

            x_2 = x2 * 2 + 1
            y_2 = y2 * 2 + 1

            x_3 = (x_1 + x_2) / 2
            y_3 = (y_1 + y_2) / 2

            #chemin[num2_element]["color"] = color
            #chemin[num2_element]["id"] = num1
            chemin[num2_element]["valide"] += 1
            chemin[position_aleatoir]["valide"] += 1
            print(f"position_1 = {position_aleatoir} ; position_2 = {num2_element}")
            print(f"id_1 = {num1} ; id_2 = {num2}")
            print(f"id de 1er carré : {chemin[position_aleatoir]["id"]}")

            time.sleep(2)
            print("\n \n")
            pygame.draw.rect(screen, color, (x_3 * TAILLE_CARRE + ESPACEMENT, y_3 * TAILLE_CARRE + ESPACEMENT, TAILLE_CARRE, TAILLE_CARRE))

            if chemin[position_aleatoir]["valide"] >= chemin[num2_element]["valide"]:
                pygame.draw.rect(screen, color, (x_2 * TAILLE_CARRE + ESPACEMENT, y_2 * TAILLE_CARRE + ESPACEMENT, TAILLE_CARRE, TAILLE_CARRE))
                # Parcourir le dictionnaire et afficher les coordonnées des éléments avec id selectionner
                for key, value in chemin.items():
                    if value['id'] == chemin[position_aleatoir]["id"]:
                        x_deja_valide = value['x'] * 2 + 1
                        y_deja_valide = value['y'] * 2 + 1
                        value["color"] = color
                        chemin[num2_element]["id"] = num1
                        pygame.draw.rect(screen, color, (
                        x_deja_valide * TAILLE_CARRE + ESPACEMENT, y_deja_valide * TAILLE_CARRE + ESPACEMENT, TAILLE_CARRE, TAILLE_CARRE))
                        print(f"Élément {key} a les coordonnées x: {value['x']}, y: {value['y']}")
            else:
                for key, value in chemin.items():
                    if value['id'] == chemin[num2_element]["id"]:
                        x_deja_valide = value['x'] * 2 + 1
                        y_deja_valide = value['y'] * 2 + 1
                        value["color"] = color2
                        chemin[position_aleatoir]["id"] = num2
                        pygame.draw.rect(screen, color, (
                        x_deja_valide * TAILLE_CARRE + ESPACEMENT, y_deja_valide * TAILLE_CARRE + ESPACEMENT, TAILLE_CARRE, TAILLE_CARRE))
                        print(f"Élément {key} a les coordonnées x: {value['x']}, y: {value['y']}")

                pygame.draw.rect(screen, color2, (x_1 * TAILLE_CARRE + ESPACEMENT, y_1 * TAILLE_CARRE + ESPACEMENT, TAILLE_CARRE, TAILLE_CARRE))



            pygame.display.flip()


    return True


    #carre2 = random.choice()


def main():
    # Remplir l'écran avec une couleur de fond (facultatif)
    screen.fill((250, 250, 250))

    grid()
    print(f"-élément : {element}-")

    running = generer()
    # Boucle principale

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        # Dessiner les carrés
        #pygame.draw.rect(screen, NOIR, (*POSITION_NOIR, TAILLE_CARRE, TAILLE_CARRE))
        #pygame.draw.rect(screen, BLANC, (*POSITION_BLANC, TAILLE_CARRE, TAILLE_CARRE))

        # Mettre à jour l'affichage
        pygame.display.flip()
    # Quitter Pygame
    pygame.quit()

if start:
    # Initialisation de Pygame
    pygame.init()

    screen = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
    pygame.display.set_caption("Affichage de Carrés")
    main()


