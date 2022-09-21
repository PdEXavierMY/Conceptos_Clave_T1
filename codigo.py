import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def constructor(a=0, b=0):
        punto = [a, b]
        return punto
    
    def string(self, Punto):
        print("("+str(Punto[0])+", "+str(Punto[1])+")")

    def cuadrante(punto):
        if punto[0]>0 and punto[1]>0:
            print("Pertenece al cuadrante 1")
        elif punto[0]<0 and punto[1]>0:
            print("Pertenece al cuadrante 2")
        elif punto[0]>0 and punto[1]<0:
            print("Pertenece al cuadrante 3")
        elif punto[0]<0 and punto[1]<0:
            print("Pertenece al cuadrante 4")
        elif punto[0]==0:
            print("Está sobre el eje x")
        elif punto[1]==0:
            print("Está sobre el eje y")
        elif punto[0]==0 and punto[1]==0:
            print("Está en el eje de coordenadas")

    def vector(Punto1, Punto2):
        vector = [Punto2[0]-Punto1[0], Punto2[1]-Punto1[1]]
        return vector

    def distancia(Punto1, Punto2):
        return math.sqrt(Punto.vector(Punto1, Punto2)[0]**2+Punto.vector(Punto1, Punto2)[1]**2)

class Rectangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def constructor(a=0, b=0, c=0, d=0):
        punto1 = [a, b]
        punto2 = [c, d]
        return punto1, punto2

    def base():

    def altura():

    def area():