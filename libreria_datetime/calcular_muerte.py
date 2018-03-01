"""
Programa que calcula la fecha de la muerte
"""
import random
import datetime

VIDA_MEDIA = 80
PENALIZACION_FUMADOR = 10
PENALIZACION_BEBEDOR = 10
PENALIZACION_DEPORTISTA = 10

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

anos_perdidos = int(fumar + beber + deportista)

esperanza_vida = random.randint(VIDA_MEDIA/2, VIDA_MEDIA) - anos_perdidos

muerte = fecha_nacimiento + datetime.timedelta(days=esperanza_vida*365)
fecha_muerte = muerte.strftime("%d de %B del %Y")
dias_restantes = muerte - datetime.datetime.now()

print("Vas a morir el día {}, te quedan {} días".format(fecha_muerte, dias_restantes.days))