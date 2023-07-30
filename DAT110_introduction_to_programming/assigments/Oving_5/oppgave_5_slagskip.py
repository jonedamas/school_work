import random


class Skip:
    def __init__(self, start_x, start_y, retning='horisontal', lengde=2):
        self.x_koordinat = start_x
        self.y_koordinat = start_y
        self.retning = retning
        self.lengde = lengde
        self.__antall_treff = 0
        self.treffpunkter = list()

        for punkt in range(self.lengde):
            if self.retning == 'horisontal':
                treffpunkt = tuple((self.x_koordinat + punkt, self.y_koordinat))
                if self.x_koordinat + self.lengde - 1 <= 10:
                    self.treffpunkter.append(treffpunkt)
                else:
                    raise ValueError(f'Dette skipet går utenfor brettet i {self.retning} rettning:\n{self}')

            elif self.retning == 'vertikal':
                treffpunkt = tuple((self.x_koordinat, self.y_koordinat + punkt))
                if self.y_koordinat + self.lengde - 1 <= 10:
                    self.treffpunkter.append(treffpunkt)
                else:
                    raise ValueError(f'Dette skipet går utenfor brettet i {self.retning} rettning:\n{self}')
            else:
                raise ValueError(f'Dette skipet har en ugyldig rettning:\n{self}')

    def __str__(self):
        return f'Startkoordinater: ({self.x_koordinat}, {self.y_koordinat})\n' \
               f'Lengde: {self.lengde}, Antall treff: {self.__antall_treff}'

    def treff(self):
        self.__antall_treff += 1

    @property
    def er_senket(self):
        if self.__antall_treff == self.lengde:
            return True
        else:
            return False


class SkipLoadout:
    def __init__(self, name):
        self.name = name
        self.skipliste = []
        self.type_skip = [5, 4, 4, 3, 3, 2]
        for skipslengde in self.type_skip:
            try:
                ny_x = int(input(f'X-koordinat for skip med lengde {self.type_skip[skipslengde]}: '))
                ny_y = int(input(f'Y-koordinat for skip med lengde {self.type_skip[skipslengde]}: '))
                ny_retning = input('Retning for skipet(vertikal/horisontal): ')
                nytt_skip = Skip(ny_x, ny_y, ny_retning, skipslengde)
                for skipene in self.skipliste:
                    if nytt_skip.treffpunkter in skipene.treffpunkter:
                        print(f'Skipet overlapper med skip: {skipene}')
                        raise TypeError()
                    else:
                        continue
            except TypeError:
                print('Prøv igjen')

    def __str__(self):
        loadout = f'{self.name}\n'
        for element in self.skipliste:
            loadout += str(element) + '\n'
        return loadout


def skudd_koordinat_promt():
    skudd_x = int(input('X koordinat:'))
    while skudd_x <= 0 or skudd_x > 10:
        print('X-posisjonen er utenfor spillbrettet, prøv igjen.')
        skudd_x = int(input('X koordinat:'))
    skudd_y = int(input('y koordinat:'))
    while skudd_y <= 0 or skudd_y > 10:
        print('Y-posisjonen er utenfor spillbrettet, prøv igjen.')
        skudd_y = int(input('y koordinat:'))
    skudd_koordinatet = (skudd_x, skudd_y)
    return skudd_koordinatet


def skudd_koordinat_npc():
    skudd_x = random.randint(1, 10)
    skudd_y = random.randint(1, 10)
    skudd_koordinatet = (skudd_x, skudd_y)
    return skudd_koordinatet


def skutt_sjekk(ruter_skutt):
    if skudd_koordinat in ruter_skutt:
        print(f'Skuddet {skudd_koordinat} har allerede blitt skutt.')
    else:
        return True


def sjekk_treff(skip_liste):
    for enhet in skip_liste:
        if skudd_koordinat in enhet.treffpunkter:
            enhet.treff()
            print('Treff.')
            if enhet.er_senket:
                print(f'{enhet}, er senket.')
                skip_liste.remove(enhet)
            return True
        else:
            continue
    print('Bom.')


if __name__ == "__main__":
    # Skip spiller 1
    spiller_1 = SkipLoadout()
    skip_1_1 = Skip(6, 2, 'horisontal', 5)
    skip_1_2 = Skip(1, 2, 'vertikal', 4)
    skip_1_3 = Skip(3, 1, 'vertikal', 4)
    skip_1_4 = Skip(8, 4, 'vertikal', 3)
    skip_1_5 = Skip(2, 9, 'horisontal', 3)
    skip_1_6 = Skip(5, 4, 'horisontal', 2)

    # Skip spiller 2
    skip_2_1 = Skip(3, 4, 'vertikal', 5)
    skip_2_2 = Skip(7, 2, 'horisontal', 4)
    skip_2_3 = Skip(5, 6, 'horisontal', 4)
    skip_2_4 = Skip(1, 6, 'vertikal', 3)
    skip_2_5 = Skip(7, 4, 'horisontal', 3)
    skip_2_6 = Skip(1, 2, 'horisontal', 2)

    # Lister over hver spiller sine skip
    spiller_1_skip = [skip_1_1, skip_1_2, skip_1_3, skip_1_4, skip_1_5, skip_1_6]
    spiller_2_skip = [skip_2_1, skip_2_2, skip_2_3, skip_2_4, skip_2_5, skip_2_6]

    ruter_skutt_spiller_1 = list()
    ruter_skutt_spiller_2 = list()

    # Utskrift alle skip med info
    print('Spiller 1 skip:')
    for skip in spiller_1_skip:
        print(f'{skip} \n{skip.treffpunkter}')
        print()

    print()
    print('Spiller 2 skip:')
    for skip in spiller_2_skip:
        print(f'{skip} \n{skip.treffpunkter}')
        print()

    # Div parameter
    spiller_1_tur = True
    spiller_1_vinner = False
    spiller_2_vinner = False
    end_game = False
    motspiller = True

    # Tester om skipene har treffpunkter
    for skip in spiller_1_skip:
        if not skip.treffpunkter:
            end_game = True

    for skip in spiller_2_skip:
        if not skip.treffpunkter:
            end_game = True

    # Gameloop
    while True:
        if end_game:
            break
        try:
            if spiller_1_tur:
                print()
                print('Spiller 1 sin tur.')
                skudd_koordinat = skudd_koordinat_promt()
                if skutt_sjekk(ruter_skutt_spiller_1):
                    spiller_1_tur = False
                    ruter_skutt_spiller_1.append(skudd_koordinat)
                    sjekk_treff(spiller_2_skip)
                    if not spiller_2_skip:
                        end_game = True
                        spiller_1_vinner = True
                        break
            else:
                print()
                print('Spiller 2 sin tur.')
                if motspiller:
                    skudd_koordinat = skudd_koordinat_npc()
                else:
                    skudd_koordinat = skudd_koordinat_promt()
                if skutt_sjekk(ruter_skutt_spiller_2):
                    print(f'Spiller 2 skjøt på: {skudd_koordinat}')
                    spiller_1_tur = True
                    ruter_skutt_spiller_2.append(skudd_koordinat)
                    sjekk_treff(spiller_1_skip)
                    if not spiller_1_skip:
                        end_game = True
                        spiller_2_vinner = True
                        break

        except ValueError:
            print('Ugyldig input, prøv på nytt.')

    print()
    if spiller_1_vinner:
        print('Spillet er avsluttet, spiller 1 Vinner.')
    elif spiller_2_vinner:
        print('Spillet er avsluttet, spiller 2 Vinner.')
    else:
        print('Spillet er avsluttet.')
