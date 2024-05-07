# Crie uma função que receba um número de horas como parâmetro e retorne o equivalente em minutos e segundos.
def conv_hora(x):
    minutos = 0
    segundos = x*3600
    while (segundos >= 60):
        segundos = segundos - 60
        minutos += 1
    return f"{minutos} minutos, {segundos} segundos"

# Implemente uma função que calcule o montante final com base no capital inicial, taxa de juros e período, considerando tanto juros simples quanto compostos.


def juros(capital, taxajuros, periodo):
    juroSimples = capital*(taxajuros/100)*periodo
    juroSimples = juroSimples + capital
    juroComposto = capital*(1 + taxajuros/100)**periodo
    return f"Valor final com juros simples: R${juroSimples:.2f}\nValor final com juros compostos: R${juroComposto:.2f}"

# Escreva uma função que converta uma determinada quantia em uma moeda para outra moeda, com base em uma taxa de câmbio fornecida.
def cambio(valor, taxaCambio):
    return f"{valor/taxaCambio:.2f}"

# Crie uma função que gere uma lista de números primos dentro de um intervalo especificado.


def primos(x, y):
    divisores = 0
    primolist = []
    for i in range(x-1, y):
        for j in range(1, y):
            if i % j == 0:
                divisores += 1
        if (divisores <= 2):
            primolist.append(i)
            divisores = 0
        else:
            divisores = 0
    return primolist

# Implemente uma função que gere os primeiros n números da sequência de Fibonacci
def fibonacci(x):
    lista_fibo = []
    inicio = 0
    fibo = 1
    for i in range(x+1):
        lista_fibo.append(fibo)
        temp = fibo
        fibo += inicio
        inicio = temp
    
    return lista_fibo
