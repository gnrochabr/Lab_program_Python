# Exercício 1:
# Crie uma tupla com os seguintes elementos: 1, 2, 3, 4, 5. Imprima a tupla.
tupla = (1, 2, 3, 4, 5)
print(tupla)

# Exercício 2:
# Dada a tupla (10, 20, 30, 40, 50), acesse e imprima o terceiro elemento.
tupla = (10, 20, 30, 40, 50)
print(tupla[2])  # Saída: 30

# Exercício 3:
# Dada a tupla ("maçã", "banana", "cereja"), desempacote os elementos em variáveis separadas e imprima-as.
frutas = ("maçã", "banana", "cereja")
f1, f2, f3 = frutas
print(f1)  # Saída: maçã
print(f2)  # Saída: banana
print(f3)  # Saída: cereja

# Exercício 4:
# Dadas as tuplas (1, 2, 3) e (4, 5, 6), concatene-as em uma nova tupla e imprima o resultado.
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
nova_tupla = tupla1 + tupla2
print(nova_tupla)  # Saída: (1, 2, 3, 4, 5, 6)

# Exercício 5: Fatiamento de Tuplas
# Dada a tupla ("a", "b", "c", "d", "e"), imprima uma subtupla contendo apenas os três primeiros elementos.
tupla = ("a", "b", "c", "d", "e")
subtupla = tupla[:3]
print(subtupla)  # Saída: ('a', 'b', 'c')

# Exercício 6:
# Verifique se o número 5 está presente na tupla (1, 2, 3, 4, 5) e imprima o resultado.
tupla = (1, 2, 3, 4, 5)
print(5 in tupla)

# Exercício 7: Contagem de Elementos
# Dada a tupla (1, 2, 2, 3, 3, 3, 4, 4, 4, 4), conte quantas vezes o número 3 aparece.
tupla = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
contagem = tupla.count(3)
print(contagem)  # Saída: 3

# Exercício 8:
# Dada a tupla (10, 20, 30, 40, 50), encontre o índice do elemento 40.
tupla = (10, 20, 30, 40, 50)
indice = tupla.index(40)
print(indice)  # Saída: 3

# Exercício 9: Soma de Elementos
# Dada a tupla (1, 2, 3, 4, 5), calcule e imprima a soma dos elementos.
tupla = (1, 2, 3, 4, 5)
soma = sum(tupla)
print(soma)  # Saída: 15

# Exercício 10: Função que Retorna Tupla
# Escreva uma função que receba três números como argumentos e retorne uma tupla contendo esses três números.


def criar_tupla(a, b, c):
    return (a, b, c)


resultado = criar_tupla(1, 2, 3)
print(resultado)  # Saída: (1, 2, 3)
