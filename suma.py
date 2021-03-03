def operacion(flag):
    try:
        a = float(input('\nIngrese un numero: '))
        b = float(input('Ingrese otro numero: '))
        if flag:
            res = a + b
            print('\n\t' + str(a) + ' + ' + str(b) + ' = ' + str(res) + '\n')
        else:
            res = a - b
            print('\n\t' + str(a) + ' - ' + str(b) + ' = ' + str(res) + '\n')
    except:
        print('\n\tIngrese solo valores numéricos!\n\n')


while True:
    
    print('1. Sumar')
    print('2. Restar')
    print('3. Ver Log')
    print('4. Salir')
    op = int(input('\tSeleccione una opción: '))

    if op == 1:
        operacion(True)

    elif op == 2:
        operacion(False)

    elif op == 3:
        #logger
        print('log')
        break

try:
    a = int(input('Ingrese un numero: '))
    b = int(input('Ingrese otro numero: '))

    res = a + b
    print(res)
except:
    print('Ingrese solo valores numéricos')