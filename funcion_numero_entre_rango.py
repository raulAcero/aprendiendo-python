"""
Escribe una funcion que dado un numero y un rango (otros dos numeros), compruebe que ese numero está entre los dos (dentro del rango).
"""

print("Dime un numero, un rango y te diré si el primer número está dentro de ese rango")
numero = int(input("Numero elegido "))
rango_inicial = int(input("Rango inicial "))
rango_final = int(input("Rango final "))

def numero_dentro_de_rango(numero, rango_inicial, rango_final):
    verificar = False
    if numero > rango_inicial and numero < rango_final:
        verificar = True
    return verificar

print(numero_dentro_de_rango(numero, rango_inicial, rango_final))