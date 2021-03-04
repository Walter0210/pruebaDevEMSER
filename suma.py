import logging

def operacion(flag):
    strRes = False
    try:
        a = float(input('Ingrese un numero: '))
        b = float(input('Ingrese otro numero: '))
        if flag:
            res = a + b
            strRes = ('\n\t' + str(a) + ' + ' + str(b) + ' = ' + str(res))
            
        else:
            res = a - b
            strRes = ('\n\t' + str(a) + ' - ' + str(b) + ' = ' + str(res))
    except:
        print('\n\tIngrese solo valores numéricos!\n\n')
    finally:
        return strRes

log = open("logger.txt", "w")
while True:
    
    print('\n.::Menú principal::.')
    print('1. Sumar')
    print('2. Restar')
    print('3. Ver Log')
    print('4. Salir')
    try:
        op = int(input('\tSeleccione una opción: '))

        if op == 1:
            print("\t\nSuma de dos números:")
            sum = operacion(True)
            if sum != False:
                log = open("logger.txt", "a")
                print(sum)
                log.write(sum)
                log.close()
            
            
        elif op == 2:
            print("\t\nResta de dos números:")
            rest = operacion(False)
            if rest != False:
                log = open("logger.txt", "a")
                print(rest)
                log.write(rest)
                log.close()

        elif op == 3:    
            print("\t\nRegistro de operaciones:")
            log = open("logger.txt", "r")   
            print(log.read())
            log.close()

        elif op == 4:
            print("Gracias! nos vemos!")
            break
    except:
        print('Seleccione una opcion valida!')