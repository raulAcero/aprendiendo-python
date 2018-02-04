string_usuario = input("Dime algo compi: ")
vocales = ["a", "e", "i", "o", "u"]

for letras in vocales:
    string_usuario = string_usuario.replace("a", "i")
    string_usuario = string_usuario.replace("e", "i")
    string_usuario = string_usuario.replace("o", "i")
    string_usuario = string_usuario.replace("u", "i")

print(string_usuario)
