import tkinter as tk
from tkinter import messagebox
import numpy as np
import random


class SpillbrettGUI:
    def __init__(self):
        self.hovedvindu = tk.Tk()
        self.ruteliste = list()
        self.ruteliste_fi = list()
        self.skipslengder = [5, 4, 3, 3, 2]

        self.spillbrett_blue = Spillbrett()
        self.spillbrett_green = Spillbrett()

        autofyll(self.spillbrett_blue, self.skipslengder)
        autofyll(self.spillbrett_green, self.skipslengder)

        self.beskjed_string = tk.StringVar()
        self.beskjed_string_fi = tk.StringVar()
        self.beskjed_string.set('Trykk på en rute for å begynne')
        self.beskjed_string_fi.set('')
        self.tekstfelt = tk.Label(self.hovedvindu, textvariable=self.beskjed_string)
        self.tekstfelt_fi = tk.Label(self.hovedvindu, textvariable=self.beskjed_string_fi)

        # Blå spillbrett
        for i in range(10):
            for j in range(10):
                ny_rute = Rute(self.hovedvindu, i, j, self.spillbrett_blue.ref_ruter[i, j],
                               self.ruteliste, self.beskjed_string, self.data_skyter, self.sjekk_vinn)
                ny_rute.lerret.grid(row=i, column=j)
                self.ruteliste.append(ny_rute)

        self.empty = tk.Label(self.hovedvindu, text='              ')
        self.empty.grid(row=0, column=10)

        # Grønn spillbrett
        for i in range(10):
            for j in range(10):
                ny_rute = FiRute(self.hovedvindu, i, j, self.spillbrett_green.ref_ruter[i, j],
                                 self.ruteliste_fi, self.beskjed_string_fi, self.sjekk_vinn_fi)
                ny_rute.lerret.grid(row=i, column=j + 11)
                self.ruteliste_fi.append(ny_rute)

        self.tekstfelt.grid(row=10, column=0, columnspan=10)
        self.tekstfelt_fi.grid(row=10, column=11, columnspan=10)

        tk.mainloop()

    def sjekk_vinn(self):
        for skip in self.spillbrett_blue.skipsliste:
            if skip.er_senket():
                pass
            else:
                return
        messagebox.showinfo('Spillet er avsluttet', 'Gratulerer, du vant')
        self.hovedvindu.destroy()

    def sjekk_vinn_fi(self):
        for skip in self.spillbrett_green.skipsliste:
            if skip.er_senket():
                pass
            else:
                return
        messagebox.showinfo('Spillet er avsluttet', 'Datamaskinen vant')
        self.hovedvindu.destroy()

    def data_skyter(self):
        fortsett = True
        while fortsett:
            skudd_x = random.randint(0, 9)
            skudd_y = random.randint(0, 9)
            for rute in self.ruteliste_fi:
                if rute.x == skudd_x and rute.y == skudd_y:
                    if rute.tilstand == 'ikke_skutt':
                        rute.data_skyter_rute()
                        self.beskjed_string_fi.set(f'Datamaskinen skyter på rute [{rute.y}, {rute.x}].')
                        fortsett = False
                    else:
                        continue


class Rute:
    def __init__(self, vindu, x, y, innhold, ruteliste, stringvar, data_skyt, sjekk_vinn):
        self.vindu = vindu
        self.ruteliste = ruteliste
        self.x = x
        self.y = y
        self.lerret = tk.Canvas(self.vindu, width=64, height=64)
        self.rektangel = self.lerret.create_rectangle(0, 0, 64, 64, fill='lightblue')

        self.innhold = innhold
        self.data_skyter = data_skyt
        self.beskjed = stringvar
        self.sjekk = sjekk_vinn

        # Starttilstand
        self.tilstand = 'ikke_skutt'
        self.fyll_enter = 'steelblue'
        self.fyll_leave = 'lightblue'

        self.lerret.bind('<Enter>', lambda e: self.lerret.itemconfig(self.rektangel, fill=self.fyll_enter))
        self.lerret.bind('<Leave>', lambda e: self.lerret.itemconfig(self.rektangel, fill=self.fyll_leave))
        self.lerret.bind('<Button-1>', lambda e: self.museklikk(self.ruteliste))

    def endre_tilstand(self, tilstand):
        self.tilstand = tilstand
        if self.tilstand == 'skutt_treff':
            self.fyll_enter = 'indianred'
            self.fyll_leave = 'lightcoral'
        if self.tilstand == 'skutt_bom':
            self.fyll_enter = 'slategray'
            self.fyll_leave = 'gray'
        if self.tilstand == 'skutt_senket':
            self.fyll_enter = 'maroon'
            self.fyll_leave = 'firebrick'

    def museklikk(self, ruteliste):
        # Hvis ruten er tom
        if self.innhold == 0 and self.tilstand == 'ikke_skutt':
            self.endre_tilstand('skutt_bom')
            self.beskjed.set(f'Skudd på rute [{self.y}, {self.x}] bommet.')
            self.data_skyter()
        # Hvis Ruten har et skip i seg
        elif isinstance(self.innhold, Skip) and self.tilstand != 'skutt_treff' and self.tilstand != 'skutt_senket':
            self.endre_tilstand('skutt_treff')
            self.innhold.treff()
            self.beskjed.set(f'Treff på rute [{self.y}, {self.x}].')

            # Hvis alle rutene til skipet er skutt
            if self.innhold.er_senket():
                for koordinat in self.innhold.koordinatliste:
                    for rute in ruteliste:
                        if rute.x == koordinat[0] and rute.y == koordinat[1]:
                            rute.endre_tilstand('skutt_senket')
                            rute.lerret.itemconfig(rute.rektangel, fill='firebrick')
                            self.beskjed.set(f'Treff på rute [{self.y}, {self.x}], skipet er senket.')
                            self.sjekk()
            self.data_skyter()
        # Hvis ruten allerede er skutt på
        else:
            self.beskjed.set(f'Du har allerede skutt på [{self.y}, {self.x}].')


class FiRute:
    def __init__(self, vindu, x, y, innhold, ruteliste, stringvar, sjekk_vinn):
        self.vindu = vindu
        self.innhold = innhold
        self.beskjed = stringvar
        self.sjekk = sjekk_vinn
        self.ruteliste = ruteliste
        self.x = x
        self.y = y
        self.tilstand = 'ikke_skutt'
        self.fyll = 'lightgreen'
        self.lerret = tk.Canvas(self.vindu, width=64, height=64)

        if isinstance(self.innhold, Skip) and self.tilstand != 'skutt_treff' and self.tilstand != 'skutt_senket':
            self.fyll = 'darkgreen'

        self.rektangel = self.lerret.create_rectangle(0, 0, 64, 64, fill=self.fyll)
        self.lerret.itemconfig(self.rektangel, fill=self.fyll)

    def endre_tilstand(self, tilstand):
        self.tilstand = tilstand
        if self.tilstand == 'skutt_treff':
            self.lerret.itemconfig(self.rektangel, fill='lightcoral')
            self.fyll = 'lightcoral'
        if self.tilstand == 'skutt_bom':
            self.lerret.itemconfig(self.rektangel, fill='gray')
            self.fyll = 'gray'

    def data_skyter_rute(self):
        if self.innhold == 0:
            self.endre_tilstand('skutt_bom')

        elif isinstance(self.innhold, Skip) and self.tilstand != 'skutt_treff' and self.tilstand != 'skutt_senket':
            self.endre_tilstand('skutt_treff')
            self.innhold.treff()

            if self.innhold.er_senket():
                for koordinat in self.innhold.koordinatliste:
                    for rute in self.ruteliste:
                        if rute.x == koordinat[0] and rute.y == koordinat[1]:
                            rute.endre_tilstand('skutt_senket')
                            rute.lerret.itemconfig(rute.rektangel, fill='firebrick')
                            self.beskjed.set(f'Treff på rute [{self.y}, {self.x}], skipet er senket.')
                            self.sjekk()


class Skip:
    def __init__(self, start_x, start_y, retning='horisontal', lengde=2):
        self.x_koordinat = start_x
        self.y_koordinat = start_y
        self.retning = retning
        self.lengde = lengde
        self.__antall_treff = 0
        self.koordinatliste = list()
        for i in range(self.lengde):
            if self.retning == 'horisontal':
                self.koordinatliste.append([self.x_koordinat + i, self.y_koordinat])
            else:
                self.koordinatliste.append([self.x_koordinat, self.y_koordinat + i])

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
    data_tur = False
    gui = SpillbrettGUI()
