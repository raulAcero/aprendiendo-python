"""
Reemplazar letras de una string introducida por el usuario
"""

valor_reemplazar = ["VACA"]
string_usuario = input("Escribeme una frase: ")

for valor in valor_reemplazar:
    string_usuario = string_usuario.replace("A", valor)
    string_usuario = string_usuario.replace("a", valor)

print("La frase es, {}".format(string_usuario))