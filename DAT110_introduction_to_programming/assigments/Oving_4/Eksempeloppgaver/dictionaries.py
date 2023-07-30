#Dictionary: Slår opp med en nøkkel for å få en verdi

#Ordteller: Ønsker å lese et tekstfil, finne ut hvilke ord den består av og
# hvor mange det er av hvert ord

# Algoritmen i pseudokode:
# Åpne fila
# Les hver linje
# splitt hver linje på ord
# fjern punctuation
# fjern store bokstaver
# Lag et dictionary med ord som nøkkel og antall forekomster som verdi
# Første gang jeg ser et otd, legg det inn med 1 forekomst
# Hvis jeg har sett ordet før, øk antall forekomster med 1
# Skriv ut dictionariet på slutten


# Python kode
filnavn = input("Navn på fila: ")
ordteller = dict()
with open(filnavn, encoding="UTF-8") as filreferanse:
    for linje in filreferanse:
        ordene = linje.split()
        for ord in ordene:
            ord_rensket = ord.strip(".,:;()")
            ord_rensket = ord_rensket.lower()
            if ord_rensket in ordteller:
                ordteller[ord_rensket] += 1
            else:
                ordteller[ord_rensket] = 1
for ord in ordteller:
    print(f"{ord} : {ordteller[ord]}")

