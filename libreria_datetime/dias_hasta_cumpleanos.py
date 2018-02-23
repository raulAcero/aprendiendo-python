"""
Crea un programa que te diga cuando falta para tu cumpleaños y que día de la semana será.
"""

import datetime
print("Voy a averiguar cuantos días faltan para tu cumpleaños y que día de la semana será")
dia = int(input("¿Que día es tu cumpleaños?: "))
mes = int(input("¿Que mes es tu cumpleaños?: "))
hoy = datetime.datetime.now()
if hoy.month < mes or (hoy.month == mes and hoy.day > dia):
    ano = hoy.year
else:
    calc_ano = datetime.datetime.now() + datetime.timedelta(days=365)
    ano = calc_ano.year

cumple = datetime.datetime(day=dia, month=mes, year=ano)
tiempo_restante = cumple - hoy
semana = {"0": "lunes","1": "martes","2": "miercoles", "3": "jueves","4": "viernes","5": "sabado","6": "domingo"}
dia_semana = semana[str(cumple.weekday())]

print("Faltan {} días para tu cumple, será un {}".format(tiempo_restante.days,dia_semana))