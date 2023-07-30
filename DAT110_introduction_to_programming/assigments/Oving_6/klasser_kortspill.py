
import random


class Kort:
    def __init__(self, type_kort, verdi):
        self.type = type_kort
        self.verdi = verdi

    def __str__(self):
        if 1 <= self.verdi <= 10:
            return f"{self.type} {self.verdi}"
        if self.verdi == 11:
            return f"{self.type} Knekt"
        if self.verdi == 12:
            return f"{self.type} Dame"
        if self.verdi == 13:
            return f"{self.type} Konge"
        return "ugyldig kort"


class Kortstokk:
    def __init__(self):
        self.kortene = []
        for number in range(1, 14):
            self.kortene.append(Kort("Spar", number))
            self.kortene.append(Kort("Ruter", number))
            self.kortene.append(Kort("Kløver", number))
            self.kortene.append(Kort("Hjerter", number))

    def stokk(self):
        random.shuffle(self.kortene)

    def trekk(self):
        kortet = self.kortene[-1]
        del self.kortene[-1]
        return kortet

    def __str__(self):
        resultat = "Kortstokk \n"
        for kort in self.kortene:
            resultat += str(kort) + "\n"
        return resultat

    def __len__(self):
        return len(self.kortene)
