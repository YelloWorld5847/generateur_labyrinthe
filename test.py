import pygame
import sys

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
largeur_fenetre = 300
hauteur_fenetre = 200

# Créer la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# Charger l'image
image = pygame.image.load('image/labyrinthe_game.png')

# Obtenir les dimensions de l'image
largeur_image, hauteur_image = image.get_size()

# Calculer les nouvelles dimensions pour que l'image soit 4 fois plus petite que la fenêtre
nouvelle_largeur = largeur_fenetre // 2
nouvelle_hauteur = hauteur_fenetre // 2

# Calculer le facteur de redimensionnement pour conserver le rapport d'aspect
facteur_redimensionnement = min(nouvelle_largeur / largeur_image, nouvelle_hauteur / hauteur_image)
# Calculer les dimensions finales de l'image redimensionnée
dimensions_finales = (int(largeur_image * facteur_redimensionnement), int(hauteur_image * facteur_redimensionnement))

# Redimensionner l'image
image_redimensionnee = pygame.transform.scale(image, dimensions_finales)

# Calculer la position pour centrer l'image dans la fenêtre
position_x = (largeur_fenetre - dimensions_finales[0]) // 2
position_y = (hauteur_fenetre - dimensions_finales[1]) // 2

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Remplir la fenêtre avec une couleur (blanc ici)
    fenetre.fill((255, 255, 255))

    # Afficher l'image redimensionnée à la position calculée
    fenetre.blit(image_redimensionnee, (position_x, position_y))

    # Mettre à jour l'affichage
    pygame.display.flip()
