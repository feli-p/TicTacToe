# Juego de gato. Proyecto prueba.


class Tablero:
    def __init__(self):
        self.jugadas = [0]*9
        self.tablero = """
        +---+---+---+
        | {} | {} | {} |
        +---+---+---+
        | {} | {} | {} |
        +---+---+---+
        | {} | {} | {} |
        +---+---+---+
        """

    def imprimeTablero(self):
        print(self.tablero.format(*self.jugadas).replace('0','-').replace('1', 'X').replace('-1', 'O'))


class Jugador:
    def __init__(self):
        self.nombre = ""
        self.id = 0

    def setID(self, newID):
        self.id = newID

    def printID(self):
        print(self.id)


class JugadorHumano(Jugador):
    #def __init__(self):
        #super().__init__()
    pass

class CPU(Jugador):
    pass


class Gato():
    def __init__(self):
        self.turno = 0
    

if __name__=='__main__':
    print("Bienvenidos al juego de gato")
    print("Hecho por: losa lucines gpt")
    print("----------------------------")

    tablero = Tablero()
    tablero.imprimeTablero()
    tablero.jugadas[0] = 1
    tablero.imprimeTablero()

    player1 = Jugador()
    player2 = JugadorHumano()
    player3 = CPU()
    player2.setID(1)
    player3.setID(-1)

    player1.printID()
    player2.printID()
    player3.printID()
    