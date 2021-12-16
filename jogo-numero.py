from random import randint
from time import sleep
numero = randint(0, 5)
print('-=-' * 23)
print('Vou pensar em um número de 0 a 5. Você acha que consegue adivinhar?')
print('-=-' * 23)
sleep(3)
print('Já pensei!')
numeroUsuario = int(input('Agora, digite um número de 0 a 5: '))
if numeroUsuario == numero:
    print('Você acertou! Como você sabia?')
else:
    print(f'Que pena, você errou... Eu tinha pensado no número {numero}.')
