import klasser_kortspill as ks


class Spill:
    def __init__(self):
        self.kortstokk = ks.Kortstokk()
        self.posisjoner = []
        self.kortstokk.stokk()
        for kort in range(9):
            self.posisjoner.append(self.kortstokk.trekk())

    def skriv_tilstand(self):
        for index, kort in enumerate(self.posisjoner):
            print(f'{index + 1}: {kort}')
        print(f'Antall kort igjen: {len(self.kortstokk)}')

    def spill_over(self):
        if len(self.kortstokk) == 0:
            return True

    def plasser_2(self, pos_1, pos_2):
        if int(self.posisjoner[pos_1 - 1].verdi) + int(self.posisjoner[pos_2 - 1].verdi) == 11:
            for pos in [pos_1, pos_2]:
                self.posisjoner.remove(self.posisjoner[pos - 1])
                self.posisjoner.append(self.kortstokk.trekk())
        else:
            print('Summen av kortene er ikke 11.')

    def plasser_3(self, pos_1, pos_2, pos_3):
        if self.posisjoner[pos_1 - 1].verdi and self.posisjoner[pos_2 - 1].verdi and self.posisjoner[pos_3 - 1].verdi > 10:
            for pos in [pos_1, pos_2, pos_3]:
                self.posisjoner.remove(self.posisjoner[pos - 1])
                self.posisjoner.append(self.kortstokk.trekk())
        else:
            print('Alle kortene er ikke bildekort.')


if __name__ == '__main__':
    spill_1 = Spill()
    spill_1.skriv_tilstand()

    while not spill_1.spill_over():
        try:
            kort_1 = int(input('Første kort: '))
            kort_2 = int(input('Andre kort: '))
            if spill_1.posisjoner[kort_1 - 1].verdi <= 10:
                spill_1.plasser_2(kort_1, kort_2)
                spill_1.skriv_tilstand()
            else:
                kort_3 = int(input('Tredje kort: '))
                spill_1.plasser_3(kort_1, kort_2, kort_3)
                spill_1.skriv_tilstand()
        except ValueError:
            print('Ugyldig input.')
        except IndexError:
            print('Kortet finnes ikke.')

    print('Spillet er slutt')
