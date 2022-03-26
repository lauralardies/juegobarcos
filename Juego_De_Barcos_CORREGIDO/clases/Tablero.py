import sys
#LRL: Importar product de la libreria itertools
from itertools import product

#LRL: Importar la clase Barco
from clases.Barco import Barco
from clases.Conventions import Conventions
from clases.Case import Case
from introducir.cadena import solicitar_introducir_casilla

#LRL: Define las variables que son globales en un juego
casillas_ocupadas = []
instances = {}
jugadas = {}


class Tablero:
    def __init__(self):

        self.casillas_ocupadas = set()
        
        # Creamos las casillas:
        Case.generar_casillas(instances)

        # Creamos los barcos:
        Barco.generar_barcos(instances,self.casillas_ocupadas)

        # performance / legibilidad:
        num_lineas = Conventions.tablero_num_lineas
        num_columnas = Conventions.tablero_num_columnas
        num2l = Conventions.generar_num_linea
        num2c = Conventions.generar_num_columna

        # Creamos la herramienta para poder seguir la situación
        self.casillas_jugadas = []

        # Generamos aquí los etiquetas para facilitar la visualización
        self.etiqueta_lineas = [num2l(x) for x in range(num_lineas)]
        self.etiqueta_columnas = [num2c(x) for x in range(num_columnas)]

        self.trazo_horizontal = " --" + "+---" * 10 + "+"

    def ver(self):
        print("   |", " | ".join(self.etiqueta_columnas), "|")

        iter_etiqueta_lineas = iter(self.etiqueta_lineas)

        for x, y in product(range(Conventions.tablero_num_lineas),
                            range(Conventions.tablero_num_columnas)):

            # Trazo horizontal para cada nueva línea
            if y == 0:
                print(self.trazo_horizontal)
                print(" {}".format(next(iter_etiqueta_lineas)), end="")

            #LRL: Instances no pertenece a la clase Case
            casilla = instances[x, y]
            print(" |", casilla, end="")

            # Ver la barra vertical derecha de la tabla:
            if y == 9:
                print(" |")
        # Ver la última línea horizontal
        print(self.trazo_horizontal + "\n\n")

    def probar_fin_juego(self):
        """Permite probar si el juego ha terminado o no"""
        #LRL: casillas ocupadas se actualiza segun se van descubriendo barcos
        # Fin del juego, cuando no queden mas casillas ocupadas
        if len(self.casillas_ocupadas) == 0:
            print("Bravo. El juego ha terminado !")
            return True

        return False

    def jugar_tirada(self):
        """Permite gestionar el dato introducido de una tirada"""
        while True:
            nombre_casilla = solicitar_introducir_casilla(
                "Seleccionar una casilla (letra + cifra)")
            #LRL: Instances no pertenece a la clase Case
            # Encontrar la casilla a partir de su nombre
            casilla = instances[nombre_casilla]
            # Probar si la casilla ya ha sido jugada
            if casilla.jugada:
                print("Esta casilla ya ha sido jugada, elija otra",
                      file=sys.stderr)
            else:
                casilla.jugar()
                if (nombre_casilla in self.casillas_ocupadas): 
                    self.casillas_ocupadas.remove(nombre_casilla)
                break
