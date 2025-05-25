from controller.proposiciones import Proposiciones
from controller.cuantificadores import Cuantificadores

def menu(opc,lista):
    lista_booleanos = []
    
    if opc == 1:
        for elemento in lista:
            lista_booleanos.append(Proposiciones.P_x(elemento))
        Cuantificadores.imprimir_todos(lista_booleanos)

    elif opc == 2:
        for elemento in lista:
            lista_booleanos.append(Proposiciones.Q_x(elemento))
        Cuantificadores.imprimir_todos(lista_booleanos)
    elif opc == 3:
        for elemento in lista:
            lista_booleanos.append(Proposiciones.R_x(elemento))
        Cuantificadores.imprimir_todos(lista_booleanos)
    elif opc == 4:
        for elemento in lista:
            lista_booleanos.append(Proposiciones.S_x(elemento))
        Cuantificadores.imprimir_todos(lista_booleanos)