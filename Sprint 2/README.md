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

    XVII. [Exercício Exportação 1](#Exercício_exp_1)

    XVIII.[Exercício Exportação 2](#Exercício_exp_2)

3. [Evidências](#evidências)

4. [Certificados](#certificados)

### README:

1. [README Principal](../README.md)

2. [README Desafio](<Desafio/README.md>)

# Resumo

📊‍ **SQL:** No curso de SQL, eu aprendi vários comandos para manipulação de tabelas, como SELECT, JOIN, UNION etc. E os operadores AND, OR, BETWEEN etc. No final do curso foi proposto exercícios para praticar o primeiro foi dos exercícios 01 ao 07 com o estudo de caso da biblioteca, os exercícios do 08 ao 16 foi o estudo de caso da loja e o exercício II que consistia em exportar os dados da tabela em formato csv com diferente separadores.

🎯 **Desafio** O desafio consiste em normalizar os dados da tabela tb_locacao que contém todos os dados das tabelas IDs do arquivo concessionaria com o Modelo Relacional e depois montar com base nesse modelo normalizado o Modelo Dimensional.

[**Voltar ao Sumário**](#sumário)

# Exercícios 🥋

## Caso de Estudo: Biblioteca 📖

<a id="Exercício01"></a>

### Exercício 01

Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma.

[Solução SQL Exercício 01](Exercicios/SPRINT_02_E01.sql)

[Resultado Exercício 01](#Exercício01_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício02"></a>

### Exercício 02

Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor.

[Solução SQL Exercício 02](Exercicios/SPRINT_02_E02.sql)

[Resultado Exercício 02](#Exercício02_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício03"></a>

### Exercício 03

Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

[Solução SQL Exercício 03](Exercicios/SPRINT_02_E03.sql)

[Resultado Exercício 03](#Exercício03_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício04"></a>

### Exercício 04

Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

[Solução SQL Exercício 04](Exercicios/SPRINT_02_E04.sql)

[Resultado Exercício 04](#Exercício04_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício05"></a>

### Exercício 05

Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

[Solução SQL Exercício 05](Exercicios/SPRINT_02_E05.sql)

[Resultado Exercício 05](#Exercício05_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício06"></a>

### Exercício 06

Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

[Solução SQL Exercício 06](Exercicios/SPRINT_02_E06.sql)

[Resultado Exercício 06](#Exercício06_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício07"></a>

### Exercício 07

Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

[Solução SQL Exercício 07](Exercicios/SPRINT_02_E07.sql)

[Resultado Exercício 07](#Exercício07_1)

[**Voltar ao Sumário**](#sumário)

## Caso de Estudo: Loja

<a id="Exercício08"></a>

### Exercício 08

Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

[Solução SQL Exercício 08](Exercicios/SPRINT_02_E08.sql)

[Resultado Exercício 08](#Exercício08_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício09"></a>

### Exercício 09

Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

[Solução SQL Exercício 09](Exercicios/SPRINT_02_E09.sql)

[Resultado Exercício 09](#Exercício09_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício10"></a>

### Exercício 10

A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

[Solução SQL Exercício 10](Exercicios/SPRINT_02_E10.sql)

[Resultado Exercício 10](#Exercício10_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício11"></a>

### Exercício 11

Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

[Solução SQL Exercício 11](Exercicios/SPRINT_02_E11.sql)

[Resultado Exercício 11](#Exercício11_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício12"></a>

### Exercício 12

Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.


Observação: Apenas vendas com status concluído.

[Solução SQL Exercício 12](Exercicios/SPRINT_02_E12.sql)

[Resultado Exercício 12](#Exercício12_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício13"></a>

### Exercício 13

Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

[Solução SQL Exercício 13](Exercicios/SPRINT_02_E13.sql)

[Resultado Exercício 13](#Exercício13_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício14"></a>

### Exercício 14

Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

Observação: Apenas vendas com status concluído.

[Solução SQL Exercício 14](Exercicios/SPRINT_02_E14.sql)

[Resultado Exercício 14](#Exercício14_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício15"></a>

### Exercício 15

Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

[Solução SQL Exercício 15](Exercicios/SPRINT_02_E15.sql)

[Resultado Exercício 15](#Exercício15_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício16"></a>

### Exercício 16

Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).

Obs: Somente vendas concluídas.

[Solução SQL Exercício 16](Exercicios/SPRINT_02_E16.sql)

[Resultado Exercício 16](#Exercício16_1)

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

![Resultado](<Evidencias/Exercicios/SPRINT_02_E01.png>)

[**Voltar ao Exercício 01**](#Exercício01)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício02_1"></a>

### Exercício 02

![Resultado](<Evidencias/Exercicios/SPRINT_02_E02.png>)

[**Voltar ao Exercício 02**](#Exercício02)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício03_1"></a>

### Exercício 03

![Resultado](<Evidencias/Exercicios/SPRINT_02_E03.png>)

[**Voltar ao Exercício 03**](#Exercício03)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício04_1"></a>

### Exercício 04

![Resultado](<Evidencias/Exercicios/SPRINT_02_E04.png>)

[**Voltar ao Exercício 04**](#Exercício04)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício05_1"></a>

### Exercício 05

![Resultado](<Evidencias/Exercicios/SPRINT_02_E05.png>)

[**Voltar ao Exercício 05**](#Exercício05)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício06_1"></a>

### Exercício 06

![Resultado](<Evidencias/Exercicios/SPRINT_02_E06.png>)

[**Voltar ao Exercício 06**](#Exercício06)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício07_1"></a>

### Exercício 07

![Resultado](<Evidencias/Exercicios/SPRINT_02_E07.png>)

[**Voltar ao Exercício 07**](#Exercício07)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício08_1"></a>

### Exercício 08

![Resultado](<Evidencias/Exercicios/SPRINT_02_E08.png>)

[**Voltar ao Exercício 08**](#Exercício08)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício09_1"></a>

### Exercício 09

![Resultado](<Evidencias/Exercicios/SPRINT_02_E09.png>)

[**Voltar ao Exercício 09**](#Exercício09)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício10_1"></a>

### Exercício 10

![Resultado](<Evidencias/Exercicios/SPRINT_02_E10.png>)

[**Voltar ao Exercício 10**](#Exercício10)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício11_1"></a>

### Exercício 11

![Resultado](<Evidencias/Exercicios/SPRINT_02_E11.png>)

[**Voltar ao Exercício 11**](#Exercício11)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício12_1"></a>

### Exercício 12

![Resultado](<Evidencias/Exercicios/SPRINT_02_E12.png>)

[**Voltar ao Exercício 12**](#Exercício12)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício13_1"></a>

### Exercício 13

![Resultado](<Evidencias/Exercicios/SPRINT_02_E13.png>)

[**Voltar ao Exercício 13**](#Exercício13)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício14_1"></a>

### Exercício 14

![Resultado](<Evidencias/Exercicios/SPRINT_02_E14.png>)

[**Voltar ao Exercício 14**](#Exercício14)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício15_1"></a>

### Exercício 15

![Resultado](<Evidencias/Exercicios/SPRINT_02_E15.png>)

[**Voltar ao Exercício 15**](#Exercício15)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício16_1"></a>

### Exercício 16

![Resultado](<Evidencias/Exercicios/SPRINT_02_E16.png>)

[**Voltar ao Exercício 16**](#Exercício16)

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

[AWS Partner: Sales Accreditation (Business) (Portuguese) PDF](<Certificados/AWS Partner Sales Accreditation (Business) (Portuguese).pdf>)

![AWS Partner: Sales Accreditation (Business) (Portuguese)](<Certificados/AWS Partner Sales Accreditation (Business) (Portuguese).png>)

[**Voltar ao Sumário**](#sumário)