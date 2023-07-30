# LAger to mengder fra lister
mengde1 = set([1, 3, 5, 7, 9, 11, 13])
mengde2 = set([2, 3, 5, 7, 11, 13])

# Legger til et element i en mengde
mengde1.add(15)

# Fjerner et element fra en mengde
mengde1.remove(1)

# Å legge til samme element en gang til endrer ikke mengden - den kan ikke inneholde
# duplikater
mengde1.add(7)
mengde1.add(1)

print(mengde1)
print(mengde2)
print()

# Mengdeoperasjonen union - lager en ny mengde som inneholder alle elementene
# som er med i minst en av de opprinnelige
print(f"union: {mengde1.union(mengde2)}")

# Mengdeoperasjonen snitt (intersection) - lager nye mengde med bare de elementene
# som er med i begge
print(f"snitt: {mengde1.intersection(mengde2)}")


# Mengdeoperasjonen minus (difference) - lager ny mengde som inneholder alle
# elementene fra mengde1 som ikke er med i mengde2
print(f"minus: {mengde1.difference(mengde2)}")
