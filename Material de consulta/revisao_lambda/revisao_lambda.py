#1. Dado uma lista de números inteiros, crie uma função lambda que retorne uma nova lista com os números ao quadrado.

numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)
# Output: [1, 4, 9, 16, 25]


#2. Você possui uma lista de preços de produtos em diferentes lojas. Crie uma função lambda que encontre o menor preço de cada produto.

precos = [[100, 200, 150], [80, 90, 120], [75, 85, 95]]
menor_preco = list(map(lambda x: min(x), precos))
print(menor_preco)
# Output: [100, 80, 75]


#3. Imagine que você está desenvolvendo um sistema de gerenciamento de estudantes e tem uma lista de tuplas contendo o nome e a nota de cada aluno. Crie uma função lambda que filtre os alunos que tiraram nota maior ou igual a 7.

alunos = [("Ana", 8), ("Bruno", 6), ("Carlos", 9), ("Diana", 5)]
aprovados = list(filter(lambda x: x[1] >= 7, alunos))
print(aprovados)
# Output: [('Ana', 8), ('Carlos', 9)]


#4. Suponha que você tem uma lista de palavras. Crie uma função lambda que conte quantas palavras têm mais de 5 letras.

palavras = ["casa", "elefante", "arvore", "", "desenvolvimento"]
contagem = len(list(filter(lambda x: len(x) > 5, palavras)))
print(contagem)
# Output: 3


#5. Dada uma lista de tuplas representando coordenadas (x, y), crie uma função lambda que ordene as coordenadas pela distância da origem (0, 0).

coordenadas = [(1, 2), (3, 4), (0, 5), (2, 2)]
coordenadas_ordenadas = sorted(coordenadas, key=lambda x: x[0]**2 + x[1]**2)
print(coordenadas_ordenadas)
# Output: [(1, 2), (2, 2), (3, 4), (0, 5)]


#6. Considere uma lista de números inteiros. Crie uma função lambda que retorne uma nova lista contendo apenas os números pares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)
# Output: [2, 4, 6, 8, 10]


#7. Imagine que você está desenvolvendo um sistema de pontuação para um jogo. Crie uma função lambda que, dada uma lista de pontuações, retorne a média das pontuações.
from functools import reduce
pontuacoes = [10, 20, 30, 40, 50]
media = reduce(lambda x,y: x + y,pontuacoes)/len(pontuacoes)
print(media)
# Output: 30.0


#8. Você tem uma lista de nomes de funcionários e uma lista de seus respectivos salários. Crie uma função lambda que filtre os funcionários que ganham mais de R$ 3.000,00.

funcionarios = [("Ana", 2500), ("Bruno", 3200), ("Carlos", 4500), ("Diana", 2800)]
altos_salarios = list(filter(lambda x: x[1] > 3000, funcionarios))
print(altos_salarios)
# Output: [('Bruno', 3200), ('Carlos', 4500)]


#9. Dada uma lista de strings representando datas no formato "dd-mm-yyyy", crie uma função lambda que ordene as datas em ordem cronológica.

datas = ["12-05-2021", "01-01-2020", "23-11-2022", "15-08-2020"]
datas_ordenadas = sorted(datas, key=lambda x: (x.split("-")[2], x.split("-")[1], x.split("-")[0]))
print(datas_ordenadas)
# Output: ['01-01-2020', '15-08-2020', '12-05-2021', '23-11-2022']


#10. Suponha que você tem uma lista de dicionários representando produtos, onde cada dicionário tem as chaves 'nome' e 'preço'. Crie uma função lambda que retorne uma lista contendo apenas os nomes dos produtos mais caros que R$ 100,00.

produtos = [{"nome": "Produto A", "preço": 90}, {"nome": "Produto B", "preço": 150}, {"nome": "Produto C", "preço": 200}]
produtos_caros = list(map(lambda x: x["nome"], filter(lambda x: x["preço"] > 100, produtos)))
print(produtos_caros)
# Output: ['Produto B', 'Produto C']


#11. Você possui uma lista de idades de pessoas em um grupo. Crie uma função lambda que verifique se todos os membros do grupo são maiores de idade (18 anos ou mais).

idades = [20, 18, 21, 17, 19]
maiores_idade = all(map(lambda x: x >= 18, idades))
print(maiores_idade)
# Output: False


#12. Imagine que você está desenvolvendo um sistema de análise de vendas e tem uma lista de tuplas onde cada tupla contém o nome do produto e a quantidade vendida. Crie uma função lambda que retorne o produto mais vendido.

vendas = [("Produto A", 50), ("Produto B", 75), ("Produto C", 100), ("Produto D", 60)]
mais_vendido = max(vendas, key=lambda x: x[1])
print(mais_vendido)
# Output: ('Produto C', 100)


#13. Dada uma lista de números inteiros, crie uma função lambda que retorne a soma de todos os números ímpares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_impares = sum(filter(lambda x: x % 2 != 0, numeros))
print(soma_impares)
# Output: 25


#14. Suponha que você tem uma lista de tuplas contendo o nome de uma pessoa e a sua altura em centímetros. Crie uma função lambda que converta todas as alturas para metros.

alturas = [("Ana", 160), ("Bruno", 175), ("Carlos", 180)]
alturas_metros = list(map(lambda x: (x[0], x[1] / 100), alturas))
print(alturas_metros)
# Output: [('Ana', 1.6), ('Bruno', 1.75), ('Carlos', 1.8)]


#15. Imagine que você está desenvolvendo uma aplicação que precisa calcular a diferença entre duas listas de números inteiros. Crie uma função lambda que, dada duas listas, retorne uma lista com a diferença entre os elementos correspondentes.

lista1 = [10, 20, 30, 40]
lista2 = [5, 15, 25, 35]
diferenca = list(map(lambda x, y: x - y, lista1, lista2))
print(diferenca)
# Output: [5, 5, 5, 5]
