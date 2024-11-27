
# Générateur de Labyrinthes

Un jeu interactif en Python pour générer et explorer des labyrinthes. Ce projet utilise **Pygame** pour l'affichage et propose des fonctionnalités dynamiques comme la personnalisation de la taille du labyrinthe et des contrôles pour déplacer un joueur à travers le labyrinthe généré.

## Fonctionnalités

- **Génération aléatoire de labyrinthes** avec des dimensions configurables.
- **Déplacements interactifs** du joueur à travers le labyrinthe.
- **Personnalisation des paramètres**, notamment la taille des cases, la vitesse de génération, et le mode plein écran.
- Gestion des dimensions pour éviter les erreurs liées à des tailles invalides.

## Prérequis

Avant d'exécuter le projet, assurez-vous d'avoir les outils suivants installés :

- **Python 3.x**
- Les bibliothèques suivantes :
  - `pygame`
  - `pyautogui`
  - `random` (inclus nativement dans Python)
  - `time` (inclus nativement dans Python)

Pour installer Pygame, utilisez la commande suivante :

```bash
pip install pygame
```

## Installation et exécution

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/YelloWorld5847/generateur_labyrinthe.git
   cd generateur_labyrinthe
   ```

2. Exécutez le fichier principal :

   ```bash
   python main_2.py
   ```

3. Appuyez sur **`s`** pour commencer la génération du labyrinthe.

## Contrôles du jeu

- **Flèches directionnelles** : déplacer le joueur dans les quatre directions.
- **`s`** : démarrer la génération du labyrinthe.

## Paramètres ajustables

Dans le fichier `main_2.py`, vous pouvez modifier les paramètres suivants :

- `TAILLE_GRILLE` : Nombre de cases dans la grille.
- `TAILLE_CARRE` : Taille des cases (pixels).
- `FULL_SCREEN` : Activer/désactiver le mode plein écran.
- `VITESSE` : Détermine la vitesse de génération et d'animation.


## Problèmes connus

- La taille de la grille doit être impaire pour éviter des erreurs. Si une taille paire est entrée, le programme ajustera automatiquement les dimensions.
- L'affichage peut ne pas être optimal sur des résolutions d'écran inhabituelles.

