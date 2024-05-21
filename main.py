#Usuario informa um número
while True:
    try:
        contador = int(input('Informe um número inteiro: '))
        contador >= 0
        contador -=1
        print(contador)
        break
    except ValueError:
        print('Por favor informe um valor válido!')


# Usuario informa um número
'''contador = int(input('Informe um número inteiro: '))
while contador >=0:
    print(contador)
    contador -= 1
'''
