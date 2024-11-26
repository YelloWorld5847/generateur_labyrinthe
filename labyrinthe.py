import random
import pygame
import time

class Creer_labyrint():

    def __init__(self, NOIR, BLANC, VITESSE, TAILLE_GRILLE, ESPACEMENT, TAILLE_CARRE, TAILLE_GRILLE_HAUTEUR,
                 TAILLE_GRILLE_LARGEUR, MOVE_PLAYER, PRINT,STOP, screen):
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
        self.screen = screen
        self.chemin = {}

        self.element = 0
        self.entrer, self.sorti = None, None

    def grid(self):
        def colonne1(x, num_grid):
            global element

            if num_grid == 1:
                for y in range(self.TAILLE_GRILLE_HAUTEUR):
                    pygame.draw.rect(self.screen, self.NOIR, (x * self.TAILLE_CARRE + self.ESPACEMENT, y * self.TAILLE_CARRE + self.ESPACEMENT, self.TAILLE_CARRE, self.TAILLE_CARRE))
            else:
                for y in range(self.TAILLE_GRILLE_HAUTEUR):
                    if y % 2 == 0:
                        color = self.NOIR
                    else:
                        self.element += 1

                        aleatoir = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                        color = aleatoir

                        self.chemin[self.element] = {"x": x, "y": y, "color": color, "id": self.element, "valide": 0}

                    if self.PRINT:
                        print(f"elemnt = {self.element}")
                        print(f"x : {x} ; y : {y}")

                    pygame.draw.rect(self.screen, color, (x * self.TAILLE_CARRE + self.ESPACEMENT, y * self.TAILLE_CARRE + self.ESPACEMENT, self.TAILLE_CARRE, self.TAILLE_CARRE))

        for x in range(self.TAILLE_GRILLE_LARGEUR):
            if x % 2 == 0:
                colonne1(x, 1)
            else:
                colonne1(x, 2)
            if self.VITESSE >= 4:
                pygame.display.flip()


        if self.PRINT:
            for num, x_y_color_id in self.chemin.items():
                print(f"id = {num}")
                print(f"x = {x_y_color_id["x"]}; y = {x_y_color_id["y"]}; couleur = {x_y_color_id["color"]}; id = {x_y_color_id["id"]}; valide = {x_y_color_id["valide"]}")
                print(" ")

        # créer une entrer et un sortie
        self.entrer = random.choice([i for i in range(1, self.TAILLE_GRILLE_HAUTEUR - 1) if i % 2 != 0])
        pygame.draw.rect(self.screen, self.BLANC, (
            0 * self.TAILLE_CARRE + self.ESPACEMENT, self.entrer * self.TAILLE_CARRE + self.ESPACEMENT,
            self.TAILLE_CARRE, self.TAILLE_CARRE))
        self.chemin[self.element + 10] = {"x": 0, "y": self.entrer, "color": self.BLANC, "id": 20000, "valide": 0}

        self.sorti = random.choice([i for i in range(1, self.TAILLE_GRILLE_HAUTEUR - 1) if i % 2 != 0])
        pygame.draw.rect(self.screen, self.BLANC, (
            (self.TAILLE_GRILLE_LARGEUR - 1) * self.TAILLE_CARRE + self.ESPACEMENT, self.sorti * self.TAILLE_CARRE + self.ESPACEMENT,
            self.TAILLE_CARRE, self.TAILLE_CARRE))
        self.chemin[self.element + 11] = {"x": (self.TAILLE_GRILLE_LARGEUR - 1), "y": self.sorti, "color": self.BLANC, "id": 20000, "valide": 0}

        pygame.display.flip()


    def generer(self):
        liste = [1,2,3,4,16,12]
        liste_direct = [3,3,3,2,4,4]
        carrer_noir_element = self.element + 100

        generating = True
        while generating:
            position_aleatoir = random.randint(1, self.element)
            if self.PRINT:
                print(" ")
                #position_aleatoir = liste[i]
                print(position_aleatoir)
                print("chemin de x :", self.chemin[position_aleatoir]["x"])
                print(f"{x}; {y}; {color}; {id}; {valide}")
                print(" ")
            x, y, color, id, valide = self.chemin[position_aleatoir].values()


            num1 = self.chemin[position_aleatoir]["id"]
            #print(f"num1 = {num1}")
            # 1 haut | 2 droite | 3 bas | 4 gauche
            possibiliter = [1, 2, 3, 4]

            if x == 1:
                possibiliter.remove(4)
            elif x == self.TAILLE_GRILLE_LARGEUR - 2:
                possibiliter.remove(2)

            if y == 1:
                possibiliter.remove(1)
            elif y == self.TAILLE_GRILLE_HAUTEUR - 2:
                possibiliter.remove(3)

            #print(f"possibiliter : {possibiliter}")

            direction = random.choice(possibiliter)  #liste_direct[i]

            if self.PRINT:
                print(f"direction = {direction}")

            position_x = 0
            position_y = 0

            match direction:
                case 1:
                    position_x = 0
                    position_y = -2
                case 2:
                    position_x = 2
                    position_y = 0
                case 3:
                    position_x = 0
                    position_y = 2
                case 4:
                    position_x = -2
                    position_y = 0

            x2 = x + position_x
            y2 = y + position_y

            if self.PRINT:
                print(" ")
                print("chemin :")
                for num, x_y_color_id in self.chemin.items():
                    print(f"id = {num}")
                    print(f"x = {x_y_color_id["x"]}; y = {x_y_color_id["y"]}; couleur = {x_y_color_id["color"]}; id = {x_y_color_id["id"]}; valide = {x_y_color_id["valide"]}")

                print(f"x2 : {x2} ; y2 : {y2}")

            num2 = None

            for numero, coordonnees in self.chemin.items():
                if coordonnees["x"] == x2 and coordonnees["y"] == y2:
                    num2_element = numero
                    num2 = coordonnees["id"]
                    color2 = coordonnees["color"]
                    break


            if num2 == None:
                print("\n \n \n--------------erreur----------------------------------------------------\n")
                for numero, coordonnees in self.chemin.items():
                    print(f"x : {coordonnees["x"]} | y : {coordonnees["y"]}   =    {x2}, {y2}")
                    if coordonnees["x"] == x2 and coordonnees["y"] == y2:
                        num2_element = numero
                        num2 = coordonnees["id"]
                        color2 = coordonnees["color"]
                        break
                return False

            elif num1 != num2:

                x_3 = (x + x2) / 2
                y_3 = (y + y2) / 2


                if self.PRINT:
                    print(f"position_1 = {position_aleatoir} ; position_2 = {num2_element}")
                    print(f"id_1 = {num1} ; id_2 = {num2}")
                    print(f"id de 1er carré : {self.chemin[position_aleatoir]["id"]}")
                    #print(chemin)
                    print("chemin :")
                    for num, x_y_color_id in self.chemin.items():
                        print(f"id = {num}")
                        print(
                            f"x = {x_y_color_id["x"]}; y = {x_y_color_id["y"]}; couleur = {x_y_color_id["color"]}; id = {x_y_color_id["id"]}; valide = {x_y_color_id["valide"]}")
                        print(" ")

                    print(f"si {position_aleatoir} -> valide >= {num2_element}")
                    print(f"tester si : {self.chemin[position_aleatoir]["valide"]} >= {self.chemin[num2_element]["valide"]}")

                    print("attendre")
                stop = False
                if self.STOP:
                    while not stop:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    print("ok")
                                    stop = True
                    #time.sleep(0.0001)
                    if self.PRINT:
                        print("fin")
                        print("\n")
                #pygame.draw.rect(screen, color, (x_3 * TAILLE_CARRE + ESPACEMENT, y_3 * TAILLE_CARRE + ESPACEMENT, TAILLE_CARRE, TAILLE_CARRE))


                #chemin[position_aleatoir]["valide"] >= chemin[num2_element]["valide"]:
                #print("oui")
                self.chemin[position_aleatoir]["valide"] += 1 # carré 1 -> valide + 1
                self.chemin[num2_element]["valide"] = self.chemin[position_aleatoir]["valide"] # carré 2 -> valide = valide du carré 2
                # ajouter au dictionnaire le carré noir
                self.chemin[carrer_noir_element] = {"x": x_3, "y": y_3, "color": color, "id": num1, "valide": self.chemin[position_aleatoir]["valide"]}
                pygame.draw.rect(self.screen, color, (
                    x_3 * self.TAILLE_CARRE + self.ESPACEMENT, y_3 * self.TAILLE_CARRE + self.ESPACEMENT, self.TAILLE_CARRE, self.TAILLE_CARRE))

                list_carre_2 = []
                # Parcourir le dictionnaire et afficher les coordonnées des éléments avec un id selectionne
                for key, value in self.chemin.items():
                    if value['id'] == self.chemin[num2_element]["id"]:
                        if self.PRINT:
                            print(f"color {color}")
                        if self.VITESSE >= 4:
                            pygame.draw.rect(self.screen, self.BLANC, (
                                value['x'] * self.TAILLE_CARRE + self.ESPACEMENT, value['y'] * self.TAILLE_CARRE + self.ESPACEMENT,
                                self.TAILLE_CARRE, self.TAILLE_CARRE))
                            pygame.display.flip()
                            time.sleep(0.1)
                        pygame.draw.rect(self.screen, color, (
                        value['x'] * self.TAILLE_CARRE + self.ESPACEMENT, value['y'] * self.TAILLE_CARRE + self.ESPACEMENT, self.TAILLE_CARRE, self.TAILLE_CARRE))
                        if self.VITESSE >= 3:
                            pygame.display.flip()

                        self.chemin[num2_element]["color"] = color

                        if self.PRINT:
                            print(f"Élément {key} a les coordonnées x: {value['x']}, y: {value['y']} et"
                                f" a id {value["id"]} et couleur : {value["color"]}")

                        list_carre_2.append(key)

                for i in list_carre_2:
                    if self.PRINT:
                        print(f"i : {i} id : {self.chemin[i]["id"]}")
                        print(f"mise à jour : ")
                        print(f"i : {i} id : {self.chemin[i]["id"]}")

                        print(" ")

                    self.chemin[i]["id"] = num1
                    self.chemin[i]["color"] = color



                if self.PRINT:
                    print("\n \n")

                if self.VITESSE >= 2:
                    pygame.display.flip()

                id_all_same = True
                all_key = list(self.chemin.keys())
                key_1 = all_key[0]
                id_1 = self.chemin[key_1]["id"]
                for value in self.chemin.values():
                    if value["id"] != id_1 and value["id"] != 20000:
                        id_all_same = False
                        break
                if id_all_same:
                    print(f"--------------break----------------------" * 3)
                    generating = False
                else:
                    chemin_id = [value["id"] for value in self.chemin.values()]

            carrer_noir_element += 1

        for key, value in self.chemin.items():
            pygame.draw.rect(self.screen, self.BLANC, (
                value['x'] * self.TAILLE_CARRE + self.ESPACEMENT, value['y'] * self.TAILLE_CARRE + self.ESPACEMENT,
                self.TAILLE_CARRE, self.TAILLE_CARRE))
            value["color"] = self.BLANC

        return True


        #carre2 = random.choice()

    def trouver_mur(self):
        id_ajout = 1
        for y in range(self.TAILLE_GRILLE_HAUTEUR):
            for x in range(self.TAILLE_GRILLE_LARGEUR):
                trouver = False
                # pour chaque élément du dictionnaire tester si le carré (x, y) est dans le dictionnaire (donc si c'est un passage)
                for key, value in self.chemin.items():
                    if x == value['x'] and y == value['y']:
                        trouver = True
                # si carré ne se trouve pas dans le dictionnaire alors:
                if not trouver:
                    self.chemin[self.element * self.element + id_ajout] = {"x": x, "y": y, "color": self.NOIR, "id": (self.element * self.element + id_ajout), "valide": 0}
                    id_ajout += 1