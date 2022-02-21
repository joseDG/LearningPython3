#NOTE Creacion de Composicion 

class Coordenada:
    def __init__(self, x, y):
        self.X = x 
        self.Y = y 
    
    def MostrarCoordenada(self):
        print("(",self.X,",",self.Y,")")

class Cuadrado:
    def __init__(self, v1, v2, v3, v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    def MostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices:")
        self.V1.MostrarCoordenada()
        self.V2.MostrarCoordenada()
        self.V3.MostrarCoordenada()
        self.V4.MostrarCoordenada()

v1 = Coordenada(1,1)
v2 = Coordenada(4,1)
v3 = Coordenada(4,4)
v4 = Coordenada(1,4)

cuadrado = Cuadrado(v1,v2,v3,v4)
cuadrado.MostrarVertices()
