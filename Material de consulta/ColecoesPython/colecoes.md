# Coleções em Python

Neste conteúdo vamos aprender sobre três coleções fundamentais em Python: **listas**, **tuplas** e **dicionários**. Cada uma dessas coleções tem suas próprias características e é utilizada em diferentes situações, dependendo da necessidade do programa.

## Listas

Conforme já vimos, as listas são coleções **mutáveis** que podem armazenar diferentes tipos de dados. Isso significa que, após a criação, você pode modificar o conteúdo de uma lista, adicionando ou removendo elementos.

```python
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(programadores[4])  # Saída: Luana
```

No exemplo acima, criamos uma lista chamada `programadores`. O item no índice 4 é "Luana".

### Características das Listas

As listas são altamente flexíveis. Elas podem armazenar diferentes tipos de dados, inclusive misturados. Por exemplo, podemos ter números, strings e até outras listas dentro de uma mesma lista:

```python
mix = [23, 'Python', [3, 4, 5], 9.8]
print(mix)  # Saída: [23, 'Python', [3, 4, 5], 9.8]
```

As listas são **mutáveis**, ou seja, podemos adicionar, remover ou alterar os itens. Veja como podemos alterar um item na lista:

```python
programadores[1] = 'Carolina'
print(programadores)  # ['Victor', 'Carolina', 'Samuel', 'Caio', 'Luana']
```

Também podemos adicionar novos itens com o método `append()`:

```python
programadores.append('Renato')
print(programadores)  # ['Victor', 'Carolina', 'Samuel', 'Caio', 'Luana', 'Renato']
```

Se quisermos adicionar um item em uma posição específica, usamos o método `insert()`:

```python
programadores.insert(1, 'Rafael')
print(programadores)  # ['Victor', 'Rafael', 'Carolina', 'Samuel', 'Caio', 'Luana']
```

### Removendo Itens

Podemos remover itens de uma lista usando o método `remove()` (remover por valor) ou `pop()` (remover por índice):

```python
programadores.remove('Victor')
print(programadores)  # ['Rafael', 'Carolina', 'Samuel', 'Caio', 'Luana']
```

```python
programadores.pop(0)
print(programadores)  # ['Carolina', 'Samuel', 'Caio', 'Luana']
```

## Tuplas

As **tuplas** são semelhantes às listas, mas têm uma característica importante que as diferencia: **tuplas são imutáveis**. Isso significa que, uma vez criada, uma tupla não pode ser modificada — você não pode alterar seus elementos, nem adicionar ou remover itens.

### Quando Usar Tuplas?

As tuplas são usadas quando você precisa garantir que os dados permaneçam inalterados durante a execução do programa. Um exemplo clássico seria armazenar coordenadas geográficas ou configurações de sistema que não devem ser alteradas.

### Criando Tuplas

Veja um exemplo simples de tupla:

```python
times_rj = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')
print(times_rj[2])  # Saída: Fluminense
```

Diferente das listas, se tentarmos modificar uma tupla, receberemos um erro:

```python
times_rj[1] = 'Bangu'  # Isso causará um erro
```

### Métodos das Tuplas

Apesar de serem imutáveis, as tuplas ainda permitem a leitura de seus elementos e podem ser usadas em operações comuns, como contagem de itens ou busca de valores. Exemplos:

```python
frutas = ('maçã', 'banana', 'laranja', 'maçã')
print(frutas.count('maçã'))  # Saída: 2
print(frutas.index('laranja'))  # Saída: 2
```

Tuplas podem conter diferentes tipos de dados e até outras coleções dentro de si:

```python
dados = (23, 'João', [5, 7, 9], {'chave': 'valor'})
print(dados)  # Saída: (23, 'João', [5, 7, 9], {'chave': 'valor'})
```

## Dicionários

Os **dicionários** em Python são coleções de dados organizadas em pares *chave/valor*. Eles são usados quando você precisa associar uma chave única a um valor específico. É uma estrutura extremamente útil para representar dados mais complexos, como informações de um cliente ou de um produto.

### Estrutura de um Dicionário

Vamos criar um exemplo simples de dicionário:

```python
dados_cliente = {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
}
print(dados_cliente['Nome'])  # Saída: Renan
```

Neste exemplo, cada chave ('Nome', 'Endereco', 'Telefone') está associada a um valor específico.

### Adicionando e Removendo Itens

Você pode adicionar novos pares *chave/valor* a qualquer momento:

```python
dados_cliente['Idade'] = 40
print(dados_cliente)  # {'Nome': 'Renan', 'Endereco': 'Rua Cruzeiro do Sul', 'Telefone': '982503645', 'Idade': 40}
```

Se precisar remover um par, pode usar o método `pop()` (para remover um item específico por chave) ou `del`:

```python
dados_cliente.pop('Telefone')
print(dados_cliente)  # {'Nome': 'Renan', 'Endereco': 'Rua Cruzeiro do Sul', 'Idade': 40}
```

```python
del dados_cliente['Endereco']
print(dados_cliente)  # {'Nome': 'Renan', 'Idade': 40}
```

### Dicionários com Múltiplas Características

Os dicionários podem ser usados para armazenar dados mais complexos. Por exemplo, imagine que queremos armazenar informações de múltiplos clientes, cada um com várias características:

```python
clientes = {
    'cliente1': {
        'Nome': 'Ana',
        'Idade': 30,
        'Endereco': 'Av. Brasil'
    },
    'cliente2': {
        'Nome': 'Pedro',
        'Idade': 45,
        'Endereco': 'Rua do Comércio'
    }
}
print(clientes['cliente1']['Nome'])  # Saída: Ana
```

Aqui, temos um dicionário chamado `clientes`, onde cada cliente é representado como um outro dicionário com suas respectivas características.

### Atualizando Valores em Dicionários

Para atualizar valores em um dicionário, basta referenciar a chave que você deseja modificar:

```python
clientes['cliente1']['Idade'] = 31
print(clientes['cliente1']['Idade'])  # Saída: 31
```

### Verificando a Existência de uma Chave

Antes de acessar uma chave, você pode verificar se ela existe para evitar erros:

```python
if 'Telefone' in dados_cliente:
    print(dados_cliente['Telefone'])
else:
    print("Telefone não encontrado")
```

## Funções Úteis para Coleções

Existem várias funções úteis que podem ser aplicadas a coleções, incluindo listas, tuplas e dicionários:

- **min() e max()**: Retornam o menor e maior valor de uma coleção.

```python
numeros = [15, 5, 0, 20, 10]
print(min(numeros))  # Saída: 0
print(max(numeros))  # Saída: 20
```

- **sum()**: Retorna a soma dos itens de uma coleção numérica.

```python
numeros = [1, 3, 6]
print(sum(numeros))  # Saída: 10
```

- **len()**: Retorna o tamanho de uma coleção.

```python
paises = ['Argentina', 'Brasil', 'Colômbia', 'Uruguai']
print(len(paises))  # Saída: 4
```

- **type()**: Informa o tipo de uma coleção.

```python
print(type(paises))  # Saída: <class 'list'>
```
