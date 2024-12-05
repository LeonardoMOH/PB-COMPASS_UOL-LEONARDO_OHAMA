# Sumário

### Sprint 4:

1. [Resumo](#resumo)

2. [Exercícios](#exercícios)

    I.    [Exercício 01](#Exercício01)

    II.   [Exercício 02](#Exercício02)

    III.  [Exercício 03](#Exercício03)

    IV.   [Exercício 04](#Exercício04)

    V.    [Exercício 05](#Exercício05)

    VI.   [Exercício 06](#Exercício06)

    VII.  [Exercício 07](#Exercício07)

3. [Evidências](#evidências)

4. [Certificados](#certificados)

### README:

1. [README Principal](../README.md)

2. [README Desafio](<Desafio/README.md>)

# Resumo

📊‍ **Docker:** No curso de Docker aprendemos a instalar o Docker, fazer containers, imagens, volumes, conexão com Networks, Docker Swarm e Kubernetes.

✍️‍ **AWS:** No curso de AWS aprendi os diversos serviços da AWS, como o Amazon EFS, EC2, S3 Bucket, entre outros.

🎯 **Desafio** O desafio consiste em criar arquivos Dockerfile para criar um container a partir de uma imagem, executar arquivos Python e também demonstrar se é possível reutilizar containers já criados.

[**Voltar ao Sumário**](#sumário)

# Exercícios 🥋

<a id="Exercício01"></a>

### Exercício 01

Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.



Você deverá aplicar as seguintes funções no exercício:



map

filter

sorted

sum



Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):



a lista dos 5 maiores números pares em ordem decrescente;

a soma destes valores.

[Solução Python Exercício 01](Exercicios/SPRINT_04_E01.py)

[Resultado Exercício 01](#Exercício01_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício02"></a>

### Exercício 02

Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.



É obrigatório aplicar as seguintes funções:

len

filter

lambda



Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.

[Solução Python Exercício 02](Exercicios/SPRINT_04_E02.py)

[Resultado Exercício 02](#Exercício02_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício03"></a>

### Exercício 03

A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 

Abaixo apresentando uma possível entrada para a função.



lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]


A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, por exemplo, teríamos como resultado final 200.



Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:



reduce (módulo functools)

map

[Solução Python Exercício 03](Exercicios/SPRINT_04_E03.py)

[Resultado Exercício 03](#Exercício03_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício04"></a>

### Exercício 04

A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.



Veja o exemplo:



Entrada

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]


Aplicar as operações aos pares de operandos

[ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 


Obter o maior dos valores

12


Na resolução da atividade você deverá aplicar as seguintes funções:

max

zip

map

[Solução Python Exercício 04](Exercicios/SPRINT_04_E04.py)

[Resultado Exercício 04](#Exercício04_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício05"></a>

### Exercício 05

Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.



Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:



Nome do estudante

Três maiores notas, em ordem decrescente

Média das três maiores notas, com duas casas decimais de precisão

O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:



Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>



Exemplo:

Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67

Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33



Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:

round

map

sorted

[Solução Python Exercício 05](Exercicios/SPRINT_04_E05.py)

[Resultado Exercício 05](#Exercício05_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício06"></a>

### Exercício 06

Você foi encarregado de desenvolver uma nova feature  para um sistema de gestão de supermercados. O analista responsável descreveu o requisito funcional da seguinte forma:



- Para realizar um cálculo de custo, o sistema deverá permitir filtrar um determinado conjunto de produtos, de modo que apenas aqueles cujo valor unitário for superior à média deverão estar presentes no resultado. Vejamos o exemplo:



Conjunto de produtos (entrada):



Arroz: 4.99

Feijão: 3.49

Macarrão: 2.99

Leite: 3.29

Pão: 1.99



Produtos com valor acima da média:

Arroz: 4.99

Feijão: 3.49





Observe que estamos definindo a assinatura de uma função como parte de sua resposta. Você não pode mudá-la, apenas codificar seu corpo. O parâmetro conteudo é um dicionário cuja chave contém o nome do produto e o valor, o respectivo preço (ponto flutuante).

Observe um exemplo de valor para conteudo:



{
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}
O retorno da função obrigatoriamente deve ser uma lista. Cada elemento da lista é uma tupla em que a primeira posição contém o nome do produto e a segunda, o respectivo preço. Veja um exemplo de retorno:



[
 
('feijão', 3.49),
 
 ('arroz', 4.99)
 
]


Importante: O retorno da função deve estar ordenado pelo preço do item (ordem crescente).

[Solução Python Exercício 06](Exercicios/SPRINT_04_E06.py)

[Resultado Exercício 06](#Exercício06_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício07"></a>

### Exercício 07

Generators são poderosos recursos da linguagem Python. Neste exercício, você deverá criar o corpo de uma função, cuja assinatura já consta em seu arquivo de início (def pares_ate(n:int):) .

O objetivo da função pares_ate é retornar um generator para os valores pares no intervalo [2,n] . Observe que n representa o valor do parâmetro informado na chamada da função.

[Solução Python Exercício 07](Exercicios/SPRINT_04_E07.py)

[Resultado Exercício 07](#Exercício07_1)

[**Voltar ao Sumário**](#sumário)

# Evidências

## Desafio

[Evidências Desafio](<Desafio/README.md#etapas>)

[**Voltar ao Sumário**](#sumário)

## Exercícios

<a id="Exercício01_1"></a>

### Exercício 01

![Resultado](<Evidencias/Exercicios/SPRINT_04_E01.png>)

[**Voltar ao Exercício 01**](#Exercício01)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício02_1"></a>

### Exercício 02

![Resultado](<Evidencias/Exercicios/SPRINT_04_E02.png>)

[**Voltar ao Exercício 02**](#Exercício02)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício03_1"></a>

### Exercício 03

![Resultado](<Evidencias/Exercicios/SPRINT_04_E03.png>)

[**Voltar ao Exercício 03**](#Exercício03)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício04_1"></a>

### Exercício 04

![Resultado](<Evidencias/Exercicios/SPRINT_04_E04.png>)

[**Voltar ao Exercício 04**](#Exercício04)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício05_1"></a>

### Exercício 05

![Resultado](<Evidencias/Exercicios/SPRINT_04_E05.png>)

[**Voltar ao Exercício 05**](#Exercício05)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício06_1"></a>

### Exercício 06

![Resultado](<Evidencias/Exercicios/SPRINT_04_E06.png>)

[**Voltar ao Exercício 06**](#Exercício06)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício07_1"></a>

### Exercício 07

![Resultado](<Evidencias/Exercicios/SPRINT_04_E07.png>)

[**Voltar ao Exercício 07**](#Exercício07)

[**Voltar ao Sumário**](#sumário)

# Certificados

[AWS Partner Credenciamento (Tecnico) (Portugues) AWS Partner Accreditation (Tecnical) (Portugues)](<Certificados/AWS Partner Credenciamento (Tecnico) (Portugues) AWS Partner Accreditation (Tecnical) (Portugues).pdf>)

![AWS Partner Credenciamento (Tecnico) (Portugues) AWS Partner Accreditation (Tecnical) (Portugues)](<Certificados/AWS Partner Credenciamento (Tecnico) (Portugues) AWS Partner Accreditation (Tecnical) (Portugues).png>)

[Fundamentos Tecnicos Da AWS (Portugues) AWS Tecnical Essentials (Portuguese)](<Certificados/Fundamentos Tecnicos Da AWS (Portugues) AWS Tecnical Essentials (Portuguese).pdf>)

![Fundamentos Tecnicos Da AWS (Portugues) AWS Tecnical Essentials (Portuguese)](<Certificados/Fundamentos Tecnicos Da AWS (Portugues) AWS Tecnical Essentials (Portuguese).png>)

[**Voltar ao Sumário**](#sumário)