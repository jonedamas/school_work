from spiller import Terning, Spiller


class Rute:
    def __init__(self, posisjon):
        self.posisjon = posisjon

    def flytt_hit(self, spillobjekt: Spiller):
        spillobjekt.poengsum = self.posisjon
        return f'{spillobjekt} har flyttet til rute {self.posisjon}.'


class TilbakeTilStart:
    def __init__(self, posisjon):
        self.posisjon = posisjon

    def flytt_hit(self, spillobjekt: Spiller):
        spillobjekt.poengsum = 0
        return f'{spillobjekt} har flyttet til rute {self.posisjon}, men må flytte tilbake til start.'


class Hinder:
    def __init__(self, posisjon):
        self.posisjon = posisjon

    def flytt_hit(self, spillobjekt: Spiller):
        spiller.poengsum -= terning.verdi
        return f'{spillobjekt} har blitt hindret i rute {self.posisjon}.'


def utskrift(spiller_posisjoner):
    for ruter in reversed(vei):
        rute_index = vei.index(ruter)
        spiller_plass = ''
        for spillere in spiller_posisjoner:
            if rute_index == spillere.poengsum:
                spiller_plass += f'({spillere.id})  '

        if rute_index < 10:
            space = ' '
        else:
            space = ''
        if isinstance(ruter, Rute):
            print(f'{rute_index}:{space} |O|  {spiller_plass}')
        if isinstance(ruter, Hinder):
            print(f'{rute_index}:{space} |H|  {spiller_plass}')
        if isinstance(ruter, TilbakeTilStart):
            print(f'{rute_index}:{space} |X|  {spiller_plass}')


if __name__ == '__main__':
    spill_slutt = False

    vei = [i for i in range(20)]

    for rute in [2, 10, 18]:
        vei[rute] = TilbakeTilStart(rute)

    for rute in [4, 8, 12, 17]:
        vei[rute] = Hinder(rute)

    for rute in [0, 1, 3, 5, 6, 7, 9, 11, 13, 14, 15, 16, 19]:
        vei[rute] = Rute(rute)

    spiller_1 = Spiller('Jone')
    spiller_2 = Spiller('Louise')
    spillerliste = [spiller_1, spiller_2]
    terning = Terning(antall_sider=6)

    utskrift(spillerliste)
    while not spill_slutt:
        for spiller in spillerliste:
            kast = input(f'Kast terning, {spiller}?')
            terning.kast()
            print(f'{spiller} kastet: {terning.verdi}')
            spiller.poengsum += terning.verdi
            if spiller.poengsum < 19:
                print(vei[spiller.poengsum].flytt_hit(spiller))
                print()
                utskrift(spillerliste)

            else:
                print(f'{spiller} vinner')
                spill_slutt = True
                break
    print()
    print('spillet er avsluttet.')
