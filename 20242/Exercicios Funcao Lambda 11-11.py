#1 Crie uma função lambda que some dois números e teste com os valores 5 e 3.
soma = lambda x,y: x+y
print(5,4)

#2 Crie uma função lambda que multiplique dois números e teste com os valores 4 e 5.
mult = lambda x,y: x*y
print(mult(4,5))

#3 Crie uma função lambda que retorne o comprimento de uma string e teste com a string "Olá, mundo!".
tam = lambda x: len(x)
print(tam('olá mundo!'))

#4 Crie uma função lambda que retorne o quadrado de um número e teste com o valor 5.
quadrado = lambda x:x**2
print(quadrado(5)) 

#5 Use a função filter() com uma função lambda para filtrar os números pares de uma lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
listinha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtrado = list(filter(lambda x: x%2 == 0,listinha))
print(filtrado)

#6 Crie uma função lambda que eleve um número ao cubo e teste com o valor 3.
cubo = lambda x:x**3
print(quadrado(3)) 

#7 Use a função sorted() com uma função lambda para ordenar uma lista de tuplas [(1, 3), (4, 1), (5, 2), (2, 4)] pelo segundo valor.
listazinha = [(1, 3), (4, 1), (5, 2), (2, 4)]
ordenado = sorted(listazinha, key = lambda x: x[1])
print(ordenado)

#8 Crie uma função lambda que converta uma temperatura de Celsius para Fahrenheit e teste com o valor 0.
fahrenheit = lambda x:(x*(9/5))+32
print(fahrenheit(0))

#9 Use a função map() com uma função lambda para mapear uma lista de nomes ["Ana", "João", "Carlos", "Beatriz"] para seus comprimentos.
nombres = ["Ana", "João", "Carlos", "Beatriz"]
mapeado = list(map(lambda x: len(x),nombres))
print(mapeado)

#10 Use a função reduce() com uma função lambda para calcular a soma acumulada de uma lista de números [1, 2, 3, 4, 5].
from functools import reduce
listazita = [1, 2, 3, 4, 5]
reduzida = reduce(lambda x,y:x+y,listazita)
print(reduzida)
