'''

Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string, o número
mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo
e mínimo, e falso em caso contrário.

'''

def verificarString(palavra, min, max):
    if len(palavra) >= min and len(palavra) <= max:
        return True
    return False

min = int(input("Informe a quantidade minima de caracteres: "))
max = int(input("Informe a quantidade maximo de caracteres: "))
palavra = input("Informe uma palavra: ")

print(verificarString(palavra,min,max))