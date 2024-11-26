import pygame
import math

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
width, height = 800, 600
window = pygame.display.set_mode((width, height))

# Définir les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Définir la position initiale du joueur (utilisation de coordonnées flottantes)
player_pos = pygame.Vector2(100, 100)
player_speed = 13  # Vitesse du joueur (pixels par frame)

# Définir la position de la cible (point B)
target_pos = pygame.Vector2(400, 100)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculer la direction du déplacement
    direction = target_pos - player_pos
    distance = direction.length()  # Distance entre le joueur et la cible

    # Déplacer le joueur vers la cible
    if distance > 0:  # Éviter la division par zéro
        direction = direction.normalize()  # Normaliser la direction
        player_pos += direction * player_speed  # Déplacer le joueur

    # Remplir l'écran de blanc
    window.fill(WHITE)

    # Dessiner le joueur (cercle noir)
    pygame.draw.circle(window, BLACK, (int(player_pos.x), int(player_pos.y)), 10)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Définir la vitesse de la boucle
    pygame.time.Clock().tick(60)

pygame.quit()
