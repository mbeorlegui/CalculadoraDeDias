from datetime import date
from colorama import Fore, Back, Style


def main():
    while True:
        while True:
            print("     Elija la acción a realizar")
            print("1. Diferencia entre hoy y un día a seleccionar")
            des = input("2. Diferencia entre dos días a seleccionar  ")

            if des == '1':
                hoy = date.today()
                dia = input("Ingrese el dia de hoy con el formato DD-MM-AAAA: ")
                dia = str(dia).split('-')
                dia = date(int(dia[2]), int(dia[1]), int(dia[0]))
                dif = abs((dia - hoy).days)
                print(Fore.YELLOW + "La diferencia de dias entre hoy y la fecha "
                      "seleccionada es de {} dias".format(dif))
                print("{} meses".format(dif/30.4167))
                print("{} horas".format(dif*24))
                print("{} minutos".format(dif*24*60))
                print("{} segundos".format(dif*24*60*60) + Fore.RESET)
                break
            elif des == '2':
                dia1 = input("Ingrese el primer dia de con el formato DD-MM-AAAA: ")
                dia2 = input("Ingrese el segundo dia de con el formato DD-MM-AAAA: ")
                dia1 = str(dia1).split('-')
                dia2 = str(dia2).split('-')
                dia1 = date(int(dia1[2]), int(dia1[1]), int(dia1[0]))
                dia2 = date(int(dia2[2]), int(dia2[1]), int(dia2[0]))
                dif = abs((dia1 - dia2).days)
                print(Fore.YELLOW + "La diferencia de dias entre cambas fechas seleccionadas "
                      "es de {} dias, lo que es igual a:".format(dif))
                print("{} meses".format(dif/30.4167))
                print("{} horas".format(dif*24))
                print("{} minutos".format(dif*24*60))
                print("{} segundos".format(dif*24*60*60) + Fore.RESET)
                break
            else:
                print(Fore.RED + "Ingreso incorrecto. Reingresar.\n" + Fore.RESET)

        cont = input("Desea realizar otra consulta? [S/n] ")
        if cont == 'n' or cont == 'N':
            break


main()