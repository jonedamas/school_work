import numpy as np

# Lager en array med 10 0-ere
array = np.zeros(10)

# Kan indeksere og tilordne som ei liste, men kan ikke legge til elementer da
# numpy arrays har en fast størrelse, definert nbår du lager den
array[5] = 3

# Lager en array med elementene fra og med 0, til men ikke med 10, og med
# 0.2 mellom hvert element
array2 = np.arange(0, 10, 0.2)

print(array)
print(array2)

# LAger en 4*3 matrise gjennom å oppgi et tuppel med to elementer i stedet for
# en enkeltverdi
matrise = np.zeros((4, 3))

print(matrise)

# Kan gjøre matematiske operasjoner på numpy arrays:
print(array2 + 10)
print(array2 * 5)

# Numpy inneholder matematiske funksjoner som opererer element-for-element
# på numpy arrays. Eksempel sinus:
print(np.sin(array2))

# Kan summere og multiplisere to arrays med samme dimensjoner, dette gjøres
# element for element.

# Vanlig matrisemultiplikasjon gjøres med @ operatoren på numpy arrays
