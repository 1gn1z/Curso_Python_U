"""import math

def diagonal_rectangulo():
    base = int(input('Base: '))                                  
    altura =int(input('Altura: '))                                  
    diagonal = base*base + altura*altura       
    diagonal = math.sqrt(diagonal)              
    return diagonal                                

print(f'El diagonal del rectángulo es:',diagonal_rectangulo())

#



def diagonal_rectangulo(ancho, alto):
    '''(number, number) -> float
    Devuelve la diagonal de un rectángulo al pasarle su ancho y alto.
    >>> diagonal_rectangul0(10, 6)
    11.66
    >>> diagonal_rectangulo(34.6, 56.4)
    66.16'''
    suma_cuadrados = (ancho**2) + (alto**2)
    diagonal = math.sqrt(suma_cuadrados)

"""
color = 'verde'

if color == 'verde':
    print('¡Puedes pasar!')
elif color == 'naranja':
    print('¡Pasa con precaución!')
else:
    print('¡Espera')

    
