#py

a = (2)
b = (5)
c = ("Bonjour")
d = (-9)
e = (" ")
a = [a, b, c, d, e]

for x in (a):

    if type(x)==str:
    
        print(x, "= Tu ne me la mettras pas à l'envers.")
    
    elif type(x)==float:
    
        print(x, "= Tu ne me la mettras pas à l'envers.")

    elif x %2 == 0:

        print(x, "= is even.")
    
    elif x %2 == 1:

        print(x, "= is odd.")