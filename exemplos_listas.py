### Outras operações com listas

a = [0, 1, 2]
b = [3, 4, 5]
c = ["seis", "sete", "oito"]
d = a + b + c # concatena as listas
e = a * 3 # (lista * x) repete os elementos da lista "x" vezes em uma só lista
print(d)
print(e)



### Fatiamento de listas

lista = [7, 'Blue' , 9.6 , [6, 7, 8], 'Python', (3 , 'j')]

print(lista[1:4]) # lista[x,y] retorna os elementos de x até "y -1"
print(lista[:3]) # lista[:x] retorna de 0 até x -1
print(lista[3:]) # lista[x:] retorna os elementos a partir de x
print()
print(lista[-2]) # lista[-x] retorna o elemento x contando a partir do final (começando em 1)
print(lista[-5:-2]) # lista[-x:-y] retorna os elementos entre os itens x e y contados a partir do final
print(lista[:-3]) # lista[:-x] retorna os elementos até "x -1" contados a partir do final
print(lista[-3:]) # lista[-x:] retorna os elementos a partir de x contados a partir do final
print(lista[3:-1]) # lista[x:-y] retorna os elementos a partir de x até "y -1 contando do final"
print(lista[0:-1])
print(lista[-1])


### Criando listas a partie de range()
### função list()

lista_range1 = list(range(8)) # list(coisas) cria uma lista a partir do que foi passado
lista_range2 = list(range(3, 8))
lista_range3 = list(range(1, 9, 2)) 
print(lista_range1)
print(lista_range2)
print(lista_range3)


### Tuplas

tupla1 = (1,2,3,4,5)
tupla2 = ("Tupla",["Lista","Elemento"])
lista1 = [1,2,3,4,5]

print(tupla1)
print(lista1)
print(tupla2)
print()

print(type(tupla2[1]))
tupla2[0] = "Blue"

lista_de_tupla = list(tupla1)
lista_de_tupla2 = [tupla1]

print(tupla2)
print(lista1)
print(tupla1)
print(lista_de_tupla)
print(lista_de_tupla2)

lista = ["10",10,20,30,40,50, ["Yago", ["Glauco", True]]]

for i in lista:
    print(i)

print("--==--"*5)
for i in range(len(lista)): # Crio uma sequência de número de 0 até o tamanho da lista -1
    print(i)

print("--==--"*5)
for i, v in enumerate(lista): # Retorna tanto o índice quanto o valor do elemento
    print(f'O índice {i} contém: {v}')

print("--==--"*5)
for i, v in enumerate(lista[3:],3): # Retorna a partir do item 3, e começa a contar o índice em 3
    print(f'O índice {i} contém: {v}')
    print(i)
    print(v)