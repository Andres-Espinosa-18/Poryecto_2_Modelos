def validar():
    while True:
        entrada = input("Por favor, ingrese un número entero: ")
        try:
            numero_entero = int(entrada)
            # Si la conversión a int() tiene éxito, 'numero_entero' contendrá el valor entero.
            # Puedes salir del bucle ya que la entrada es válida.
            print(f"¡Excelente! Ingresaste el entero: {numero_entero}")
            break  # Sale del bucle while
        except ValueError:
            # Si la conversión falla, se ejecuta este bloque.
            print("¡Error! La entrada no es un número entero válido. Inténtelo de nuevo.")
    pass