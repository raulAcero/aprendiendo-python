"""
Crea un programa que te diga, introduciendo cualquier fecha, cuantas horas han pasado desde ese momento.
"""

import datetime
print("Voy a averiguar cuantos horas han pasado desde la fecha que introduzcas[debe ser inferior a ahora]")
dia = int(input("¿Que día?: "))
mes = int(input("¿Que mes?: "))
ano = int(input("¿Que año?: "))
hoy = datetime.datetime.now()
fecha = datetime.datetime(year=ano, month=mes, day=dia)

while fecha > hoy:
    print("esa fecha no vale")
    dia = int(input("¿Que día?: "))
    mes = int(input("¿Que mes?: "))
    ano = int(input("¿Que año?: "))
    fecha = datetime.datetime(year=ano, month=mes, day=dia)

diferencia = datetime
resta = hoy - fecha
diferencia = resta.total_seconds() / 3600

print(diferencia)