# Sumário

### Desafio:

1. [processamento_de_vendas.sh](Sprint1\processamento_de_vendas.sh)

2. [consolidador_de_vendas.sh](Sprint1\ecommerce\vendas\backup\consolidador_de_processamento_de_vendas.sh)

3. *[relatorio20241022.txt](Sprint1\ecommerce\vendas\backup\relatorio20241022.txt)

4. *[relatorio20241023.txt](Sprint1\ecommerce\vendas\backup\relatorio20241023.txt)

5. [relatorio20241024.txt](Sprint1\ecommerce\vendas\backup\relatorio20241024.txt)

6. [relatorio20241025.txt](Sprint1\ecommerce\vendas\backup\relatorio20241025.txt)

7. [relatorio20241026.txt](Sprint1\ecommerce\vendas\backup\relatorio20241026.txt)

8. [relatorio20241027.txt](Sprint1\ecommerce\vendas\backup\relatorio20241027.txt)

9. [relatorio_final.txt](Sprint1\ecommerce\vendas\backup\relatorio_final.txt)

10. [dados_de_vendas.csv](Sprint1\dados_de_vendas\dados_de_vendas.csv)

11. [dados_de_vendas2.csv](Sprint1\dados_de_vendas\dados_de_vendas2.csv)

12. [dados_de_vendas3.csv](Sprint1\dados_de_vendas\dados_de_vendas3.csv)

13. [dados_de_vendas4.csv](Sprint1\dados_de_vendas\dados_de_vendas4.csv)

*[Observações](#Observacoes)

1. [Etapas](#etapas)

    I.    [Etapa 1 - Verificação dos dados da tabela](#Etapa1)

    II.   [Etapa 2 - Tratamento de dados](#Etapa2)

    III.  [Etapa 3 - Criação de uma tabela auxiliar e o primeiro tratamento de dados](#Etapa3)

    IV.   [Etapa 4 - Finalização do tratamento de dados](#Etapa4)

    V.    [Etapa 5 - Criação das tabelas e normalização](#Etapa5)

    VI.   [Etapa 6 - Inserção dos dados nas novas tabelas](#Etapa6)

    VII.  [Etapa 7 - Finalização do relatorio$DATA_ARQUIVO](#Etapa7)

    VIII. [Etapa 8 - crontab](#Etapa8)

    IX.   [Etapa 9 - crontab configuração](#Etapa9)

    X.    [Etapa 10 - Segundo script](#Etapa10)

    XI.   [Observações](#Observacoes)

2. [Anexos](#anexos)

    I.    [Anexo 1 - Tabela Locacao Relacional](#Anexo1)

    II.   [Anexo 2 - Tabela Carro Relacional](#Anexo2)

    III.  [Anexo 3 - Tabela Cliente Relacional](#Anexo3)

    IV.   [Anexo 4 - Tabela Vendedor Relacional](#Anexo4)

    V.    [Anexo 5 - Tabela Combustivel Relacional](#Anexo5)

    VI.   [Anexo 6 - Primeiros outputs testes 2](#Anexo6)

    VII.  [Anexo 7 - Primeiros outputs testes 3](#Anexo7)

    VIII. [Anexo 8 - Configurações da VM](#Anexo8)

    IX.   [Anexo 9 - Local do crontab](#Anexo9)

    X.    [Anexo 10 - Relatório gerado com CSV bugado do dia 23/10/2024](#Anexo10)    

### README:

1. [README Principal](../../README.md)

2. [README Sprint 1](../README.md)

# Etapas

Explicação do desenvolvimento dos shells scripts e anexos contendo algumas informações adicionais.

<a id="Etapa1"></a>

1. ... [Etapa 1 - Verificação dos dados da tabela](#Etapa1)

    Inicialmente verifica-se os dados que contém na tabela (tb_locacao) e percebe-se alguns dados que devem ser tratados antes de começar o processo de normalização (a imagem representa apenas uma parte dela, os dados que serão tratados vão ser mostrados na etapa seguinte).
    
    ![Evidência](../Evidencias/Desafio/ETAPA1_-_TABELA_INICIAL.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa2"></a>

2. ... [Etapa 2 - Tratamento de dados](#Etapa2)

    As colunas dataLocacao e dataEntrega aparecem em um formato não desejado (YYYYMMDD) para datas e diferente dos exercícios feitos no SQL que estão no formato YYYY-MM-DD e a coluna de horaLocacao alguns horários estão no formato H:MM e não no formato HH:MM, finalmente a coluna sexoVendedor está em um "formato binário", para uma melhor visualização dos dados será trocado por M que corresponde ao sexo masculino e F para o sexo feminino.

    ![Evidência](../Evidencias/Desafio/ETAPA2_-_TABELA_TRATAMENTO_DADOS.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa3"></a>

3. ... [Etapa 3 - Criação de uma tabela auxiliar e o primeiro tratamento de dados](#Etapa3)

    Primeiro é importante ressaltar que no SQLITE é difícil de utilizar o comando ALTER TABLE para alterar a tabela, por isso foi decidido que é necessário criar tabelas novas. Para isso foi criado uma tabela auxiliar e cópia a original para que caso haja perda de dados ou alterações errôneas esses dados da tabela sejam mantidos, pois irá se utilizar o comando UPDATE que irá alterar os valores da tabela original e logo após isso executamos o comando UPDATE com o auxílio da função printf que coloca o "formato" de saída desejado que é YYYY-MM-DD e juntamente com a função SUBSTR que retorna uma string a partir da posição dada e o tamanho dela.

    ![Evidência](../Evidencias/Desafio/ETAPA3_-_TABELA_TRATAMENTO_DATA.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa4"></a>

4. ... [Etapa 4 - Finalização do tratamento de dados](#Etapa4)

    Agora é feito o tratamento de dados referente às horas que começa com o comando UPDATE e também se utiliza a função printf que foi dito anteriormente, só que agora o formato será HH:MM e logo se utiliza a função CAST para que os números sejam retornados como inteiro, pois se caso não se faça isso o horário irá retornar como H:MM para alguns horários e também se utiliza o comando SUBSTR que vai pegar a string e retornar a posição inicial que é dada até o tamanho que se deseja e também utilizada a função INSTR que é necessária diferentemente do tratamento anterior, porque no tratamento anterior não havia um problema de data no dia que em vez de retornar 01, ele retorna 1. E essa função tem o objetivo de encontrar até o separador ":" subtraindo uma unidade para que o tamanho da função SUBSTR seja até às horas, é feito esse mesmo procedimento para os minutos.
    Para o sexoVendedor também é utilizado o comando UPDATE em conjunto com o comando CASE que irá substituir o valor toda vez que corresponda ao valor dado, que no caso o "0" corresponde ao "M" e o "1" corresponde ao "F". Por fim é finalizado os dados inconsistentes da tabela.

    ![Evidência](../Evidencias/Desafio/ETAPA4_-_TABELA_TRATAMENTO_FINAL.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa5"></a>

5. ... [Etapa 5 - Criação das tabelas e normalização](#Etapa5)

    Primeiro é criado as tabelas de forma que separem elas por "objeto", exemplificando, a tabela cliente criada esteja relacionada a todos os dados relacionado ao cliente para que não tenha dependências parciais e transitivas, respeitando a 2FN e 3FN, respectivamente. E sempre criando as tabelas a partir dos IDs fornecidos que serão as chaves primárias (PK - Primary Key) para cada respectiva tabela e serão chaves estrangeiras (FK - Foreign Key) para a tabela principal que será o tb_locacao_atual, é importante ressaltar que a coluna dataLocacao da tabela principal estava do tipo DATETIME e para essa nova tabela foi utilizado o formato DATE para que se siga a normalização e os tipos que foram seguidos foram todos da tabela original. E a coluna kmCarro foi mantida na tabela principal por ser uma coluna que está ligada com o próprio idLocacao e os dados da locação e não somente ao objeto carro, esse campo é uma importante informação para verificar a km a cada locação.

    ![Evidência](../Evidencias/Desafio/ETAPA5_-_CRIACAO_TABELAS.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa6"></a>

6. ... [Etapa 6 - Inserção dos dados nas novas tabelas](#Etapa6)

    Para a inserção dos dados foi utilizado o comando INSERT INTO em conjunto com o comando SELECT e DISTINCT que irá pegar os dados não duplicados, como por exemplo, os IDs que não podem ser repetidos para respeitar a 1FN e a unicidade da chave primária, em cada tabela que contém os "objetos", como carro, combustível, cliente, vendedor. E também foi utilizado o comando Order By para ordernar em relação ao ID. Para melhor visualização dos resultados das tabelas relacionais normalizadas, elas ficarão na parte de Anexo.

    - [tb_locacao_atual](#Anexo1)
    - [tb_carro](#Anexo2)
    - [tb_cliente](#Anexo3)
    - [tb_vendedor](#Anexo4)
    - [tb_combustivel](#Anexo5)

    ![Evidência](../Evidencias/Desafio/ETAPA6_-_INSERCAO_DADOS.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa7"></a>

7. ... [Etapa 7 - Finalização do relatorio$DATA_ARQUIVO](#Etapa7)

    É deletado o arquivo auxiliar que foi utilizado para ordenação dos itens e o relatório movido para o diretório backup, logo após é movido o diretório de execução do script para compactar o arquivo backup-dados-$DATA_ARQUIVO.csv e em seguida é removido o arquivo csv, deixando apenas o arquivo compactado e para finalizar é deletado o arquivo dados_de_vendas.csv.
    
    ![Evidência](../Evidencias/ETAPA7_-_FINALIZACAO_DO_RELATORIO.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa8"></a>

8. ... [Etapa 8 - crontab](#Etapa8)

    O crontab é um comando para agendar execuções no linux para isso é utilizado o crontab -e no terminal para editar o agendamento para executar o shell script.

    ![Evidência](../Evidencias/ETAPA8_-_CRONTAB.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa9"></a>

9. ... [Etapa 9 - crontab configuração](#Etapa9)

    Para a sua configuração é colocado para o crontab executar o processamento_de_vendas.sh às 15h27 nos dias quinta-feira a domingo, vale ressaltar que no comando é mudado o diretório de execução para a pasta raiz da Sprint1, porque se caso não se faça isso o shell script vai tentar executar no diretório home.

    ![Evidência](../Evidencias/ETAPA9_-_CRONTAB.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa10"></a>

10. ... [Etapa 10 - Segundo script](#Etapa10)

    Após executado em quatro dias consecutivos o script, agora é gerado um relatório final com a junção dos quatro relatórios.

    ![Evidência](../Evidencias/ETAPA10_-_SEGUNDO_SCRIPT.png)

    ![Evidêcia](../Evidencias/ETAPA11_-_RELATORIO_FINAL.png)

[**Voltar ao Sumário**](#sumário)

<a id="Observacoes"></a>

11. ... [Observações](#Observacoes)

    I. O relatório do dia 22/10/2024 teve um pequeno erro no começo da data que está no formato DD/MM/YYYY que não é o pedido pelo desafio, portanto, o problema foi arrumado no dia 24/10 e foi feito um novo relatório no dia 27/10 com a correção. O desafio pedia que o formato da data inicial fosse YYYY/MM/AA.

    ![Evidência](../Evidencias/ANEXO3_-_PRIMEIRO_RELATORIO.png)

    II. Durante o dia 23/10/2024 tive um problema ao rodar script que fornecia um relatório com output errado, porém o problema foi resolvido por um conflito com arquivo CSV e não com o código do programa.

    ![Evidência](../Evidencias/ANEXO10_-_RELATORIO_GERADO_COM_CSV_BUGADO.png)

    III. O arquivo do crontab está localizado no diretório /var/spool/cron/crontabs da VM Linux Ubuntu.

    IV. dados_de_vendas.csv = 27/10/2024
        dados_de_vendas2.csv = 24/10/2024
        dados_de_vendas3.csv = 25/10/2024
        dados_de_vendas4.csv = 26/10/2024

[**Voltar ao Sumário**](#sumário)

## Anexos

<a id="Anexo1"></a>

1. ... [Anexo 1 - Tabela Locacao Relacional](#Anexo1)

    ![Evidência](../Evidencias/Desafio/ANEXO1_-_TABELA_LOCACAO_RELACIONAL.png)

[**Voltar a Etapa 6**](#Etapa6)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo2"></a>

2. ... [Anexo 2 - Tabela Carro Relacional](#Anexo2)

    ![Evidência](../Evidencias/Desafio/ANEXO2_-_TABELA_CARRO_RELACIONAL.png)

[**Voltar a Etapa 6**](#Etapa6)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo3"></a>

3. ... [Anexo 3 - Tabela Cliente Relacional](#Anexo3)

    ![Evidência](../Evidencias/Desafio/ANEXO3_-_TABELA_CLIENTE_RELACIONAL.png)

[**Voltar a Etapa 6**](#Etapa6)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo4"></a>

4. ... [Anexo 4 - Tabela Vendedor Relacional](#Anexo4)

    ![Evidência](../Evidencias/Desafio/ANEXO4_-_TABELA_VENDEDOR_RELACIONAL.png)

[**Voltar a Etapa 6**](#Etapa6)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo5"></a>

5. ... [Anexo 5 - Tabela Combustivel Relacional](#Anexo5)

    ![Evidência](../Evidencias/Desafio/ANEXO5_-_TABELA_COMBUSTIVEL_RELACIONAL.png)

[**Voltar a Etapa 6**](#Etapa6)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo6"></a>

6. ... [Anexo 6 - Primeiros outputs testes 2](#Anexo6)

    ![Evidência](../Evidencias/ANEXO6_-_PRIMEIROS_OUTPUTS_TESTES_2.png)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo7"></a>

7. ... [Anexo 7 - Primeiros outputs testes 3](#Anexo7)

    ![Evidência](../Evidencias/ANEXO7_-_PRIMEIROS_OUTPUTS_TESTES_3.png)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo8"></a>

8. ... [Anexo 8 - Configurações da VM](#Anexo8)

    ![Evidência](../Evidencias/ANEXO8_-_CONFIGURACOES_DA_VM.png)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo9"></a>

9. ... [Anexo 9 - Local do crontab](#Anexo9)

    ![Evidência](../Evidencias/ANEXO9_-_CRONTAB_LOCAL.png)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo10"></a>

10. ... [Anexo 10 - Relatório gerado com CSV bugado do dia 23/10/2024](#Anexo10)

    ![Evidência](../Evidencias/ANEXO10_-_RELATORIO_GERADO_COM_CSV_BUGADO.png)    

[**Voltar ao Sumário**](#sumário)