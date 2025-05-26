class Validacion:
    def __init__ (self):
        self  
        
    def validar(mensaje):
        while True:
            entrada = input(mensaje)
            try:
                numero_entero = int(entrada)
                break
            except ValueError:
                print("")
                print("Error, solo se permiten numeros enteros")
                print("")
        return numero_entero