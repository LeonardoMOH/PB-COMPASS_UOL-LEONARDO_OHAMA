# Sumário

### Sprint 2:

1. [Resumo](#resumo)

2. [Exercícios](#exercícios)

    I.    [Exercício 01](#Exercício01)

    II.   [Exercício 02](#Exercício02)

    III.  [Exercício 03](#Exercício03)

    IV.   [Exercício 04](#Exercício04)

    V.    [Exercício 05](#Exercício05)

    VI.   [Exercício 06](#Exercício06)

    VII.  [Exercício 07](#Exercício07)

    VIII. [Exercício 08](#Exercício08)

    IX.   [Exercício 09](#Exercício09)

    X.    [Exercício 10](#Exercício10)

    XI.   [Exercício 11](#Exercício11)

    XII.  [Exercício 12](#Exercício12)

    XIII. [Exercício 13](#Exercício13)

    XIV.  [Exercício 14](#Exercício14)

    XV.   [Exercício 15](#Exercício15)

    XVI.  [Exercício 16](#Exercício16)

    XVII. [Exercício 17](#Exercício17)

    XVIII.[Exercício 18](#Exercício18)

    XIX.  [Exercício 19](#Exercício19)

    XX.   [Exercício 20](#Exercício20)

    XXI.  [Exercício 21](#Exercício21)

    XXII. [Exercício 22](#Exercício22)

    XXIII.[Exercício 23](#Exercício23)

    XXIV. [Exercício 24](#Exercício24)

    XXV.  [Exercício 25](#Exercício25)

    XXVI. [Exercício Exportação 1](#Exercício_exp_1)

    XXVII.[Exercício Exportação 2](#Exercício_exp_2)

3. [Evidências](#evidências)

4. [Certificados](#certificados)

### README:

1. [README Principal](../README.md)

2. [README Desafio](<Desafio/README.md>)

# Resumo

📊‍ **Python:** No curso de SQL, eu aprendi vários comandos para manipulação de tabelas, como SELECT, JOIN, UNION etc. E os operadores AND, OR, BETWEEN etc. No final do curso foi proposto exercícios para praticar o primeiro foi dos exercícios 01 ao 07 com o estudo de caso da biblioteca, os exercícios do 08 ao 16 foi o estudo de caso da loja e o exercício II que consistia em exportar os dados da tabela em formato csv com diferente separadores.

🎯 **Desafio** O desafio consiste em normalizar os dados da tabela tb_locacao, que contém todos os dados das tabelas IDs do arquivo concessionaria com o Modelo Relacional e depois montar com base nesse modelo normalizado o Modelo Dimensional.

[**Voltar ao Sumário**](#sumário)

# Exercícios 🥋

## Caso de Estudo: Biblioteca 📖

<a id="Exercício01"></a>

### Exercício 01

Desenvolva um código em Python que crie variáveis para armazenar o nome e a idade de uma pessoa, juntamente com seus valores correspondentes. Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

[Solução SQL Exercício 01](Exercicios/SPRINT_03_E01.py)

[Resultado Exercício 01](#Exercício01_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício02"></a>

### Exercício 02

Escreva um código Python que use a função range() para adicionar três números em uma lista(Esta lista deve chamar-se 'números')  e verificar se esses três números são pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).



Importante: Aplique a função range() em seu código.



Exemplos de saída:

Par: 2
Ímpar: 3

[Solução SQL Exercício 02](Exercicios/SPRINT_03_E02.py)

[Resultado Exercício 02](#Exercício02_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício03"></a>

### Exercício 03

Escreva um código Python para imprimir os números pares de 0 até 20 (incluso).



Importante: Aplique a função range() em seu código.

[Solução SQL Exercício 03](Exercicios/SPRINT_03_E03.py)

[Resultado Exercício 03](#Exercício03_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício04"></a>

### Exercício 04

Escreva um código Python para imprimir todos os números primos entre 1 até 100. Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.



Importante: Aplique a função range().

[Solução SQL Exercício 04](Exercicios/SPRINT_03_E04.py)

[Resultado Exercício 04](#Exercício04_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício05"></a>

### Exercício 05

Escreva um código Python que declara 3 variáveis:



dia, inicializada com valor 22

mes, inicializada com valor 10 e

ano, inicializada com valor 2022

Como saída, você deverá imprimir a data correspondente, no formato a seguir dia/mes/ano.

[Solução SQL Exercício 05](Exercicios/SPRINT_03_E05.py)

[Resultado Exercício 05](#Exercício05_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício06"></a>

### Exercício 06

Considere as duas listas abaixo:



a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


Escreva um programa para avaliar o que ambas as listas têm em comum (sem repetições), imprimindo a lista de valores da interseção na saída padrão.



Importante:  Esperamos que você utilize o construtor set() em seu código.

[Solução SQL Exercício 06](Exercicios/SPRINT_03_E06.py)

[Resultado Exercício 06](#Exercício06_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício07"></a>

### Exercício 07

Dada a seguinte lista:



a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



Faça um programa que gere uma nova lista contendo apenas números ímpares.

[Solução SQL Exercício 07](Exercicios/SPRINT_03_E07.py)

[Resultado Exercício 07](#Exercício07_1)

[**Voltar ao Sumário**](#sumário)

## Caso de Estudo: Loja

<a id="Exercício08"></a>

### Exercício 08

Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.

Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.



É necessário que você imprima no console exatamente assim:



A palavra: maça não é um palíndromo
 
A palavra: arara é um palíndromo
 
A palavra: audio não é um palíndromo
 
A palavra: radio não é um palíndromo
 
A palavra: radar é um palíndromo
 
A palavra: moto não é um palíndromo

[Solução SQL Exercício 08](Exercicios/SPRINT_03_E08.py)

[Resultado Exercício 08](#Exercício08_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício09"></a>

### Exercício 09

Dada as listas a seguir:



primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]


Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".



Exemplo:

0 - João Soares está com 19 anos

[Solução SQL Exercício 09](Exercicios/SPRINT_03_E09.py)

[Resultado Exercício 09](#Exercício09_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício10"></a>

### Exercício 10

Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.



['abc', 'abc', 'abc', '123', 'abc', '123', '123']

[Solução SQL Exercício 10](Exercicios/SPRINT_03_E10.py)

[Resultado Exercício 10](#Exercício10_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício11"></a>

### Exercício 11

Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

Dica: leia a documentação do pacote json

[Solução SQL Exercício 11](Exercicios/SPRINT_03_E11.py)

[Resultado Exercício 11](#Exercício11_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício12"></a>

### Exercício 12

Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.



Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.

[Solução SQL Exercício 12](Exercicios/SPRINT_03_E12.py)

[Resultado Exercício 12](#Exercício12_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício13"></a>

### Exercício 13

Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

Dica: leia a documentação da função open(...)



[Solução SQL Exercício 13](Exercicios/SPRINT_03_E13.py)

[Resultado Exercício 13](#Exercício13_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício14"></a>

### Exercício 14

Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.



Teste sua função com os seguintes parâmetros:



(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

[Solução SQL Exercício 14](Exercicios/SPRINT_03_E14.py)

[Resultado Exercício 14](#Exercício14_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício15"></a>

### Exercício 15

Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:

liga(): muda o estado da lâmpada para ligada

desliga(): muda o estado da lâmpada para desligada

esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

Para testar sua classe:

Ligue a Lampada

Imprima: A lâmpada está ligada? True

Desligue a Lampada

Imprima: A lâmpada ainda está ligada? False

[Solução SQL Exercício 15](Exercicios/SPRINT_03_E15.py)

[Resultado Exercício 15](#Exercício15_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício16"></a>

### Exercício 16

Exercícios Parte 2
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.



A string deve ter valor  "1,3,4,6,10,76"

[Solução SQL Exercício 16](Exercicios/SPRINT_03_E16.py)

[Resultado Exercício 16](#Exercício16_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício17"></a>

### Exercício 17

Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo



lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

[Solução SQL Exercício 17](Exercicios/SPRINT_03_E17.py)

[Resultado Exercício 17](#Exercício17_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício18"></a>

### Exercício 18

Dado o dicionário a seguir:

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.

[Solução SQL Exercício 18](Exercicios/SPRINT_03_E18.py)

[Resultado Exercício 18](#Exercício18_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício19"></a>

### Exercício 19

Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:



Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!



import random 

amostra aleatoriamente 50 números do intervalo 0...500

random_list = random.sample(range(500),50)


Use as variáveis abaixo para representar cada operação matemática:



mediana
media
valor_minimo 
valor_maximo 


Importante: Esperamos que você utilize as funções abaixo em seu código:



random

max

min

sum

[Solução SQL Exercício 19](Exercicios/SPRINT_03_E19.py)

[Resultado Exercício 19](#Exercício19_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício20"></a>

### Exercício 20

Imprima a lista abaixo de trás para frente.

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

[Solução SQL Exercício 20](Exercicios/SPRINT_03_E20.py)

[Resultado Exercício 20](#Exercício20_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício21"></a>

### Exercício 21

Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.



Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.



Imprima no console exatamente assim:

Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu

[Solução SQL Exercício 21](Exercicios/SPRINT_03_E21.py)

[Resultado Exercício 21](#Exercício21_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício22"></a>

### Exercício 22

Crie uma classe chamada Pessoa, com um atributo privado chamado nome (declarado internamente na classe como __nome) e um atributo público de nome id.

Adicione dois métodos à classe, sendo um para definir o valor de __nome e outro para retornar o valor do respectivo atributo.

Lembre-se que o acesso ao atributo privado deve ocorrer somente através dos métodos definidos, nunca diretamente.  Você pode alcançar este comportamento através do recurso de properties do Python.



Veja um exemplo de como seu atributo privado pode ser lido e escrito:



pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)

[Solução SQL Exercício 22](Exercicios/SPRINT_03_E22.py)

[Resultado Exercício 22](#Exercício22_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício23"></a>

### Exercício 23

Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).



Utilize os valores abaixo para testar seu exercício:

x = 4 
y = 5
imprima:

Somando: 4+5 = 9
Subtraindo: 4-5 = -1

[Solução SQL Exercício 23](Exercicios/SPRINT_03_E23.py)

[Resultado Exercício 23](#Exercício23_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício24"></a>

### Exercício 24

Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente.

Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].

Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método ordenacaoDecrescente.



Imprima o resultado da ordenação crescente e da ordenação decresce

[1, 2, 3, 4, 5] 
[9, 8, 7, 6]

[Solução SQL Exercício 24](Exercicios/SPRINT_03_E24.py)

[Resultado Exercício 24](#Exercício24_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício25"></a>

### Exercício 25

Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.

Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.

Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.

Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:

“O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.

Sendo x, y, z e w cada um dos atributos da classe “Avião”.



Valores de entrada:

modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul

modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul

modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul

[Solução SQL Exercício 25](Exercicios/SPRINT_03_E25.py)

[Resultado Exercício 25](#Exercício25_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício_exp_1"></a>

### Exercício Exportação 1

Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. Utiizar o caractere ; (ponto e vírgula) como separador. Lembre-se que o conteúdo do seu arquivo deverá respoeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo: CodLivro, Titulo, CodAutor, NomeAutor, Valor, CodEditora, NomeEditora. Observação: O arquivo exportado, conforme as especificações acima, deve ser disponibilizado no GitHub.

[Solução SQL Exercício Exportação 1](Exercicios/SPRINT_02_E02_02.sql)

[Solução CSV Exercício Exportação 1](Exercicios/SPRINT_02_E02_02.csv)

[Resultado Exercício Exportação 1](#Exercício_exp_1_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício_exp_2"></a>

### Exercício Exportação 2

Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo CSV. Utilizar o caractere | (pipe) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo: CodEditora, NomeEditora, QuantidadeLivros. Observação: O arquivo exportado, conforme as especificações acima, deve ser disponibilizado no GitHub.

[Solução SQL Exercício Exportação 2](Exercicios/SPRINT_02_E03_02.sql)

[Solução CSV Exercício Exportação 2](Exercicios/SPRINT_02_E03_02.csv)

[Resultado Exercício Exportação 2](#Exercício_exp_2_1)

[**Voltar ao Sumário**](#sumário)

# Evidências

## Desafio

[Evidências Desafio](<Desafio/README.md#etapas>)

[**Voltar ao Sumário**](#sumário)

## Exercícios

<a id="Exercício01_1"></a>

### Exercício 01

![Resultado](<Evidencias/Exercicios/SPRINT_03_E01.png>)

[**Voltar ao Exercício 01**](#Exercício01)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício02_1"></a>

### Exercício 02

![Resultado](<Evidencias/Exercicios/SPRINT_03_E02.png>)

[**Voltar ao Exercício 02**](#Exercício02)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício03_1"></a>

### Exercício 03

![Resultado](<Evidencias/Exercicios/SPRINT_03_E03.png>)

[**Voltar ao Exercício 03**](#Exercício03)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício04_1"></a>

### Exercício 04

![Resultado](<Evidencias/Exercicios/SPRINT_03_E04.png>)

[**Voltar ao Exercício 04**](#Exercício04)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício05_1"></a>

### Exercício 05

![Resultado](<Evidencias/Exercicios/SPRINT_03_E05.png>)

[**Voltar ao Exercício 05**](#Exercício05)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício06_1"></a>

### Exercício 06

![Resultado](<Evidencias/Exercicios/SPRINT_03_E06.png>)

[**Voltar ao Exercício 06**](#Exercício06)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício07_1"></a>

### Exercício 07

![Resultado](<Evidencias/Exercicios/SPRINT_03_E07.png>)

[**Voltar ao Exercício 07**](#Exercício07)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício08_1"></a>

### Exercício 08

![Resultado](<Evidencias/Exercicios/SPRINT_03_E08.png>)

[**Voltar ao Exercício 08**](#Exercício08)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício09_1"></a>

### Exercício 09

![Resultado](<Evidencias/Exercicios/SPRINT_03_E09.png>)

[**Voltar ao Exercício 09**](#Exercício09)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício10_1"></a>

### Exercício 10

![Resultado](<Evidencias/Exercicios/SPRINT_03_E10.png>)

[**Voltar ao Exercício 10**](#Exercício10)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício11_1"></a>

### Exercício 11

![Resultado](<Evidencias/Exercicios/SPRINT_03_E11.png>)

[**Voltar ao Exercício 11**](#Exercício11)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício12_1"></a>

### Exercício 12

![Resultado](<Evidencias/Exercicios/SPRINT_03_E12.png>)

[**Voltar ao Exercício 12**](#Exercício12)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício13_1"></a>

### Exercício 13

![Resultado](<Evidencias/Exercicios/SPRINT_03_E13.png>)

[**Voltar ao Exercício 13**](#Exercício13)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício14_1"></a>

### Exercício 14

![Resultado](<Evidencias/Exercicios/SPRINT_03_E14.png>)

[**Voltar ao Exercício 14**](#Exercício14)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício15_1"></a>

### Exercício 15

![Resultado](<Evidencias/Exercicios/SPRINT_03_E15.png>)

[**Voltar ao Exercício 15**](#Exercício15)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício16_1"></a>

### Exercício 16

![Resultado](<Evidencias/Exercicios/SPRINT_03_E16.png>)

[**Voltar ao Exercício 16**](#Exercício16)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício17_1"></a>

### Exercício 17

![Resultado](<Evidencias/Exercicios/SPRINT_03_E17.png>)

[**Voltar ao Exercício 17**](#Exercício17)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício18_1"></a>

### Exercício 18

![Resultado](<Evidencias/Exercicios/SPRINT_03_E18.png>)

[**Voltar ao Exercício 18**](#Exercício18)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício19_1"></a>

### Exercício 19

![Resultado](<Evidencias/Exercicios/SPRINT_03_E19.png>)

[**Voltar ao Exercício 19**](#Exercício19)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício20_1"></a>

### Exercício 20

![Resultado](<Evidencias/Exercicios/SPRINT_03_E20.png>)

[**Voltar ao Exercício 20**](#Exercício20)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício21_1"></a>

### Exercício 21

![Resultado](<Evidencias/Exercicios/SPRINT_03_E21_1.png>)

![Resultado](<Evidencias/Exercicios/SPRINT_03_E21_2.png>)

[**Voltar ao Exercício 21**](#Exercício21)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício22_1"></a>

### Exercício 22

![Resultado](<Evidencias/Exercicios/SPRINT_03_E22.png>)

[**Voltar ao Exercício 22**](#Exercício22)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício23_1"></a>

### Exercício 23

![Resultado](<Evidencias/Exercicios/SPRINT_03_E23.png>)

[**Voltar ao Exercício 23**](#Exercício23)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício24_1"></a>

### Exercício 24

![Resultado](<Evidencias/Exercicios/SPRINT_03_E24.png>)

[**Voltar ao Exercício 24**](#Exercício24)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício25_1"></a>

### Exercício 25

![Resultado](<Evidencias/Exercicios/SPRINT_03_E25.png>)

[**Voltar ao Exercício 25**](#Exercício25)

[**Voltar ao Sumário**](#sumário)


<a id="Exercício_exp_1_1"></a>

### Exercício Exportação 1

![Resultado](<Evidencias/Exercicios/SPRINT_02_E02_02.png>)

[**Voltar ao Exercício Exportação 1**](#Exercício_exp_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício_exp_2_1"></a>

### Exercício Exportação 2

![Resultado](<Evidencias/Exercicios/SPRINT_02_E03_02.png>)

[**Voltar ao Exercício Exportação 2**](#Exercício_exp_2)

[**Voltar ao Sumário**](#sumário)

# Certificados

[AWS Partner Cloud Economics (Portuguese)](<Certificados/AWS Partner Cloud Economics (Portuguese).pdf>)

![AWS Partner Cloud Economics (Portuguese)](<Certificados/AWS Partner Cloud Economics (Portuguese).png>)

[**Voltar ao Sumário**](#sumário)