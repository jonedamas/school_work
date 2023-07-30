import math


class Sirkel:
    def __init__(self, ny_x, ny_y, ny_r):
        self.senter_x_koordinat = ny_x
        self.senter_y_koordinat = ny_y
        self.radius = ny_r

    def flytt(self, delta_x, delta_y):
        self.senter_x_koordinat += delta_x
        self.senter_y_koordinat += delta_y

    def areal(self):
        return math.pi * self.radius ** 2

    def avstand(self, annen_sirkel):
        return math.sqrt((self.senter_x_koordinat - annen_sirkel.senter_x_koordinat) ** 2
                         + (self.senter_y_koordinat - annen_sirkel.senter_x_koordinat) ** 2)

    def overlapper(self, annen_sirkel):
        if self.radius + annen_sirkel.radius - self.avstand(annen_sirkel) > 0:
            return True
        else:
            return False

    def __str__(self):
        return f'Senterkordinat: ({self.senter_x_koordinat}, {self.senter_y_koordinat})\n' \
               f'Radius: {self.radius}'


if __name__ == "__main__":
    sirkel_1 = Sirkel(2, 2, 1)
    sirkel_2 = Sirkel(2, 6, 2)
    sirkel_3 = Sirkel(2, 7, 3)
    sirkler = [sirkel_1, sirkel_2, sirkel_3]

    for sirkel in sirkler:
        print(sirkel)

    for sirkel in sirkler:
        for i in range(len(sirkler)):
            print(sirkel.avstand(sirkler[i]))
            print(sirkel.overlapper(sirkler[i]))
