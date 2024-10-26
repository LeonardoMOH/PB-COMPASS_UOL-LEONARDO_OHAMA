# Sumário

### Desafio:

1. [Etapas](#etapas)

    I.    [Etapa 1 - Criação do arquivo processamento_de_vendas.sh](#Etapa1)

    II.   [Etapa 2 - Interpretador, datas e horários](#Etapa2)

    III.  [Etapa 3 - Criação de diretórios e organização de arquivos](#Etapa3)

    IV.   [Etapa 4 - Criação do relatorio$DATA_ARQUIVO](#Etapa4)

    V.    [Etapa 5 - Primeiro e último itens comprados relatorio$DATA_ARQUIVO](#Etapa5)

    VI.   [Etapa 6 - Total de itens e os 10 primeiros itens relatorio$DATA_ARQUIVO](#Etapa6)

    VII.  [Etapa 7 - Finalização do relatorio$DATA_ARQUIVO](#Etapa7)

    VIII. [Etapa 8 - crontab](#Etapa8)

    IX.   [Etapa 9 - crontab configuração](#Etapa9)

    X.    [Etapa 10 - Segundo script](#Etapa10)

2. [Anexos](#anexos)

    I.    [Anexo 1 - Código](#Anexo1)

    II.   [Anexo 2 - Código](#Anexo2)

    III.  [Anexo 3 - Relatório feito no primeiro dia](#Anexo3)

    IV.   [Anexo 4 - Comando history](#Anexo4)

    V.    [Anexo 5 - Primeiros outputs testes](#Anexo5)

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

1. ... [Etapa 1 - Criação do arquivo processamento_de_vendas.sh](#Etapa1)

    Inicialmente cria-se o arquivo processamento_de_vendas.sh e move para a pasta raiz do projeto (Script1).
    
    ![Evidência](../Evidencias/ETAPA1_-_CRIACAO_DO_SHELL_SCRIPT.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa2"></a>

2. ... [Etapa 2 - Interpretador, datas e horários](#Etapa2)

    Após criado o arquivo, é escrito o interpretador do script no arquivo shell e é criado as variáveis para guardar as horas e as datas de execução do script.

    ![Evidência](../Evidencias/ETAPA2_-_INTERPRETADOR_DATAS_HORARIOS.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa3"></a>

3. ... [Etapa 3 - Criação de diretórios e organização de arquivos](#Etapa3)

    Agora é criado o diretório ecommerce e o arquivo de dados_de_vendas.csv é movido para essa pasta, logo em seguida, as pastas vendas e backup são criados (obs: é utilizado a flag -p para evitar erro de criação de pasta já existente) e depois isso é movido o diretório de execução do script para que seja feito as execuções do comando para o backup do arquivo dados_de_vendas.csv que acabou de ser movido.

    ![Evidência](../Evidencias/ETAPA3_-_CRIACAO_DE_DIRETORIOS_E_ORGANIZACAO.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa4"></a>

4. ... [Etapa 4 - Criação do relatorio$DATA_ARQUIVO](#Etapa4)

    Agora é criado o relatório$DATA_ARQUIVO.txt que irá receber os outputs do arquivo processado dados_de_vendas. Primeiramente é feito o comando echo que irá registrar o dia e horário que fora registrado anteriormente e logo após isso é utilizado o comando awk para criar uma coluna auxiliar em um segundo arquivo para processar a ordenação do sort para isso no comando awk é imprimir todas as colunas já existentes e na sexta coluna é criado a coluna auxiliar que consiste na data no formato YYYYMMDD, pois utilizando o comando sort em uma data DD/MM/YYYY é ordenado somente pelo dia, ou seja, se uma data 01/03/2024 é comparado com uma data 25/01/2024 com o comando sort a primeira data estará na frente da segunda data. Portanto, no comando sort é utilizado a ordenação numérica na sexta coluna (lembrando que foi utilizado as tags para respeitarem os separadores do arquivo csv).

    ![Evidência](../Evidencias/ETAPA4_-_CRIACAO_DO_RELATORIO.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa5"></a>

5. ... [Etapa 5 - Primeiro e último itens comprados relatorio$DATA_ARQUIVO](#Etapa5)

    Depois de processado a ordenação, se imprime a segunda linha (por causa do cabeçalho) que irá consistir na primeira data do registro de venda e o último registro de venda contendo a data do mesmo (novamente é utilizado o comando BEGIN para adicionar as virgulas no output).

    ![Evidência](../Evidencias/ETAPA5_-_PRIMEIRO_E_ULTIMO_ITEM.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa6"></a>

6. ... [Etapa 6 - Total de itens e os 10 primeiros itens relatorio$DATA_ARQUIVO](#Etapa6)

    Agora é contabilizado o número de itens diferentes e pegar as primeiras 10 linhas do arquivo csv, para isso foi utilizado o comando cut para filtrar as duplicadas na coluna 2 que corresponde ao nome do item, exemplo: camiseta e é utilizado o pipeline para um comando seguinte ter a saída do outro, sendo assim, primeiro é "selecionado" pela 2 coluna e em seguinda é tirado com o tail o cabeçalho da tabela e em seguida é utilizado o sort para conseguir tirar duplicatas com o comando uniq e finalmente é utilizado o wc para somar todos os itens restantes.

    ![Evidência](../Evidencias/ETAPA6_-_TOTAL_E_OS_10_PRIMEIROS_ITENS.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa7"></a>

7. ... [Etapa 7 - Finalização do relatorio$DATA_ARQUIVO](#Etapa7)

    É deletado o arquivo auxiliar que foi utilizado para ordenação dos itens e o relatório é movido para o diretório backup e logo após é movido o diretório de execução do script para compactar o arquivo backup-dados-$DATA_ARQUIVO.csv e é removido o arquivo csv, deixando só o arquivo compactado e logo após é deletado o arquivo dados_de_vendas.csv.
    
    ![Evidência](../Evidencias/ETAPA7_-_FINALIZACAO_DO_RELATORIO.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa8"></a>

8. ... [Etapa 8 - crontab](#Etapa8)

    O crontab é um comando para agendar execuções no linux para isso é utilizado o crontab -e no terminal para editar o agendamento para executar o shell script.

    ![Evidência](../Evidencias/ETAPA8_-_CRONTAB.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa9"></a>

9. ... [Etapa 9 - crontab configuração](#Etapa9)

    Para a sua configuração é colocado para o crontab executar o processamento_de_vendas.sh às 15h27 nos dias terça-feira a sábado, vale ressaltar que no comando é mudado o diretório de execução para a pasta raiz da Sprint1, porque se caso não se faça isso o shell script vai tentar executar no diretório home.

    ![Evidência](../Evidencias/ETAPA9_-_CRONTAB.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa10"></a>

10. ... [Etapa 10 - Segundo script](#Etapa10)

    Após executado em quatro dias consecutivos o script, agora é gerado um relatório final com a junção dos quatro relatórios.

    ![Evidência](../Evidencias/ETAPA10_-_SEGUNDO_SCRIPT.png)

[**Voltar ao Sumário**](#sumário)

<a id="Observacoes"></a>

11. ... [Observações](#Observacoes)

    I. O relatório do dia 22/10/2024 teve um pequeno erro no começo da data que está no formato DD/MM/YYYY que não é o pedido pelo desafio, portanto, o problema foi arrumado no dia 24/10. O desafio pedia que o formato da data inicial fosse YYYY/MM/AA.

    ![Evidência](../Evidencias/ANEXO3_-_PRIMEIRO_RELATORIO.png)

    II. Durante o dia 23/10/2024 tive um problema ao rodar script que fornecia um relatório com output errado, porém o problema foi resolvido por um conflito com arquivo CSV e não com o código do programa.

    ![Evidência](../Evidencias/ANEXO10_-_RELATORIO_GERADO_COM_CSV_BUGADO.png)

[**Voltar ao Sumário**](#sumário)

## Anexos

<a id="Anexo1"></a>

1. ... [Anexo 1 - Código](#Anexo1)

    ![Evidência](../Evidencias/ANEXO1_-_CODIGO.png)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo2"></a>

2. ... [Anexo 2 - Código](#Anexo2)

    ![Evidência](../Evidencias/ANEXO2_-_CODIGO.png)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo3"></a>

3. ... [Anexo 3 - Relatório feito no primeiro dia](#Anexo3)

    ![Evidência](../Evidencias/ANEXO3_-_PRIMEIRO_RELATORIO.png)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo4"></a>

4. ... [Anexo 4 - Comando history](#Anexo4)

    ![Evidência](../Evidencias/ANEXO4_-_COMANDO_HISTORY.png)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo5"></a>

5. ... [Anexo 5 - Primeiros outputs testes](#Anexo5)

    ![Evidência](../Evidencias/ANEXO5_-_PRIMEIROS_OUTPUTS_TESTES.png)

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