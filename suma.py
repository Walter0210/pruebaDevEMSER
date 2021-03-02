
a = input('Ingrese un numero: ')
try:
    if not isinstance(a, int):
        raise Exception()
except:
    print('Ingrese solo valores numéricos')