#Usuario informa um número
import os
import time

contador = int(input('Informe um número inteiro: '))

while contador >=0:
    try:   
        print(f'Contagem regressiva: {contador}...')
        time.sleep(1)
        os.system('cls')
        contador -= 1
        
    except ValueError:
        print('Por favor informe um valor válido!')

# Usuario informa um número
'''contador = int(input('Informe um número inteiro: '))
os.system('cls')
while contador >=0:
    print(f'Contagem regressiva: {contador}...')
    time.sleep(1)
    os.system('cls')
    contador -= 1

print('Booooom!!!')'''