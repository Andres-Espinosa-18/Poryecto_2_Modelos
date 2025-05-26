class Predicados:
    def __init__ (self):
        self
    
    #funcion proposicional P(x) x es un numero par

    def P_x(x):
        return x % 2 == 0
    
    #funcion proposicional Q(x) x positivo

    def Q_x(x):
        return x > 0
    
    #funcion proposicional R(x) x es negativo

    def R_x(x):
        return x < 0
    
    #funcion proposicional S(x) x con un diginito
    
    def S_x(x):
        return x >= -9 and x <= 9

    