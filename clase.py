
class Ventana:
    __titulo = ""
    __valorXsupI = 0
    __valorYsupI = 0
    __valorXinfD = 0
    __valorYinfD = 0


    def __init__(self, titulo, valorXsupI=0, valorYsupI=0, valorXinfD=50, valorYinfD=50):
        self.__titulo = titulo
        #Si el valorXsupI es menor que cero, la función max retorna cero. En caso contrario, retorna valorXsupI.
        self.__valorXsupI = max(0,valorXsupI)
        self.__valorYsupI = max(0,valorYsupI)
        ##Si el valorXsupI es mayor que 500, la función max retorna 500. En caso contrario, retorna valorYsupI.
        self.__valorXinfD = min(500,valorXinfD)
        self.__valorYinfD = min(500,valorYinfD)

    def mostrar(self):
        return print(f"Titulo: {self.__titulo}\nCoordenadas Vertice Superior Izquierdo: X= {self.__valorXsupI}\tY= {self.__valorYsupI} \nCoordenadas Vertice Inferior Derecho:   X= {self.__valorXinfD}\tY= {self.__valorYinfD}")
    

    def getTitulo(self):
        return self.__titulo
    
    def alto(self):
        return self.__valorXinfD - self.__valorXsupI
    
    def ancho(self):
        return self.__valorYsupI - self.__valorYinfD
    
    def moverDerecha(self, default = 1):
        self.__valorXinfD += default
        self.__valorXsupI += default

    def moverIzquierda(self, default= 1):
        self.__valorXinfD -= default
        self.__valorXsupI -= default

    def bajar(self, default= 1):
        self.__valorYinfD -= default
        self.__valorYsupI -= default

    def subir(self, default= 1):
        self.__valorYinfD += default
        self.__valorYsupI += default