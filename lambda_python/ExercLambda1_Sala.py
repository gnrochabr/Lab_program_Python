#1. Crie uma função lambda que some dois números e teste com os valores 5 e 3.
soma = lambda x,y:x+y
print("Exercicio 1:",soma(5,3))

#2. Crie uma função lambda que multiplique dois números e teste com os valores 4 e 5.
mult = lambda x,y: x*y
print("Exercicio 2:",mult(4,5))

#3. Crie uma função lambda que retorne o comprimento de uma string e teste com a string "Olá, mundo!".
tam = lambda x: len(x)
print("Exercicio 3:",tam('Olá, mundo!'))

#4. Crie uma função lambda que retorne o quadrado de um número e teste com o valor 5.
quad = lambda x: x**2
print("Exercicio 4:",quad(5))

#5. Use a função filter() com uma função lambda para filtrar os números pares de uma lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x%2==2,lista))
print("Exercicio 5:",pares)

#6. Crie uma função lambda que eleve um número ao cubo e teste com o valor 3.
cubo = lambda x: x**3
print("Exercicio 6:",cubo(3))

#7. Use a função sorted() com uma função lambda para ordenar uma lista de tuplas [(1, 3), (4, 1), (5, 2), (2, 4)] pelo segundo valor.
t_list = [(1, 3), (4, 1), (5, 2), (2, 4)]
t_order = sorted(t_list,key=lambda x:x[1])
print("Exercicio 7",t_order)

#8. Crie uma função lambda que converta uma temperatura de Celsius para Fahrenheit e teste com o valor 0.
ctoF = lambda x: (x*9/5) + 32
print("Exercicio 8",ctoF(0))

#9. Use a função map() com uma função lambda para mapear uma lista de nomes ["Ana", "João", "Carlos", "Beatriz"] para seus comprimentos.
nomes = ["Ana", "João", "Carlos", "Beatriz"]
maptoC = list(map(lambda x:len(x),nomes))
print("Exercicio 9:",maptoC)


#10. Use a função reduce() com uma função lambda para calcular a soma acumulada de uma lista de números [1, 2, 3, 4, 5].
from functools import reduce
numeros = [1, 2, 3, 4, 5]
red_num = reduce(lambda x,y:x+y,numeros)
print("Exercicio 10:", red_num)
