from random import randint
num = randint(0, 10)
print('Vou pensar em um número entre 0 e 10. Adivinhe!!! ')
acertou = False
soma = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    soma += 1
    if jogador == num:
        acertou = True
    else:
        if jogador < num:
            print('Mais... Tente mais uma vez!')
        elif jogador > num:
            print('Menos... Tente mais uma vez!')
print('Acertou com {} palpites!'.format(soma))
