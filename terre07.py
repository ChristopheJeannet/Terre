#py

# S02 M03 - Épreuve de la Terre

# Exercice “ Racine carrée d'un nombre ”

# Pseudo-code:
# si je veux dire que dans la list, tu prends la valeur et tu la mets au carrée
# nous avons besoin:
#
# - d'une list contenant le chiffre : 9, plus si affinité.
#    - d'une boucle FOR qui contients : 
#      - prise en compte des erreurs " try / except ".
#      - conversion du type de donné en " float ".
#      - action de diviser " ** " à afficher " print ".


# Déclaration de la valeur.

a = [9, "dfghn", "douze"]

# Vérrification de la varaible.

print(a)

# Vérrification de la class.

print(type(a))

# Boucle d"execution de la demande.

for x in a:

# Mise en place d'une identification d'erreur: " try / except ".

    try:

# Conversion du type de donné.

        Valeur_float = float(x)

# Déclaration de ce que nous voulons.

        Racine_carree = (Valeur_float ** 0.5)

# Conversion du résultat en nombre entier.

        resultat_entier = int(Racine_carree)

        print("Résultat a la racine² :", resultat_entier)

# Condition si identification d'erreurs : " try / except ".

    except ValueError:

        print("La valeur donnée :", x, ", n'est pas un nombre valable.")