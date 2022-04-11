#- Crear una función con tres parámetros que sean números que se suman entre sí.
# Llamar a la función en el main y darle valores.

def main ():
    a=5
    b=6
    c=7
    sumaparametros=(a+b+c)
    print(sumaparametros)
main()

# - Crear una clase coche.
# - Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
# - Una función que incremente el número de puertas que tiene el coche.
# - Crear un objeto miCoche en el main y añadirle una puerta.
# - Mostrar el número de puertas que tiene el objeto.

class Coche:
    puertas=''
    numerodepuertas=4
    numerodepuertas2=numerodepuertas+1
    print('el número de puertas inicial es:',numerodepuertas)
    print('el número de puertas incrementado es:', numerodepuertas2)



    def print_puertas(self):
        print(self.puertas)

coche=Coche()#instancia

mustang= Coche()
mustang.puertas='el mustang tiene 5'
mustang.print_puertas()

