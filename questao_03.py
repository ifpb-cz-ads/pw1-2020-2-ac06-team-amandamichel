'''

Escreva uma função que receba o lado (l) de um quadrado e retorne sua área (A = lado^2).

Valores esperados:
área_quadrado(4) == 16
área_quadrado(9) == 81

'''

def area(l):
    return l*l

l = int(input("Informe o valor do lado: "))

print("A area eh: ", area(l))