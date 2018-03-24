"""
Antes de comenzar el while principal, preguntar al usuario si desea configurar una alarma, esta alarma sonara una vez al día a la hora que el usuario decida (no hace falta tener los minutos en cuenta).
También el usuario podrá decidir que días de la semana quiere que esta alarma suene o si quiere que suene una fecha en concreto.
Cuando llegue el momento especificado en la alarma, simplemente escribir una nueva linea de texto en el archivo y en pantalla. Esto representaría que la alarma ha sonado.
"""

from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 1


def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)


def alarma():
    hora_alarma = int(input("Dime la hora de la alarma[formato hh]: "))
    if not 0 < hora_alarma < 24:
        print("Esa hora no vale")
        hora_alarma = int(input("Dime una hora válida:"))

    str_hora = str(hora_alarma)
    hora = datetime.datetime.strptime(str_hora, "%H")
    return hora


def dia_alarma(current_time):
    pregunta = ""
    sonar = False
    while pregunta != "Si" and pregunta != "No":
        pregunta = input("¿Quieres que tu alarma suene?[Si/no]: ")
    hoy = datetime.datetime.now()

    if pregunta == "Si":
        dia_o_fecha = ""
        while dia_o_fecha != "dia semana" and dia_o_fecha != "fecha":
            dia_o_fecha = input("¿Quieres que tu alarma suene una dia en concreto de la semana o una fecha[dia semana/fecha]?")

        if dia_o_fecha == "dia semana" and not sonar:
            dia = input("Que dia quieres que suene tu alarma[L,M,X,J,V,S,D]")
            dias_semana = {"L": 0, "M": 1, "X": 2, "J": 3, "V": 4, "S": 5, "D": 6}
            dia_elegido = dias_semana[dia]
            return dia_elegido

        elif dia_o_fecha == "fecha":
            fecha = input("Dime la fecha que quieres poner la alarma[dd/mm/yyyy]: ")
            fecha_alarma = datetime.datetime.strptime(fecha, "%d/%m/%Y")
            while fecha_alarma < hoy:
                print("Esa fecha no vale, debe ser superior a la actual")
                fecha = input("Dime la fecha que quieres poner la alarma[dd/mm/yyyy]: ")
                fecha_alarma = datetime.datetime.strptime(fecha, "%d/%m/%Y")

            return fecha_alarma

    elif pregunta == "No":
        return


def main():
    current_time = datetime.datetime.now()
    is_night = False
    hora_de_alarma = alarma()
    dia_de_alarma = dia_alarma(current_time)

    sonar = False

    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True

        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True

        if current_time.hour == hora_de_alarma.hour:
            write_file_and_screen("Es la hora de la alarma", "horas.txt")

        try:
            if current_time.weekday() == dia_de_alarma and not sonar:
                print("HOY ES EL DÍA DE LA ALARMA\n")
                sonar = True

        except TypeError:
            pass

        try:
            if current_time.date() == dia_de_alarma.date() and not sonar:
                print("HOY ES EL DÍA DE LA ALARMA\n")
                sonar = True
        except TypeError:
            pass


        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
                light_changed = False
            else:
                write_file_and_screen("Se ha hecho de día", "horas.txt")
                light_changed = False


        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")


if __name__ == "__main__":
    main()
