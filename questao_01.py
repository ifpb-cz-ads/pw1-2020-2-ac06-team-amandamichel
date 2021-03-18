'''

Escreva uma função que retorne o maior de dois números. Valores esperados:

máximo(5,6) == 6
máximo(2,1) == 2
máximo(7,7) == 7

'''


def maior(a, b):
    if a > b:
        return a
    else:
        return b

n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))

print("O valor maior é: ", maior(n1,n2))
