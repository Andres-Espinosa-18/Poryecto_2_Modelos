traduccion = {True: "Verdadera", False: "Falsa"}
class Cuantificadores:
    def __init__ (self):
        self
    
    def para_todos(dominio):
        for dato in dominio:
            if dato == False:
                return False
        return True
        
    def existe(dominio):
        for dato in dominio:
            if dato == True:
                return True
        return False
    
    def existe_un_unico(dominio):
        cont = 0
        for dato in dominio:
            if dato == True:
                cont +=1
        if cont == 1:
            return True
        else:
            return False
    

    def no_existe(dominio):
        for dato in dominio:
            if dato == True:
                return False
        return True
    
    def imprimir_todos(lista):
        print("Evaluando el predicado con el cuantificador Para todo, la veracidad es: ", traduccion[Cuantificadores.para_todos(lista)])
        print("Evaluando el predicado con el cuantificador Existe almenos uno, la veracidad es: ", traduccion[Cuantificadores.existe(lista)])
        print("Evaluando el predicado con el cuantificador Existe un unico, la veracidad es: ", traduccion[Cuantificadores.existe_un_unico(lista)])
        print("Evaluando el predicado con el cuantificador No existe ninguno, la veracidad es: ", traduccion[Cuantificadores.no_existe(lista)])