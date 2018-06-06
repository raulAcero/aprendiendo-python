class Notas:

    def sacar_nota(self):
        self.notas = []
        self.nota = ""
        while self.nota != "ya":
            self.nota = input("Dime tu nota: ")
            try:
                self.notas.append(float(self.nota))
            except ValueError:
                pass
        notas_sumadas = 0
        for i in self.notas:
            notas_sumadas += i
        final = notas_sumadas / len(self.notas)
        print("la nota media es {}".format(final))
        return final

    def calcular_faltas(self):
        numero_faltas = input("¿Cuantas veces has faltado?: ")
        if numero_faltas.isdigit():
            numero_faltas = int(numero_faltas)
            if numero_faltas <= 10:
                return 1
            if 10 < numero_faltas <= 20:
                return 0.5
            if numero_faltas > 20:
                return 0

    def nota_final(self):
        notas_ejercicios = self.sacar_nota()
        notas_practicas = self.sacar_nota()
        nota_examen = self.sacar_nota()
        nota_faltas = self.calcular_faltas()
        nota = round((notas_ejercicios * 0.3) + (notas_practicas * 0.3) + (nota_examen * 0.3) + nota_faltas, 2)
        print("la nota es: {}".format(nota))


par = Notas()
par.nota_final()

