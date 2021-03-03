
def operacion(flag):
    strRes = False
    try:
        a = float(input('\nIngrese un numero: '))
        b = float(input('Ingrese otro numero: '))
        if flag:
            res = a + b
            strRes = ('\n\t' + str(a) + ' + ' + str(b) + ' = ' + str(res) + '\n')
            
        else:
            res = a - b
            strRes = ('\n\t' + str(a) + ' - ' + str(b) + ' = ' + str(res) + '\n')
    except:
        print('\n\tIngrese solo valores numéricos!\n\n')
    finally:
        return strRes

log = ''
while True:

    print('1. Sumar')
    print('2. Restar')
    print('3. Ver Log')
    print('4. Salir')
    op = int(input('\tSeleccione una opción: '))

    if op == 1:
        sum = operacion(True)
        print(sum)
        log += sum
        
        
    elif op == 2:
        res = operacion(False)
        print(res)
        log += res

    elif op == 3:       
        print(log)
             

try:
    a = int(input('Ingrese un numero: '))
    b = int(input('Ingrese otro numero: '))

    res = a + b
    print(res)
except:
    print('Ingrese solo valores numéricos')