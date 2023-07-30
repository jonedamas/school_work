import math


class Posisjon:
    def __init__(self, x_koordinat, y_koordinat, hoyde):
        self.x_koordinat = x_koordinat
        self.y_koordinat = y_koordinat
        self.hoyde = hoyde

    def hoydeforskjell(self, annen_posisjon):
        return abs(self.hoyde - annen_posisjon.hoyde)

    def avstand(self, annen_posisjon):
        return math.sqrt((self.x_koordinat - annen_posisjon.x_koordinat) ** 2 +
                         (self.y_koordinat - annen_posisjon.y_koordinat) ** 2 +
                         (self.hoyde - annen_posisjon.hoyde) ** 2)

    def __eq__(self, other):
        if self.x_koordinat != other.x_koordinat:
            return False
        if self.y_koordinat != other.y_koordinat:
            return False
        if self.hoyde != other.hoyde:
            return False
        return True


class Tur:
    def __init__(self, navn, starttidspunkt, sluttidspunkt):
        self.navn = navn
        self.starttidspunkt = starttidspunkt
        self.sluttidspunkt = sluttidspunkt
        self.posisjoner = list()

    def add_posisjon(self, posisjon):
        self.posisjoner.append(posisjon)

    def add_posisjon_koordinater(self, x_koordinat, y_koordinat, hoyde):
        self.posisjoner.append(Posisjon(x_koordinat, y_koordinat, hoyde))
        # Rettet skrivefeil

    def hoydemeter(self):
        resultat = 0.0
        for i in range(len(self.posisjoner) - 1):  # Justert Indexing
            resultat += self.posisjoner[i].hoydeforskjell(self.posisjoner[i + 1])
        return resultat

    def er_rundtur(self):
        if self.posisjoner[0] == self.posisjoner[-1]:
            return True
        return False
