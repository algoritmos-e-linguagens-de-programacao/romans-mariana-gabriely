# Exercício: Conversão de Números Inteiros e Números Romanos

## Objetivo

Desenvolver duas funções em Python para converter números inteiros em números romanos e vice-versa.

- [Numeração romana (Wikipedia)](https://pt.wikipedia.org/wiki/Numera%C3%A7%C3%A3o_romana)
- [Números Romanos (com tabelas e conversor)](https://www.todamateria.com.br/numeros-romanos/)

## Descrição

Vocês vão encontrar um arquivo chamado `romans.py` que contém duas funções já declaradas, para vocês preencherem. Preencham de acordo:

1. **Função para converter inteiros em números romanos**

    Implemente a função `int_to_roman(num)` que recebe um número inteiro num e retorna uma string representando o número em algarismos romanos.

    ```python
    def int_to_roman(num):
        # Implemente sua função aqui

    ```

2. **Função para converter números romanos em inteiros**

    Implemente a função `roman_to_int(s)` que recebe uma string s representando um número em algarismos romanos e retorna o número inteiro correspondente.

    ```python
    def roman_to_int(s):
        # Implemente sua função aqui
    ```

### Regras dos Algarismos Romanos

- Algarismos: `I (1), V (5), X (10), L (50), C (100), D (500), M (1000)`
- Combinações e subtrações:
  - `IV (4), IX (9)`
  - `XL (40), XC (90)`
  - `CD (400), CM (900)`

### Exemplos de Uso

`int_to_roman(1994)` deve retornar `MCMXCIV`
`roman_to_int("MCMXCIV")` deve retornar `1994`
