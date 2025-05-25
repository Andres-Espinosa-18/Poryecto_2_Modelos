
from controller.proposiciones import Proposiciones
from view.menu import menu
from view.validacion import validar

lista = []

sent = 0
while(sent != -1):
    print("////////////////////////////////////////////")
    print("Menu, seleccion su opcion")
    print("1. Ingresar el universo, añadir un elemento")
    print("2. Remover un elemento del universo")
    print("3. Eligir proposicion")
    print("4. Salir del programa")

    opc = validar("Ingrese la opcion: ")
    if opc == 1:
        cont = 1
        numel = validar("Ingrese cuantos numeros desea añadir: ")
        while( cont <= numel):
            num = validar("Ingrese el numero que desea agregar: ")
            lista.append(num)
            cont +=1
        print(lista)
        
    elif opc == 2:
        if len(lista) == 0:
            print("No existen datos en el universo, por favor ingresar primero los datos ")
        else:
            num = validar("Ingrese el numero que desea eliminar: ")
            if num in lista:
                lista.remove(num)
            else: 
                print("No se puede remover, un numero que no esta en el dominio ")

            print(lista)

    elif opc == 3:
        if len(lista) == 0:
            print("No existen datos en el dominio, favor ingresar primero los datos ")
        else: 
            print("////////////////////////////////////////////")
            print("Menu, seleccion el predicado a evaluar")
            print("1. P(x), x es un numero par")
            print("2. Q(x), x es un numero positivo")
            print("3. R(x), x es un numero negativo")
            print("4. S(x), x es un solo digito")
            predicado = validar("Seleccione el predicado: ")
            menu(predicado,lista)
    elif opc == 4:
        print("Saliendo")
        sent = -1