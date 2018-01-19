input_usuario = int(input("¿Que tabla quieres saber? "))

for a in range(2, 11):
    if ( input_usuario* a ) % 2 == 0:
        print("{} * {} = {}".format(input_usuario, a, a * input_usuario))