
while True:
    print('1. Sumar')
    print('2. Restar')
    print('3. Ver Log')
    print('4. Salir')
    op = int(input('\tSeleccione una opción: '))

    if op == 1:
        try:
            a = int(input('\nIngrese un numero: '))
            b = int(input('Ingrese otro numero: '))

            res = a + b
            print(str(a) + ' + ' + str(b) + ' = ' + str(res) + '\n')
        except:
            print('Ingrese solo valores numéricos')

    elif op == 2:
        #restar
        print('restar')
        break
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