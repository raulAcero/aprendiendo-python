"""
Programa que calcula la fecha de la muerte
"""
import random
import datetime

VIDA_MEDIA = 80
PENALIZACION_FUMADOR = 10
PENALIZACION_BEBEDOR = 10
PENALIZACION_DEPORTISTA = 10
ALIMENTACION = random.randint(0,15)

def preguntar_si_no(pregunta,actividad):
    respuesta = ""
    while respuesta != "Si" and respuesta != "No" and respuesta != "A veces":
        respuesta = input(pregunta + " [Si/No/A veces]: ")
    respuesta_si = actividad
    respuesta_a_veces = actividad / 2
    if respuesta == "Si":
        salida = random.uniform(0.6, 1) * respuesta_si
        return salida
    if respuesta == "A veces":
        salida = random.uniform(0.6, 1) * respuesta_a_veces
        return salida

print("Voy a averiguar cuanto tiempo tienes de vida.")

nacimiento = input("Dime tu fecha de nacimiento para que averigue cuantos días te quedan[formato dd/mm/yyyy]")
fecha_nacimiento = datetime.datetime.strptime(nacimiento, "%d/%m/%Y")

fumar = preguntar_si_no("¿Fumas?", PENALIZACION_FUMADOR) or 0
beber = preguntar_si_no("¿Bebes?", PENALIZACION_BEBEDOR) or 0
deportista = preguntar_si_no("¿Haces deporte?", -PENALIZACION_DEPORTISTA) or 0
dieta = preguntar_si_no("¿Haces una dieta equilibrada?", -ALIMENTACION) or 0

anos_perdidos = int(fumar + beber + deportista)

esperanza_vida = random.randint(VIDA_MEDIA/2, VIDA_MEDIA) - anos_perdidos

muerte = fecha_nacimiento + datetime.timedelta(days=esperanza_vida*365)
fecha_muerte = muerte.strftime("%d de %B del %Y")
dias_restantes = muerte - datetime.datetime.now()

semana = {"0": "lunes","1": "martes","2": "miercoles", "3": "jueves","4": "viernes","5": "sabado","6": "domingo"}
dia_semana = semana[str(muerte.weekday())]

print("Vas a morir el día {}, será un {}, te quedan {} días".format(fecha_muerte, dia_semana, dias_restantes.days))