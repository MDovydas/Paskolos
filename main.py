import pandas
import numpy
import pickle
import os


class Paskola():
    def __init__(self, suma, terminas, palukanos):
        self.suma = suma
        self.terminas = terminas
        self.palukanos = palukanos
        moketinu_palukanu_suma = 0
        bendra_moketina_suma = 0
        menesio_palukanu_sarasas = []
        menesio_imoku_sarasas = []
        likutine_suma = []
        while terminas > 0:
            likutis = suma / terminas
            menesio_palukanos = suma * (palukanos / 100 / self.terminas)
            menesio_imoka = likutis + menesio_palukanos
            suma = suma - likutis
            moketinu_palukanu_suma = moketinu_palukanu_suma + menesio_palukanos
            bendra_moketina_suma = bendra_moketina_suma + menesio_imoka
            terminas = terminas - 1
            menesio_palukanu_sarasas.append(menesio_palukanos)
            menesio_imoku_sarasas.append(menesio_imoka)
            likutine_suma.append(suma)

        self.moketinu_palukanu_suma = moketinu_palukanu_suma
        self.bendra_moketina_suma = bendra_moketina_suma
        self.menesio_palukanu_sarasas = menesio_palukanu_sarasas
        self.menesio_imoku_sarasas = menesio_imoku_sarasas
        self.likutine_suma = likutine_suma
        grazintina_dalis = []
        mim = 0
        while mim < self.terminas:
            grazintina_dalis.append(self.suma / self.terminas)
            mim = mim + 1
        self.grazintina_dalis = grazintina_dalis

    def paskolos_informacija(self):
        print(
            f"Paskolos suma: {self.suma}\nPaskolos terminas: {self.terminas}\nPaskolos palūkanos: {self.palukanos}\n"
            f"Mokėtinų palūkanų suma: {self.moketinu_palukanu_suma}\nBendra mokėtina suma: {self.bendra_moketina_suma}\n")

    def mokejimo_grafikas(self):
        paskola = {"Grąžintina dalis, Eur": self.grazintina_dalis,
                   "Likutis, Eur": self.likutine_suma,
                   "Priskaičiuotos palūkanos": self.menesio_palukanu_sarasas,
                   "Brendra moketina suma": self.menesio_imoku_sarasas}

        dataframe = pandas.DataFrame(paskola)
        dataframe.index = numpy.arange(1, len(dataframe) +1)
        pandas.set_option('display.max_rows', None)
        pandas.set_option('display.max_columns', None)
        pandas.set_option('display.width', None)
        pandas.set_option('display.max_colwidth', None)
        print(dataframe)
        dataframe.to_csv('last_table.csv')


menu_options = {
    1: 'Įvesti paskolos duomenis',
    2: 'Parodyti paskolos informaciją',
    3: 'Parodyti paskolos mokėjimo grafiką',
    4: 'Baigti darbą',
}
if os.path.exists('data.pkl'):
    file = open('data.pkl', 'rb')
    paskolu_sarasas = pickle.load(file)
    file.close()
else:
    paskolu_sarasas = []


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    in_suma = int(input(f"Įveskite paskolos sumą: "))
    in_terminas = int(input(f"Įveskite paskolos terminą: "))
    in_palukanos = int(input(f"Įveskite palūkanas: "))
    paskolu_sarasas.append(Paskola(in_suma, in_terminas, in_palukanos))


def option2():
    for i in paskolu_sarasas:
        print('----------------')
        i.paskolos_informacija()
        print('----------------')


def option3():
    for i in paskolu_sarasas:
        print('----------------')
        i.mokejimo_grafikas()
        print('----------------')


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Įveskite savo pasirinkimą: '))
        except:
            print('Bloga įvestis, naudokit skaičius 1 - 4')

        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            file = open('data.pkl', 'wb')
            pickle.dump(paskolu_sarasas, file)
            file.close()
            print('Baigta')
            exit()
        else:
            print('Bloga įvestis, naudokit skaičius 1 - 4')
