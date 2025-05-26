from controller.predicados import Predicados
from view.menu import Menu
from view.validacion import Validacion

lista = []

sent = 0
while(sent != -1):
    print("////////////////////////////////////////////")
    print("Menu, seleccion su opcion")
    print("1. Ingresar el universo, añadir un elemento")
    print("2. Remover un elemento del universo")
    print("3. Eligir proposicion")
    print("4. Salir del programa")
    print("////////////////////////////////////////////")
    print("")

    opc = Validacion.validar("Ingrese la opcion: ")
    print("")
    while opc < 1 or opc > 4:
        print("El valor de la opcion debe ser entre 1 y 4 ")
        print("")
        opc = Validacion.validar("Ingrese la opcion: ")
    if opc == 1:
        cont = 1
        numel = Validacion.validar("Ingrese cuantos numeros desea añadir: ")
        print("")
        while( cont <= numel):
            num = Validacion.validar("Ingrese el numero que desea agregar: ")
            lista.append(num)
            cont +=1
        print("")
        print(lista)
        print("")
        
    elif opc == 2:
        if len(lista) == 0:
            print("")
            print("No existen datos en el universo, por favor ingresar primero los datos ")
            print("")
        else:
            num = Validacion.validar("Ingrese el numero que desea eliminar: ")
            if num in lista:
                lista.remove(num)
            else: 
                print("No se puede remover, un numero que no esta en el dominio ")

            print("")
            print(lista)
            print("")

    elif opc == 3:
        if len(lista) == 0:
            print("")
            print("No existen datos en el dominio, favor ingresar primero los datos ")
            print("")
        else: 
            print("////////////////////////////////////////////")
            print("Menu, seleccion el predicado a evaluar")
            print("1. P(x), x es un numero par")
            print("2. Q(x), x es un numero positivo")
            print("3. R(x), x es un numero negativo")
            print("4. S(x), x es un solo digito")
            print("")
            predicado = Validacion.validar("Seleccione el predicado: ")
            print("")

            while predicado < 1 or predicado > 4:
                print("El valor de la opcion no debe ser entre 1 y 4 ")
                print("")
                predicado = Validacion.validar("Ingrese la opcion: ")
            print("")
            Menu.menu(predicado,lista)
            print("")
    elif opc == 4:
        print("")
        print("Saliendo")
        print("")
        sent = -1