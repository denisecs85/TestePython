nome = input('Qual é o seu nome?')
print('É um grande prazer te conhecer', nome)
print('Estou aprendendo Python e estou muito feliz.')
print('Quero deixar registrado o meu desenvolvimento.')
print('Para iniciar vamos fazer uma brincadeira super simples...')
print('Vamos começar!')
from random import randint
from time import sleep
computador=randint(0,5)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...!')
jogador=int(input('Em que número eu pensei?'))
print('Processando...')
sleep(3)
if jogador==computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))
