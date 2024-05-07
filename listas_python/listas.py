lista = [10, 20, 5, 2, -6, 8, 16, 2, -1, 5]

# atividade 1 - Calcule a soma de todos os números em uma lista
print('Exercício 1 - Resolução 1:')
print(f"Soma da lista: {sum(lista)}")

print('Exercício 1 - Resolução 2:')
soma = 0
for i in lista:
    soma+=i
print(f"Soma da lista: {soma}")

# atividade 2 - Encontre o maior número em uma lista.
print('\nExercício 2 - Resolução 1:')
lista.sort(reverse=True)
print(f"Maior valor: {lista[0]}")

print('Exercício 2 - Resolução 2:')
maior = lista[0]
for i in range(1,len(lista)):
    if maior < lista[i]:
        maior = lista[i]
print(f"Maior valor: {maior}")

# atividade 3 - Encontre o menor número em uma lista.
print('\nExercício 3 - Resolução 1:')
lista.sort()
print(f"Maior valor: {lista[0]}")

print('Exercício 3 - Resolução 2:')
menor = lista[0]
for i in range(1,len(lista)):
    if menor > lista[i]:
        menor = lista[i]
print(f"Menor valor: {menor}")

# atividade 4 - Conte quantos números pares existem em uma lista de inteiros.
print('\nExercício 4 - Resolução 1:')
par = 0
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        par += 1
print(f"Pares: {par}")

print('Exercício 4 - Resolução 2:')
par = 0
for i in lista:
    if i % 2 == 0:
        par += 1
print(f"Pares: {par}")

# atividade 5 - Calcule a média dos números em uma lista.
print('\nExercício 5 - Resolução 1:')
print(f"Média: {round(sum(lista)/len(lista),2)}")

print('Exercício 5 - Resolução 2:')
soma = 0
cont = 0
for i in lista:
    soma+=i
    cont+=1
print(f"Média: {soma/cont}")



# atividade 6 - Verifique se todos os números em uma lista são positivos.
print('\nExercício 6 - Resolução 1:')
#Usando o índice
for i in range(0, len(lista)):
    if lista[i] < 0:
        print("Usando Índice: Lista possui números negativos!")
        break
    if i+1 >= len(lista):
        print("Usando o índice:Lista toda de números positivos")

print('Exercício  6- Resolução 2:')
#Usando o elemento
for i in lista:
    if i < 0:
        print("Usando o valor: Lista possui números negativos!")
        break
    if lista.index(i) >= len(lista)-1:
        print("Usando o o valor:Lista toda de números positivos") 

# atividade 7 - Verifique se pelo menos um número em uma lista é negativo.
print('\nExercício 7 - Resolução 1:')
for i in range(0, len(lista)):
    if lista[i] < 0:
        print(f"Usando o índice: Lista possui no mínimo o Negativo:{lista[i]}")
        break
    if i+1 >= len(lista):
        print("Usando o índice:Lista toda de números positivos")

print('Exercício 7 - Resolução 2:')
for i in lista:
    if i < 0:
        print(f"Usando o valor: Lista possui no mínimo o Negativo:{i}")
        break
    if lista.index(i) >= len(lista)-1:
        print("Usando o o valor:Lista toda de números positivos") 

# atividade 8 - Remova todos os números repetidos de uma lista.
lista = [10, 20, 5, 2, -6, 8, 16, 2, -1, 5]
print('\nExercício 8 - Resolução 1:')
for i in lista:
    if lista.count(i) > 1:
        print(f"Valor removido: {i}")
        lista.remove(i)
print(lista)


print('Exercício 8 - Resolução 2:')
lista = [10, 20, 5, 2, -6, 8, 16, 2, -1, 5]
for i in range(0,len(lista)):
    for j in range(len(lista)-1,i,-1): #itera de forma descrescente com a função range: range(maiorIndice,menorIndice,descrescente(-1))
        if lista[i] == lista[j]:
            print(f"Valor removido: {lista[i]}")
            lista.remove(lista[i])
print(lista)

# atividade 9 - Ordene os números em ordem crescente em uma lista.
print('\nExercício 9 - Resolução 1')
lista.sort()
print(lista)
print('Exercício 9 - Resolução 2')
for i in range(1,len(lista)):
    if lista[i] < lista[i-1]:
        temp = lista[i-1]
        lista[i-1] = lista[i]
        lista[i] = temp
print(lista)


# atividade 10 - Verifique se uma lista é uma sequência estritamente crescente (ou seja, cada elemento é maior que o anterior).

print('\nExercício 10: - Resolução 1')
texto = 'ordenada'
for i in range(0, len(lista)):
    for j in range(i+1, len(lista)-1):
        if lista[i] > lista[j]:
            texto = 'não ordenada'
            break
print(f"Lista {texto}")

print('Exercício 10: - Resolução 2')
ordenar = 0
for i in range(1, len(lista)):
    if lista[i] <= lista[i - 1]:
        ordenar+=1
if ordenar == 0:
    print("Lista ordenada")
else:
    print("Lista não ordenada")
