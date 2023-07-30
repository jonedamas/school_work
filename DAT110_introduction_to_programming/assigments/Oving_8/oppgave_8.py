import random
import numpy as np


class Skip:
    def __init__(self, start_x, start_y, retning='horisontal', lengde=2):
        self.x_koordinat = start_x
        self.y_koordinat = start_y
        self.retning = retning
        self.lengde = lengde
        self.__antall_treff = 0

    def __str__(self):
        return f'Startkoordinater: ({self.x_koordinat}, {self.y_koordinat})\n' \
               f'Lengde: {self.lengde}, Antall treff: {self.__antall_treff}'

    def treff(self):
        self.__antall_treff += 1
        if self.er_senket():
            print()
            print(f'Skip med {self.__str__()} er senket.')

    def er_senket(self):
        if self.__antall_treff >= self.lengde:
            return True
        else:
            return False


class Spillbrett:
    def __init__(self):
        self.skudd_brukt = 0
        self.skipsliste = list()
        self.skutt_ruter = np.zeros([10, 10])
        self.ref_ruter = np.zeros([10, 10], dtype=object)

    def lovlig_plassering(self, ny_x, ny_y, retning, lengde):
        try:
            for punkt in range(lengde):
                if retning == 'horisontal':

                    x_koordinat = ny_x + punkt
                    y_koordinat = ny_y
                    if x_koordinat and y_koordinat <= 9:
                        if self.ref_ruter[x_koordinat, y_koordinat] == 0:
                            continue
                        else:
                            return False
                    else:
                        return False

                elif retning == 'vertikal':

                    x_koordinat = ny_x
                    y_koordinat = ny_y + punkt
                    if x_koordinat and y_koordinat <= 9:
                        if self.ref_ruter[x_koordinat, y_koordinat] == 0:
                            continue
                        else:
                            return False
                    else:
                        return False
            return True

        except IndexError:
            return False

    def plasser_skip(self, ny_x, ny_y, retning, lengde):
        if self.lovlig_plassering(ny_x, ny_y, retning, lengde):
            nytt_skip = Skip(ny_x, ny_y, retning, lengde)
            self.skipsliste.append(nytt_skip)
            for punkt in range(lengde):
                if retning == 'horisontal':
                    self.ref_ruter[ny_x + punkt, ny_y] = nytt_skip

                elif retning == 'vertikal':
                    self.ref_ruter[ny_x, ny_y + punkt] = nytt_skip

    def skyt_rute(self, x, y, datamaskin):
        if self.skutt_ruter[y, x] == 0:
            if isinstance(self.ref_ruter[x, y], Skip):
                print('Treff')
                self.skutt_ruter[x, y] = 1
                self.ref_ruter[x, y].treff()
                self.ref_ruter[x, y] = 1
                print()
                return True
            else:
                self.skutt_ruter[x, y] = 1
                print('Bom')
                print()
                return True
        if not datamaskin:
            print('Ruten er allerede skutt')
            print()
        return False

    def brett_print(self, name, other):
        print(f'{name} skip:                      Ruter skutt')
        print('   0 1 2 3 4 5 6 7 8 9             0 1 2 3 4 5 6 7 8 9')
        for linje in range(10):
            resultat = f'{linje}: '
            for element in range(10):
                if self.skutt_ruter[element, linje] == 1 and self.ref_ruter[element, linje] == 1:
                    resultat += 'X '
                elif isinstance(self.ref_ruter[element, linje], Skip):
                    resultat += 'M '
                elif self.skutt_ruter[element, linje] != 0:
                    resultat += 'O '
                elif self.ref_ruter[element, linje] == 0:
                    resultat += '~ '
            resultat += f'         {linje}: '
            for element in range(10):
                if other.skutt_ruter[element, linje] and other.ref_ruter[element, linje] == 1:
                    resultat += 'X '
                elif other.skutt_ruter[element, linje] == 1:
                    resultat += 'O '
                else:
                    resultat += '~ '

            print(resultat)
        print()

    def sjekk_vinn(self):
        for skip in self.skipsliste:
            if skip.er_senket:
                continue
            else:
                return True
        return False


def autofyll(spillertype, lengder):
    for lengde in lengder:
        while True:
            rand_x = random.randint(0, 9)
            rand_y = random.randint(0, 9)
            rand_retning = random.choice(['horisontal', 'vertikal'])
            if spillertype.lovlig_plassering(rand_x, rand_y, rand_retning, lengde):
                spillertype.plasser_skip(rand_x, rand_y, rand_retning, lengde)
                break
            else:
                continue


if __name__ == '__main__':

    skipslengder = [5, 4, 3, 3, 2]

    spiller_data = Spillbrett()
    spiller = Spillbrett()

    autofyll(spiller_data, skipslengder)
    print()

    auto = True

    if auto:
        autofyll(spiller, skipslengder)
    else:
        for lengde_skip in skipslengder:
            while True:
                spiller.brett_print('Dine', spiller_data)
                input_retning = input(f'Retning på skip med lengde {lengde_skip}: ')
                input_x = int(input('X_koordinat: '))
                input_y = int(input('Y_koordinat: '))
                if spiller.lovlig_plassering(input_x, input_y, input_retning, lengde_skip):
                    spiller.plasser_skip(input_x, input_y, input_retning, lengde_skip)
                    break
                else:
                    continue

    avslutt = False
    spiller_tur = True

    while not avslutt:
        try:
            if spiller_tur:
                spiller_data.brett_print('Datamaskin sine', spiller)
                spiller.brett_print('Dine', spiller_data)
                skudd_x = int(input('Skuddkoordinat x: '))
                skudd_y = int(input('Skuddkoordinat y: '))
                if spiller_data.skyt_rute(skudd_x, skudd_y, False):
                    if spiller_data.sjekk_vinn():
                        avslutt = True
                    spiller_tur = False
                    print('Datamaskinen:')

            else:
                rand_skudd_x = random.randint(0, 9)
                rand_skudd_y = random.randint(0, 9)
                if spiller.skyt_rute(rand_skudd_x, rand_skudd_y, True):
                    if spiller.sjekk_vinn():
                        avslutt = True
                    print(f'Datamaskin skjøt på ({rand_skudd_x},{rand_skudd_y})')
                    print()
                    spiller_tur = True

        except ValueError and IndexError:
            print('Ugyldig input')

    if spiller_tur:
        print('Spillet er avsluttet, Datamaskin vinner')
    else:
        print('Spillet er avsluttet, du vinner.')
