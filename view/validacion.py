def validar(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            numero_entero = int(entrada)
            break
        except ValueError:
            print("Error, solo se permiten numeros enteros")
    return numero_entero