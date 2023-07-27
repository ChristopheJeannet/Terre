#py

# S02 M03 - Épreuve de la Terre

# Exercice " Inverser une chaîne ”

# Pseudo-code:
# Si nous voulons inverser des chaînes de caractères, à l'endroit comme à l'envers !
#
# Nous avons besoin:
#
# - d'une list des chaînes de caractère : Hello world!, lehciM.
#  - d'une boucle FOR qui contients :
#       - affichage des charactères comme fournis
#       - affichage des caractères comme demandés

# Déclarations des valeurs. Séparé sinon pas le même résultat.

a = " hello world! "
b = " lehciM "

# Vérrification de la list.

print(a + b)

# Vérrification de la class.

print(type(a + b))

# Boucle d'interpretation de la demande.

for x in a, b:

# Déclaration qui fait quoi.

    normale = x

    inversé = x[::-1]

# affichage de la demande suivant l'attendue.

    print("Donnée: ", normale)

    print("invesé: ", inversé)