import pygame.sprite


class Player(pygame.sprite.Sprite):

    def __init__(self, y, TAILLE_CARRE, espacement, MOVE_PLAYER):
        super().__init__()

        def arondir(arg):
            arg_str = str(arg - (int(arg)))
            #print(f"arg_str : {arg_str}")
            if int(arg_str[2]) >= 5:
                #print("+")
                #print(int(arg) + 1)
                return int(arg) + 1
            else:
                #print("-")
                #print(int(arg))
                return int(arg)

        #print(y)
        self.vitesse = 4
        self.division = TAILLE_CARRE / self.vitesse
        if TAILLE_CARRE % self.vitesse != 0:
            self.division2 = arondir(self.division)
            #print("division2 :")
            #print(self.division2)
            self.vitesse = TAILLE_CARRE / self.division2
        else:
            self.division2 = self.division


        self.taille_carre = TAILLE_CARRE
        if TAILLE_CARRE < 15:
            taille_joueur = TAILLE_CARRE
            self.image = pygame.image.load('image/Carré_vert2.jpg')
        else:
            taille_joueur = TAILLE_CARRE * 0.8
            self.image = pygame.image.load('image/extraterrestre(2).png')
        self.image = pygame.transform.scale(self.image, (taille_joueur, taille_joueur))
        self.rect = self.image.get_rect()
        self.rect.x = espacement
        self.rect.y = y + (TAILLE_CARRE - taille_joueur) / 2
        self.vitesse2 = MOVE_PLAYER
        self.rep = int(TAILLE_CARRE / self.vitesse2)


    def move_right(self):
        self.rect.x += self.vitesse2  #self.vitesse

    def move_left(self):
        self.rect.x -= self.vitesse2

    def move_up(self):
        self.rect.y -= self.vitesse2

    def move_down(self):
        self.rect.y += self.vitesse2

'''
class Player(pygame.sprite.Sprite):

    def __init__(self, y, TAILLE_CARRE, espacement, MOVE_PLAYER):
        super().__init__()

        self.taille_carre = TAILLE_CARRE
        if TAILLE_CARRE < 15:
            taille_joueur = TAILLE_CARRE
            self.image = pygame.image.load('image/Carré_vert2.jpg')
        else:
            taille_joueur = TAILLE_CARRE * 0.8
            self.image = pygame.image.load('image/extraterrestre(2).png')
        self.image = pygame.transform.scale(self.image, (taille_joueur, taille_joueur))
        self.rect = self.image.get_rect()
        self.rect.x = espacement
        self.rect.y = y + (TAILLE_CARRE - taille_joueur) / 2
        self.vitesse2 = MOVE_PLAYER
        self.rep = int(TAILLE_CARRE / self.vitesse2)

        # Position actuelle (flottante)
        self.position = pygame.Vector2(self.rect.x, self.rect.y)
        # Position cible
        self.target_position = self.position

    def set_target_position(self, x, y):
        self.target_position = pygame.Vector2(x, y)

    def update(self):
        # Calculer la direction du déplacement
        direction = self.target_position - self.position
        distance = direction.length()  # Distance entre la position actuelle et la cible

        # Déplacer le joueur vers la cible si la distance est significative
        if distance > 0:
            direction = direction.normalize()  # Normaliser la direction
            self.position += direction * self.vitesse2  # Déplacer le joueur
            # Mettre à jour le rect avec la position entière
            self.rect.x, self.rect.y = self.position.x, self.position.y

    def move_right(self):
        self.set_target_position(self.position.x + self.vitesse2, self.position.y)

    def move_left(self):
        self.set_target_position(self.position.x - self.vitesse2, self.position.y)

    def move_up(self):
        self.set_target_position(self.position.x, self.position.y - self.vitesse2)

    def move_down(self):
        self.set_target_position(self.position.x, self.position.y + self.vitesse2)
'''