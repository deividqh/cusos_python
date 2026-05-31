# import numpy as np

def calcula_pendiente():
    """
        Aplica el método de descenso de gradiente para encontrar el mínimo de la función f(x) = x^2
    """
    x_inicial = 10          # empiezas el calculo en la cima(lejos del minimo donde quiero llegar).
    tasa_aprendizaje = 0.1  # el tamaño del paso que se da en cada iteración. (Learning Rate).
    num_iteraciones = 20    # cuantos pasos doy para bajar la curva hacia el valle(minimo).

    x = x_inicial
    print(f'inicio: arrancan en posicion x=x_inicial={x_inicial}')

    def derivada(x):
        """
            Calcula la pendiente de una curva f(x) = x^2 en un punto dado x 
        """
        return 2 * x

    for i in range(num_iteraciones):
        pendiente = derivada(x)                         # calculo la pendiente en el punto actual
        x = x - tasa_aprendizaje * pendiente            # actualizo x restando el paso dado por la pendiente
        coste = x**2                                   # calculo el coste (valor de la función) en el nuevo punto
        
        print(f'iteracion {i+1}: x={x:8.4f}, pendiente={pendiente:.4f}')
