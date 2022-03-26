
"""Clase que contiene los atributos y los métodos estáticos"""

class Conventions:

    tablero_num_lineas = 10
    tablero_num_columnas = 10
        
    barcos_longitud = [2, 3, 3, 4, 4, 5]

       
    def generar_num_linea(x):
        return chr(65 + x)
    
    def generar_num_columna(y):
        return str(y)
    
    def generar_nombre_casilla(self, x, y):
        return self.generar_num_linea(x) + self.generar_num_columna(y)

