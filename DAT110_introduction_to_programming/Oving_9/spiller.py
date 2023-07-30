import random


class Terning:
    def __init__(self, antall_sider=6):
        self.__verdi = 1
        self.__sider = antall_sider

    @property
    def verdi(self):
        return self.__verdi

    @property
    def antall_sider(self):
        return self.__sider

    def kast(self):
        self.__verdi = random.randint(1, self.__sider)


class Spiller:
    neste_id = 1        # Klasse-variabel, en for hele klassen heller enn en pr. instans
                        # Bruker denne for å lage ID-er for spillerne som automatisk teller
                        # opp.

    def __init__(self, navn):
        self.id = Spiller.neste_id      # Bruker klasse-variabelen gjennom navnet til klassen
        Spiller.neste_id += 1
        self.navn = navn
        self.poengsum = 0

    def __str__(self):
        return f"Spiller {self.id}: {self.navn} som har {self.poengsum} poeng"

