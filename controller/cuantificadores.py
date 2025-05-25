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