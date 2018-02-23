"""
Crea un programa que te diga la fecha de hace 5 días respecto a hoy, y el día de la semana.
"""
import datetime

semana = {"0": "lunes","1": "martes","2": "miercoles", "3": "jueves","4": "viernes","5": "sabado","6": "domingo"}
hoy = datetime.datetime.now()
restar = datetime.timedelta(days=5)
hace_cinco_dias = hoy - restar
dia_semana = semana[str(hace_cinco_dias.weekday())]

print(hace_cinco_dias.date(),dia_semana)