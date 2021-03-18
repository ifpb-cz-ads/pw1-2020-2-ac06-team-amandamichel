'''

Altere o programa abaixo de forma que o usuário tenha três chances de acertar o número. O programa
termina se o usuário acertar ou errar três vezes. A função ‘random.randint(x, y)’ recebe como parâmetros
dois inteiros, x e y, e retorna um outro inteiro escolhido aleatoriamente entre x e y.

import random
n=random.randint(1,10)
x=int(input("Escolha um número entre 1 e 10:"))
if (x==n):
	print("Você acertou!")
else:
	print("Você errou.")

'''

import random
n=random.randint(1,10)

tentativas = 1

while tentativas <= 3:
	x = int(input("Escolha um número entre 1 e 10:"))
	if (x==n):
		print("Você acertou!")
		break
	else:
		tentativas = tentativas + 1
		print("Você errou.")