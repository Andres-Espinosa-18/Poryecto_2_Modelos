from controller.proposiciones import Proposiciones
from controller.cuantificadores import Cuantificadores


def menu(opc,lista):
    lista_booleanos = []
    
    if opc == 1:
        for elemento in lista:
            lista_booleanos.append(Proposiciones.P_x(elemento))
        print("Para todos los valores del dominio, la veracidad es: ", Cuantificadores.para_todos(lista_booleanos))
        print("Existe almenso un elemento del dominio, la veracidad es: ", Cuantificadores.existe(lista_booleanos))
        print("Existen un unico valor del dominio, la veracidad es: ", Cuantificadores.existe_un_unico(lista_booleanos))
        print("No existe ni un valor para el dominio, la veracidad es: ", Cuantificadores.no_existe(lista_booleanos))

    elif opc == 2:
        for elemento in lista:
            lista_booleanos.append(Proposiciones.Q_x(elemento))
        print("Para todos los valores del dominio, la veracidad es: ", Cuantificadores.para_todos(lista_booleanos))
        print("Existe almenso un elemento del dominio, la veracidad es: ", Cuantificadores.existe(lista_booleanos))
        print("Existen un unico valor del dominio, la veracidad es: ", Cuantificadores.existe_un_unico(lista_booleanos))
        print("No existe ni un valor para el dominio, la veracidad es: ", Cuantificadores.no_existe(lista_booleanos))
    elif opc == 3:
        for elemento in lista:
            lista_booleanos.append(Proposiciones.R_x(elemento))
        print("Para todos los valores del dominio, la veracidad es: ", Cuantificadores.para_todos(lista_booleanos))
        print("Existe almenso un elemento del dominio, la veracidad es: ", Cuantificadores.existe(lista_booleanos))
        print("Existen un unico valor del dominio, la veracidad es: ", Cuantificadores.existe_un_unico(lista_booleanos))
        print("No existe ni un valor para el dominio, la veracidad es: ", Cuantificadores.no_existe(lista_booleanos))
    elif opc == 4:
        for elemento in lista:
            lista_booleanos.append(Proposiciones.S_x(elemento))
        print("Para todos los valores del dominio, la veracidad es: ", Cuantificadores.para_todos(lista_booleanos))
        print("Existe almenso un elemento del dominio, la veracidad es: ", Cuantificadores.existe(lista_booleanos))
        print("Existen un unico valor del dominio, la veracidad es: ", Cuantificadores.existe_un_unico(lista_booleanos))
        print("No existe ni un valor para el dominio, la veracidad es: ", Cuantificadores.no_existe(lista_booleanos))