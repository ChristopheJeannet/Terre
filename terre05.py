#py

# S02 M03 - Épreuve de la Terre

# Exercice “Divisions”

# Pseudo-code:
# si je veux dire que dans la list, tu prends les couples 0 et 1 puis 2 et 3 ainsi
# de suite, pour faire l'action " // ", puis donne le resultat du reste " % ",
# nous avons besoin:
#
# - d'une list contenant les chiffres : 5, 2, 10, 0, 3, 5.
#    - d'une boucle FOR qui contients : 
#      - prise en compte des erreurs " erreur".
#      - action de diviser " // " à afficher " print ".
#      - action de calcul du reste " % " à afficher " print ".

# Déclarations des valeurs.

a = (5, 2)
b = (10, 0)
c = (3, 5)

# Regroupements des valeurs.

a = [a, b, c]

# Vérrification de la list.

print(a)

# Vérrification de la class.

print(type(a))

# Boucle pour la lecture des couples dans la list, l'un aprés l'autre.

for x in range(0, len(a)):
    
# Déclaration qui est quoi.

    dividende = a[x][0]
    
    diviseur = a[x][1]
    
# Condition pour interprêter les erreurs.

    if diviseur == 0:

        print("Erreur:",x)

# Condition pour trouver le résultat en entier "int".

    else:

        result_entier = dividende // diviseur

        print("resultat:", result_entier)

# Condition pour trouver le résultat du reste uniquement "int".

        result_reste = dividende % diviseur
    
        print("reste:", result_reste)

# Condition qui donne le résultat que l'on aurait pu attendre.

        réellement = dividende / diviseur

        print("résultat réel", réellement)