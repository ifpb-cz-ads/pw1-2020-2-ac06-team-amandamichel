'''6) Reescreva o programa da abaixo de forma a utilizar for em vez de while.

def soma(L):
	total=0
	x= 0
	while x<5:
    	total+=L[x]
    	x+=1
	return total'''

def soma(L):
  total = 0

  for element in L:
    total += element

  return total

print(soma([1,2,3,4,5])) 
