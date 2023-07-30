# Lager ei liste med oppgitte elementer
liste = [1, 2, 3, 4, 5]

# Lager ei tom liste
liste = list()

# Henter ut første element i lista. Indekser i Python lister starter på 0!
element = liste[0]

# Henter ut siste element i lista. Negative indekser teller fra slutten.
element = liste[-1]

# Setter tredje element i lista lik 5
liste[2] = 5

# Legger til elementet 8 på slutten av lista, utvider lista med ett element. Lister
# er objekter, append er en metode for lister.
liste.append(8)

# List Comprehensions
# Eksempel: lista av tall fra 1 til og med antall, kode slik dere har sett den hittil
antall = 10
liste = list()
for tall in range(1, antall+1):
    liste.append(tall)

# Med list comprehension
liste = [x for x in range(1, antall+1)]

# Kan ha formel, eksempel "liste av kvadratene for tall fra 1 til og med antall
kvadrater = [x**2 for x in range(1, antall+1)]

# Kan ha betingelse, eksempel "liste av oddetallene fra og med 1 til og med antall
oddetall = [x for x in range(1, antall+1) if x%2 != 0]

# Første intro til referanser
# Eksempel med tall og hvorden de oppfører seg
tall = 5
tall2 = 9
tall = tall2
tall2 += 5
print(f"tall:{tall} , tall2:{tall2}")

# Hvordan lister oppfører seg
liste = [x for x in range(1, 11)]
liste2 = liste
liste.append(15)
print(liste)
print(liste2)
del liste2[5]
print(liste)
print(liste2)

liste_kopi = liste[:]
print(liste_kopi)
liste_kopi.append(20)
print(liste_kopi)
print(liste)
print(liste2)

liste_slice = liste[2:5]
liste[3] = 15
print(liste)
print(liste_slice)

# tuppel / tuple: Immutable lister
tuppel = (4, 5, 6)

# Skriver ut verdien i en bestemt indeks
print(tuppel[1])
