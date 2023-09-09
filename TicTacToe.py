import random


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





if __name__=='__main__':
    print("Bienvenidos al juego de gato")
    print("Hecho por: losa lucines gpt")
    print("----------------------------")

    tablero = Tablero()
    tablero.imprimeTablero()
    tablero.jugadas[0] = 1
    tablero.imprimeTablero()