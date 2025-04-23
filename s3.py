# taper 10 nombres entier et stocker dans une liste
nombres = [int(input("Entrez un nombre : ")) for _ in range(10)]

# Afficher les elements separes par une tabulation
print("Nombres :", "\t".join(map(str, nombres)))

# Calculer la somme et calcule la moyenne
somme = sum(nombres)
print("Somme :", somme)
moyenne = somme / 10
print("Moyenne :", moyenne)

# Afficher les elements superieurs ou egale la moyenne
print("Nombres >= moyenne :", [n for n in nombres if n >= moyenne])