def Calculator():

    print('''Este programa es una calculadora basica, solo introduce
          el primer numero de la operacion y a continueacion elige el operador
          seguido del segundo numero del operador
          \nSuma: 1, Resta: 2, Multiplicacion: 3, Division: 4,''')
    
    operador1 = float(input('introduce el primer valor: '))
    operador = input('selecciona el operador: ')
    operador2 = float(input('Escribe el segundo valor: '))
    
    if operador == '1':
        resultado = operador1 + operador2
        print(resultado)
    elif operador == '2':
        resultado = operador1 - operador2
        print(resultado)
    elif operador == '3':
        resultado = operador1 * operador2
        print(resultado)
    elif operador == '4':
        print(resultado)
        
Calculator()