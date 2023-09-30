"""
Este proyecto es un juego de gato (tic tac toe).
Está hecho para practicar programación en Python, por lo que contiene elementos innecesarios para el juego
pero que se usaron para practicar programación con clases en este lenguaje.
"""

import random
import math

class Tablero:
    def __init__(self):
        self.dim = 3
        self.jugadas = [0]*9
        
    def imprimeTablero(self):
        tabla = """
        +---+---+---+
        | {} | {} | {} |
        +---+---+---+
        | {} | {} | {} |
        +---+---+---+
        | {} | {} | {} |
        +---+---+---+
        """
        print(tabla.format(*self.jugadas).replace('0','-').replace('-1', 'O').replace('1', 'X'))


class Jugador:
    def __init__(self):
        self.nombre = ""
        self.id = 0

    def setID(self, newID):
        self.id = newID

    def printID(self):
        print(self.id)


class JugadorHumano(Jugador):
    def __init__(self):
        super().__init__()
    
    def movimiento(self, tablero, ronda):
        bandera = True
        while(bandera):

            bandera2 = True
            while(bandera2):
                entradaUsuario = input("\tEscoge dónde poner tu figura:\t")
                if entradaUsuario.isdigit():
                    index = int(entradaUsuario)
                    if index > 8:
                        print("\t\tIngresa un número entre 0 y 8\n")
                    else:
                        bandera2 = False
                else:
                    print("\t\tIngresa un número entre 0 y 8\n")

            if tablero.jugadas[index] == 0:
                tablero.jugadas[index] = self.id
                bandera = False
            else:
                print("\t\tNúmero inválido, escoge de nuevo.\n")
            

class CPU(Jugador):
    def movimiento(self, tablero, ronda):
        mejorValor = -100000
        index = -1
        for i in range(9):
            if tablero.jugadas[i] != 0:
                continue
            no2 = tablero.jugadas[::]
            no2[i] = self.id
            val = self.minimax(no2,9-(ronda+1),False)
            if val > mejorValor:
                index = i
                mejorValor = val
        tablero.jugadas[index] = self.id;
        
    
    def minimax(self, nodo, depth, jugadorMaxi):
        # determinar si nodo es nodo hoja
        dim2 = len(nodo)
        ronda = 0
        for x in nodo:
            if x != 0:
                ronda += 1

        hoja = False
        heurist = self.heuristica(nodo)
        if dim2 == ronda:
            hoja = True
        elif abs(heurist) >= 10:
            hoja = True

        if depth == 0 or hoja:
            return heurist
        if jugadorMaxi:
            mejorValor = -100000
            for i in range(9):
                if nodo[i] != 0:
                    continue
                no2 = nodo[::]
                no2[i] = self.id
                val = self.minimax(no2,depth-1, False)
                mejorValor = max(mejorValor,val)
            return mejorValor
        else:
            mejorValor = 100000
            for i in range(9):
                if nodo[i] != 0:
                    continue
                no2 = nodo[::]
                no2[i] = -self.id
                val = self.minimax(no2,depth-1, True)
                mejorValor = min(mejorValor,val)
            return mejorValor
            

    def heuristica(self, nodo):
        aux = self.revisarVictoria(nodo)
        if aux == 3*self.id:
            return 1000
        elif aux == 0:
            return random.randint(-7,7)
        else:
            return -1000

    def revisarVictoria(self, nodo):
        resultado = 0
        fin = False
        dim = int(math.sqrt(len(nodo)))
        ronda = 0
        for x in nodo:
            if x != 0:
                ronda += 1
        
        if ronda+1 >= 2*dim-1:
            # Revisar Diagonales
            sum = 0
            for j in range(dim):
                sum += nodo[(dim+1)*j]
            if abs(sum) == dim:
                fin = True
                resultado = sum

            if not(fin):
                sum = 0
                for j in range(dim):
                    sum += nodo[(dim-1)*(j+1)]
                if abs(sum) == dim:
                    fin = True
                    resultado = sum

            # Revisar renglones
            i = 0
            while(not(fin) and i < dim):
                sum = 0
                for j in range(dim):
                    sum += nodo[dim*i+j]
                if abs(sum) == dim:
                    fin = True
                    resultado = sum
                i += 1

            # Revisar columnas
            i = 0
            while(not(fin) and i < dim):
                sum = 0
                for j in range(dim):
                    sum += nodo[i+dim*j]
                if abs(sum) == dim:
                    fin = True
                    resultado = sum
                i += 1
            
        return resultado


class Partida():
    def __init__(self):
        self.tablero = Tablero()
        self.ronda = 0
        self.fin = False
        self.jugadores = []

    def crearJugadores(self):
        print("Introduce el nombre de los jugadores. Si escribes CPU, el jugador correspondiente será la computadora.")
        name1 = input("\tJugador 1:\n\t\t")
        if name1 != 'CPU':
            jugador1 = JugadorHumano()
            jugador1.nombre = name1
        else:
            jugador1 = CPU()
            jugador1.nombre = 'CPU 1'
        jugador1.setID(1)

        name2 = input("\tJugador 2:\n\t\t")
        if name2 != 'CPU':
            jugador2 = JugadorHumano()
            jugador2.nombre = name2
        else:
            jugador2 = CPU()
            jugador2.nombre = 'CPU 2'
        jugador2.setID(-1)

        self.jugadores.append(jugador1)
        self.jugadores.append(jugador2)
        print("\n")
    
    def jugada(self):
        print(f"Ronda {self.ronda+1}: ",end = '')
        aux = self.ronda % 2
        print(f"Turno de {self.jugadores[aux].nombre}")
        
        self.jugadores[aux].movimiento(self.tablero, self.ronda)
        
        self.tablero.imprimeTablero()
        self.ronda += 1

    def revisarVictoria(self):
        resultado = 0
        if self.ronda+1 >= 2*self.tablero.dim-1:
            # Revisar Diagonales
            sum = 0
            for j in range(self.tablero.dim):
                sum += self.tablero.jugadas[(self.tablero.dim+1)*j]
            resultado = self.checksum(sum)

            if not(self.fin):
                sum = 0
                for j in range(self.tablero.dim):
                    sum += self.tablero.jugadas[(self.tablero.dim-1)*(j+1)]
                resultado = self.checksum(sum)

            # Revisar renglones
            i = 0
            while(not(self.fin) and i < self.tablero.dim):
                sum = 0
                for j in range(self.tablero.dim):
                    sum += self.tablero.jugadas[self.tablero.dim*i+j]
                resultado = self.checksum(sum)
                i += 1

            # Revisar columnas
            i = 0
            while(not(self.fin) and i < self.tablero.dim):
                sum = 0
                for j in range(self.tablero.dim):
                    sum += self.tablero.jugadas[i+self.tablero.dim*j]
                resultado = self.checksum(sum)
                i += 1
            
        return resultado

    def checksum(self, sum):
        resultado = 0
        if abs(sum) == self.tablero.dim:
            self.fin = True
            resultado = sum
        return resultado
            
    def iniciaPartida(self):
        self.crearJugadores()
        ganador = 0
        while(not(self.fin) and self.ronda < 9):
            self.jugada()
            ganador = self.revisarVictoria()
        if ganador == 0:
            print("¡Ha sido un empate!")
        else:
            i = 1
            if ganador == self.tablero.dim:
                i = 0
            print(f"Felicidades, {self.jugadores[i].nombre}. ¡Ganaste!")
            
        print("¡Gracias por jugar!")
        
        
if __name__=='__main__':
    print("""
            Bienvenidos al juego de gato
            Hecho por: losa lucines gpt
        ------------------------------------
          """)

    juego = Partida()
    juego.iniciaPartida()
    