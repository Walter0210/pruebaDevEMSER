import logging
logging.basicConfig(filename="logger.txt", level=logging.DEBUG)

def operacion(flag):
    strRes = False
    try:
        a = float(input('Ingrese un numero: '))
        b = float(input('Ingrese otro numero: '))
        if flag:
            res = a + b
            strRes = ('\t' + str(a) + ' + ' + str(b) + ' = ' + str(res))
            
        else:
            res = a - b
            strRes = ('\t' + str(a) + ' - ' + str(b) + ' = ' + str(res))
    except:
        logging.warning('La operación necesita valores numéricos.')
    finally:
        return strRes

#log = open("logger.txt", "w")
while True:
    
    print('\n.::Menú principal::.')
    print('1. Sumar')
    print('2. Restar')
    print('3. Ver Log')
    print('4. Salir')
    try:
        op = int(input('\tSeleccione una opción: '))

        if op == 1:
            print("\t\nSuma de dos números: ")
            sum = operacion(True)
            if sum != False:
                print(sum)
                logging.info(sum)
            
            
        elif op == 2:
            print("\t\nResta de dos números: ")
            rest = operacion(False)
            if rest != False:
                print(rest)
                logging.info(rest)

        elif op == 3:    
            print("\t\nRegistro de operaciones: ")
            log = open("logger.txt", "r")   
            print(log.read())
            log.close()

        elif op == 4:
            print("Gracias!")
            logging.info("Salió del script.")
            break
    except:
        logging.warning('Seleccionó una opción de menú inválida.')