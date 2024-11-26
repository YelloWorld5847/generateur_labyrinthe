chemin = {}
for i in range(10):
    chemin[i] = {"x": i, "y": i * 2}

# Convertir les clés du dictionnaire en une liste
cles = list(chemin.keys())

# Récupérer la clé du 5ème élément (indice 4)
cle_du_5eme_element = cles[0]

print(cle_du_5eme_element)