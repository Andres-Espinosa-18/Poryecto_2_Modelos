from controller.predicados import Predicados
from controller.cuantificadores import Cuantificadores

class Menu:
    def __init__ (self):
        self
        
    def menu(opc,lista):
        lista_booleanos = []
        
        if opc == 1:
            for elemento in lista:
                lista_booleanos.append(Predicados.P_x(elemento))
            Cuantificadores.imprimir_todos(lista_booleanos)

        elif opc == 2:
            for elemento in lista:
                lista_booleanos.append(Predicados.Q_x(elemento))
            Cuantificadores.imprimir_todos(lista_booleanos)
        elif opc == 3:
            for elemento in lista:
                lista_booleanos.append(Predicados.R_x(elemento))
            Cuantificadores.imprimir_todos(lista_booleanos)
        elif opc == 4:
            for elemento in lista:
                lista_booleanos.append(Predicados.S_x(elemento))
            Cuantificadores.imprimir_todos(lista_booleanos)