'''

Reescreva a função abaixo de forma a utilizar os métodos de pesquisa em lista, vistos na aula passada.
A função ‘enumerate’ recebe uma lista como parâmetro e retorna uma lista de tuplas, estas formada por pares
(índice, valor). O valor ‘None’ é o valor nulo da linguagem Python, similar ao ‘null’ de Java e JavaScript.

def pesquise(lista, valor):
	for x,e in enumerate(lista):
    		if e == valor:
        			return x
	return None

'''

def pesquise(list, valor):
    if valor in list:
        return list.index(valor)
    return None

list = [1,2,3,4,5,6,7]

posicao = pesquise(list,5)

if posicao != None:
    print("Eta na posicao %d" %posicao)
else:
    print("Número não encontrado!")