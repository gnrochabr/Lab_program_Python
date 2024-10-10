Aqui está a aula em formato Markdown:

```markdown
# Aula: Coleções em Python

Nesta aula, vamos aprender sobre três coleções fundamentais em Python: **listas**, **tuplas** e **dicionários**.

## Listas

As listas são coleções mutáveis que podem armazenar diferentes tipos de dados. Veja um exemplo de lista:

```python
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(programadores[4])  # Saída: Luana
```

No exemplo acima, criamos uma lista chamada `programadores`. O item no índice 4 é "Luana".

### Características das Listas

As listas são **mutáveis**, ou seja, podemos adicionar, remover ou alterar os itens da lista. Veja como podemos alterar um item na lista:

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

As **tuplas** são semelhantes às listas, mas com uma diferença importante: elas são **imutáveis**. Isso significa que, depois de criadas, seus itens não podem ser alterados. Vejamos um exemplo:

```python
times_rj = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')
print(times_rj[2])  # Saída: Fluminense
```

Diferente das listas, se tentarmos modificar uma tupla, receberemos um erro.

## Dicionários

Os **dicionários** armazenam pares *chave/valor*, como uma lista de contatos, onde cada nome está associado a um número de telefone. Vejamos um exemplo:

```python
dados_cliente = {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
}
print(dados_cliente['Nome'])  # Saída: Renan
```

### Adicionando e Removendo Itens

Para adicionar um item a um dicionário, basta associar uma nova chave a um valor:

```python
dados_cliente['Idade'] = 40
print(dados_cliente)  # {'Nome': 'Renan', 'Endereco': 'Rua Cruzeiro do Sul', 'Telefone': '982503645', 'Idade': 40}
```

Para remover, podemos usar `pop()` ou `del`:

```python
dados_cliente.pop('Telefone', None)
del dados_cliente['Endereco']
print(dados_cliente)  # {'Nome': 'Renan', 'Idade': 40}
```

## Funções Úteis para Coleções

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
print(type(paises))  # Saída: list
```

Agora que você aprendeu o básico sobre listas, tuplas e dicionários em Python, pode começar a utilizá-los para organizar dados nos seus programas!
```

Esse conteúdo está estruturado em Markdown, facilitando a leitura em plataformas de edição de texto e documentação.
