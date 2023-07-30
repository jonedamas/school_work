import random
import tkinter
import tkinter.messagebox


class BasisGUI:
    def __init__(self):
        self.mainwindow = tkinter.Tk()
        self.random_num = random.randint(1, 1000)
        self.try_string = tkinter.StringVar()
        self.hint_string = tkinter.StringVar()
        self.high_score_string = tkinter.StringVar()
        self.trys = 0
        self.try_string.set('Du har brukt 0 forsøk')
        self.last_number = 0
        self.high_score = 0
        self.high_score_string.set('')

        self.text_1 = tkinter.Label(self.mainwindow, text="Gjett et tall fra 1 til 1000:")
        self.text_2 = tkinter.Label(self.mainwindow, textvariable=self.try_string)
        self.text_3 = tkinter.Label(self.mainwindow, textvariable=self.hint_string)
        self.high_score_text = tkinter.Label(self.mainwindow, textvariable=self.high_score_string)
        self.text_input = tkinter.Entry(self.mainwindow, width=15)
        self.button = tkinter.Button(self.mainwindow, text='Gjett tall', command=self.button_press)

        self.text_1.grid(row=0, column=0)
        self.text_input.grid(row=0, column=1)
        self.text_2.grid(row=1, column=0)
        self.button.grid(row=1, column=1)
        self.text_3.grid(row=2)
        self.high_score_text.grid(row=3)

        tkinter.mainloop()

    def button_press(self):
        number = int(self.text_input.get())
        self.trys += 1
        self.try_string.set(f'Du har brukt {self.trys} forsøk')
        if self.random_num == number:
            self.hint_string.set('Riktig tall.')
            tkinter.messagebox.showinfo(message=f'Du gjettet riktig! Du brukte {self.trys} forsøk.')
            restart_box = tkinter.messagebox.askquestion(message='Vil du spille på nytt?')
            if restart_box == 'yes':
                if self.trys < self.high_score or self.high_score == 0:
                    self.high_score_string.set(f'high score: {self.trys}')
                    self.high_score = self.trys
                self.restart()
            else:
                self.mainwindow.destroy()

        else:
            if number < self.random_num:
                if abs(self.random_num - number) < abs(self.random_num - self.last_number):
                    self.hint_string.set('Tallet er høyere, du er nærmere enn forige tall.')
                else:
                    self.hint_string.set('Tallet er høyere, du lenger unna enn forige tall')
            else:
                if abs(self.random_num - number) < abs(self.random_num - self.last_number):
                    self.hint_string.set('Tallet er lavere, du er nærmere enn forige tall.')
                else:
                    self.hint_string.set('Tallet er lavere, du lenger unna enn forige tall')
        self.last_number = number

    def restart(self):
        self.trys = 0
        self.try_string.set('Du har brukt 0 forsøk')
        self.last_number = 0
        self.random_num = random.randint(1, 1000)
        self.hint_string.set('')


if __name__ == '__main__':
    gui = BasisGUI()
