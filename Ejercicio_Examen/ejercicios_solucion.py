import random
import pdb

class Coche():
    def __init__(self, nombre, caballos):
        self.nombre=nombre
        self.caballos=caballos

    def to_string(self):
        return "{marca:"+ self.nombre+ ", caballos: "+ self.caballos+ "}"
    
class Carrera():
    def __init__(self, coches):
        self.coches=coches
        self.resultado=[]

    def mostrar_parrilla_de_salida(self):
        aux = 1
        for coche in self.coches:
            print("El coche ", coche.nombre, "sale en [",aux,"] posicion")
            aux = aux+1
    
    def empieza_carrera(self):
        print("La carrera empieza... ")
    
    def finaliza_carrera(self):
        aux = self.coches
        while not len(aux) == 0:
            ran = random.randint(0, len(aux)-1)
            self.resultado.append(aux[ran])
            del aux[ran]

    def muestra_resultado(self):
        for coche in self.resultado:
            print(coche.to_string())

if __name__ == '__main__':
    c1 = Coche("Mercedes", "120hp")
    c2 = Coche("Ferrari", "200hp")
    c3 = Coche("Mustang", "200hp")
    c4 = Coche("mmm", "200hp")
    coches=[c1, c2, c3, c4]

    c = Carrera(coches)
    c.mostrar_parrilla_de_salida()
    c.empieza_carrera()
    c.finaliza_carrera()
    c.muestra_resultado()