# 1. Remover duplicatas da tupla (1, 2, 2, 3, 4, 4, 5)
tupla1 = (1, 2, 2, 3, 4, 4, 5)
tupla1_sem_duplicatas = tuple(set(tupla1))
print(f"Tupla sem duplicatas: {tupla1_sem_duplicatas}")  # (1, 2, 3, 4, 5)

# 2. Criar uma nova tupla sem duplicatas a partir das tuplas (1, 2, 3) e (3, 4, 5)
tupla2a = (1, 2, 3)
tupla2b = (3, 4, 5)
tupla_combinada = tuple(set(tupla2a + tupla2b))
print(f"Tupla combinada sem duplicatas: {tupla_combinada}")  # (1, 2, 3, 4, 5)

# 3. Função que retorna o menor e o maior valor de uma tupla (23, 1, 56, 3, 78, 2)
def min_max(tupla):
    return (min(tupla), max(tupla))

tupla3 = (23, 1, 56, 3, 78, 2)
resultado_min_max = min_max(tupla3)
print(f"Menor e maior valor: {resultado_min_max}")  # (1, 78)

# 4. Ordenar a tupla (("Alice", 25), ("Bob", 22), ("Charlie", 23)) por idade
def indicetupla(tupla):
    return tupla[1]

tupla4 = (("Alice", 25), ("Bob", 22), ("Charlie", 23))
tupla4_ordenada = tuple(sorted(tupla4, key=indicetupla))
print(f"Tupla ordenada por idade: {tupla4_ordenada}")  # (("Bob", 22), ("Charlie", 23), ("Alice", 25))

# 5. Contar quantos elementos de cada tipo estão presentes na tupla (1, "a", 2.5, "b", 3)
tupla5 = (1, "a", 2.5, "b", 3)
contagem = {"int": 0, "str": 0, "float": 0}
for elemento in tupla5:
    if isinstance(elemento, int):
        contagem["int"] += 1
    elif isinstance(elemento, str):
        contagem["str"] += 1
    elif isinstance(elemento, float):
        contagem["float"] += 1
print(f"Contagem de tipos: {contagem}")  # {'int': 2, 'str': 2, 'float': 1}

# 6. Encontrar os elementos em ambas as tuplas (1, 2, 3, 4) e (3, 4, 5, 6)
tupla6a = (1, 2, 3, 4)
tupla6b = (3, 4, 5, 6)
interseccao = tuple(set(tupla6a) & set(tupla6b))
print(f"Elementos em ambas as tuplas: {interseccao}")  # (3, 4)

# 7. Converter a lista de tuplas [("a", 1), ("b", 2), ("c", 3)] para o dicionário {"a": 1, "b": 2, "c": 3}
lista_tuplas7 = [("a", 1), ("b", 2), ("c", 3)]
dicionario7 = dict(lista_tuplas7)
print(f"Dicionário convertido: {dicionario7}")  # {'a': 1, 'b': 2, 'c': 3}

# 8. Retornar uma nova tupla apenas com os números pares da tupla (1, 2, 3, 4, 5, 6)
tupla8 = (1, 2, 3, 4, 5, 6)
tupla_pares = tuple(x for x in tupla8 if x % 2 == 0)
print(f"Tupla com números pares: {tupla_pares}")  # (2, 4, 6)

# 9. Acessar o segundo elemento da terceira tupla em ((1, 2), (3, 4), (5, 6))
tupla9 = ((1, 2), (3, 4), (5, 6))
segundo_elemento_terceira_tupla = tupla9[2][1]
print(f"Segundo elemento da terceira tupla: {segundo_elemento_terceira_tupla}")  # 6

# 10. Criar uma tupla contendo funções para soma, subtração, multiplicação e divisão e aplicar a (10, 5)
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

funcoes = (soma, subtracao, multiplicacao, divisao)
a, b = 10, 5
resultados = tuple(func(a, b) for func in funcoes)
print(f"Resultados das operações: {resultados}")  # (15, 5, 50, 2.0)