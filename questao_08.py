'''8) Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada com os elementos da lista, também passada como parâmetro.
Retorne verdadeiro se a string for encontrada dentro da lista, e falso em caso contrário.'''

def contém(string, lista):
  return string in lista


print(contém('a',['a','b','c']))
print(contém('abc',['a','b','c']))
print(contém('12',['10','11','12']))