class Calculadora:
    def __init__(self):
        pass
    
    def ingresar_valores(self, solo_uno=False):
        try:
            a = float(input('Ingrese el primer valor: '))
            if solo_uno:
                return a, None
            b = float(input('Ingresa el segundo valor: '))
            return a, b
            
        except ValueError:
            print('Error: por favor ingrese valores numericos validos.')
            return None, None
        
    def suma(self, a, b):
        return a + b
    
    def resta(self, a, b):
        return a - b
    
    def multiplicacion(self, a, b):
        return a * b
    
    def division(self, a, b):
        if b == 0:
            return "Error: no se puede dividir entre cero."
        return a / b
    
    def potencia(self, a, b):
        return a ** b
    
    def raiz_cuadrada(self, a):
        if a < 0:
            return 'Error, no se puede calcular raiz de un numero negativo'
        return a ** 0.5
    
    def seleccionar_operacion(self):
        print('\nSeleccione una operacion:')
        print('1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Potencia\n6. Raiz cuadrada')
        
        opcion = input('seleccione una operacion: ')
        return opcion
    
calc = Calculadora()
opcion = calc.seleccionar_operacion()

if opcion in ['1', '2', '3', '4', '5']:
    a, b = calc.ingresar_valores()
    if a is not None and b is not None:
        if opcion == '1':
            print(f'Resultado de la suma: {calc.suma(a, b)}')
        elif opcion == '2':
            print(f'Resultado de la resta: {calc.resta(a, b)}')
        elif opcion == '3':
            print(f'Resultado de la multiplicacion: {calc.multiplicaion(a, b)}')
        elif opcion == '4':
            print(f'Resultado de la division: {calc.division(a, b)}')
        elif opcion == '5':
            print(f' Resultado de la potencia: {calc.potencia(a, b)}')
elif opcion == '6':
    a, _ = calc.ingresar_valores(solo_uno=True)
    if a is not None:
        print(f'Resultado de la raiz cuadrada: {calc.raiz_cuadrada(a)}')
    else:
        print('opcion no valida, intenta de nuevo')