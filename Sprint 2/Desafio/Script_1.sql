-- SELECT para verificar os dados da tabela original

--SELECT * FROM tb_locacao

-- Criacao de uma tabela igual ao original para manter os dados sem alteracao

CREATE TABLE tb_locacao_auxiliar AS
	SELECT * FROM tb_locacao;

-- Transformacao das datas do tipo YYYY-MM-DD

-- Colocando as datas no formato YYYY-MM-DD que anteriormente estavam em YYYYMMDD, dando o comando update para atualizar a coluna de data, o printf coloca o formato de saida desejado e o SUBSTR é para retornar o valor da string com a posicao dada e o tamanho dela.

UPDATE tb_locacao_auxiliar 
SET dataLocacao = printf('%04d-%02d-%02d', SUBSTR(dataLocacao, 1, 4),
										   SUBSTR(dataLocacao, 5, 2),
										   SUBSTR(dataLocacao, 7, 2));

UPDATE tb_locacao_auxiliar
SET dataEntrega = printf('%04d-%02d-%02d', SUBSTR(dataEntrega, 1, 4),
									  	   SUBSTR(dataEntrega, 5, 2),
									 	   SUBSTR(dataEntrega, 7, 2));

-- Transformacao da hora H:MM para HH:MM, o comando UPDATE atualiza as informacoes da tabela, o printf coloca no formato de HH:MM e o CAST é preciso nesse caso para transformar os numero inteiros, porque se caso não use ele irá continuar como H:MM, o SUBSTR retorna o valor de uma string com o comeco e ate o tamanho especificado, que no primeiro caso é da primeira posicao ate chegar o ":" (com a utilizacao do comando INSTR que procura ate esse termo) -1 que indicaria as horas
-- e para os minutos foi feito o mesmo procedimento com a diferença da posição da função SUBSTR

UPDATE tb_locacao_auxiliar
SET horaLocacao = printf('%02d:%02d', CAST(SUBSTR(horaLocacao, 1, INSTR(horaLocacao, ':') - 1) AS INTEGER),
											 CAST(SUBSTR(horaLocacao, INSTR(horaLocacao, ':') + 1) AS INTEGER));

-- Mudando os dados da coluna sexoVendedor, o número 0 se refere ao sexo masculino que pode ser notado pela coluna nomeVendedor e o 1 para o sexo feminino.
									 	  
UPDATE tb_locacao_auxiliar
SET sexoVendedor = 
CASE
	WHEN sexoVendedor = 0 THEN 'M'
	WHEN sexoVendedor = 1 THEN 'F'
END;
	
-- Criacao de tabelas 

-- Tabela que contém as informacoes de locacao com o idlocacao como primary key (PK) e os outros IDs como chaves estrangeiras (FK), originalmente a dataLocacao estava com o tipo datetime e agora foi ajustado para o tipo date

CREATE TABLE tb_locacao_atual (
	idLocacao		int primary key,
	idCliente 		int,
	idVendedor      int,
	idCarro  		int,
	kmCarro         int,
	dataLocacao     date,
 	horaLocacao     time,
	qtdDiaria       int,
	vlrDiaria       decimal(18,2),
 	dataEntrega     date,
	horaEntrega     time,
	FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
	FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor),
	FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro)
);

-- Tabela cliente com as informacoes relacionadas ao cliente

CREATE TABLE tb_cliente (
	idCliente		int primary key,
	nomeCliente 	varchar(100),
	cidadeCliente   varchar(40),
  	estadoCliente   varchar(40),
 	paisCliente     varchar(40)
);

-- Tabela com informacoes do vendedor

CREATE TABLE tb_vendedor (
	idVendedor      int primary key,
	nomeVendedor    varchar(15),
	sexoVendedor    smallint,
	estadoVendedor  varchar(40)
);

-- Tabela com o tipo de gasolina

CREATE TABLE tb_combustivel (
 	idcombustivel   int primary key,
 	tipoCombustivel varchar(20)
);

-- Tabela que contem as informacoes do carro

CREATE TABLE tb_carro (
 	idCarro  		int primary key,
 	classiCarro     varchar(50),
 	marcaCarro      varchar(80),
	modeloCarro     varchar(80),
	anoCarro        int,
	idcombustivel   int,
	FOREIGN KEY (idcombustivel) REFERENCES tb_combustivel(idcombustivel)
);

									  
-- Inserindo os dados da tabela antiga nas novas criadas

INSERT INTO tb_locacao_atual (idLocacao, idCliente, idVendedor, idCarro, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) 
SELECT DISTINCT
	idLocacao,
	idCliente,
	idVendedor,
	idCarro,
	kmCarro,
	dataLocacao,
	horaLocacao,
	qtdDiaria,
	vlrDiaria,
	dataEntrega,
	horaEntrega
FROM tb_locacao_auxiliar
ORDER BY idLocacao;

INSERT INTO tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) 
SELECT DISTINCT
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
	paisCliente
FROM tb_locacao_auxiliar
ORDER BY idCliente;

INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) 
SELECT DISTINCT
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
FROM tb_locacao_auxiliar
ORDER BY idVendedor;

INSERT INTO tb_combustivel (idcombustivel, tipoCombustivel) 
SELECT DISTINCT
	idcombustivel,
	tipoCombustivel
FROM tb_locacao_auxiliar
ORDER BY idcombustivel;

INSERT INTO tb_carro (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel) 
SELECT DISTINCT
	idCarro,
	classiCarro,
	marcaCarro,
	modeloCarro,
	anoCarro,
	idcombustivel
FROM tb_locacao_auxiliar
ORDER BY idCarro;	

-- Verificacao se as tabelas tiveram os seus valores inseridos (tirar o comentario para executar o SELECT)

--SELECT * FROM tb_locacao_atual;

--SELECT * FROM tb_locacao_auxiliar;

--SELECT * FROM tb_cliente;

--SELECT * FROM tb_vendedor;

--SELECT * FROM tb_combustivel;

--SELECT * FROM tb_carro;

-- Comando para deletar alguma tabela desejada (tirar o comentario para deletar a tabela respectiva)

--DROP TABLE tb_locacao_atual;

--DROP TABLE tb_locacao_auxiliar;

--DROP TABLE tb_cliente;

--DROP TABLE tb_vendedor;

--DROP TABLE tb_combustivel;

--DROP TABLE tb_carro;

-- Criacao do modelo dimensional a partir das tabelas relacionais

CREATE TABLE fato_locacao (
	idLocacao		int primary key,
	idCliente 		int,
	idVendedor      int,
	idCarro  		int,
	kmCarro         int,
	dataLocacao     date,
 	horaLocacao     time,
	qtdDiaria       int,
	vlrDiaria       decimal(18,2),
 	dataEntrega     date,
	horaEntrega     time,
	FOREIGN KEY (idCliente) REFERENCES dim_cliente(id),
	FOREIGN KEY (idVendedor) REFERENCES dim_vendedor(id),
	FOREIGN KEY (idCarro) REFERENCES dim_carro(id)
);

CREATE TABLE dim_cliente (
	id 		 int primary key,
	nome 	 varchar(100),
	cidade   varchar(40),
  	estado   varchar(40),
 	pais     varchar(40)
);

CREATE TABLE dim_vendedor (
	id      int primary key,
	nome    varchar(15),
	sexo    smallint,
	estado  varchar(40)
);

CREATE TABLE dim_carro (
 	id  			int primary key,
 	classi   		varchar(50),
 	marca     		varchar(80),
	modelo    		varchar(80),
	ano       		int,
	idcombustivel   int,
	tipoCombustivel varchar(20) 
);

-- Insert nas tabelas fato e dimensao

INSERT INTO fato_locacao (idLocacao, idCliente, idVendedor, idCarro, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega) 
SELECT DISTINCT
	idLocacao,
	idCliente,
	idVendedor,
	idCarro,
	kmCarro,
	dataLocacao,
	horaLocacao,
	qtdDiaria,
	vlrDiaria,
	dataEntrega,
	horaEntrega
FROM tb_locacao_atual
ORDER BY idLocacao;

INSERT INTO dim_cliente (id, nome, cidade, estado, pais) 
SELECT DISTINCT
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
	paisCliente
FROM tb_cliente
ORDER BY idCliente;

INSERT INTO dim_vendedor (id, nome, sexo, estado) 
SELECT DISTINCT
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
FROM tb_vendedor
ORDER BY idVendedor;

INSERT INTO dim_carro (id, classi, marca, modelo, ano, idcombustivel, tipoCombustivel) 
SELECT DISTINCT
	idCarro,
	classiCarro,
	marcaCarro,
	modeloCarro,
	anoCarro,
	tb_carro.idcombustivel,
	tipoCombustivel
FROM tb_carro
JOIN tb_combustivel ON tb_carro.idcombustivel = tb_combustivel.idcombustivel
ORDER BY idCarro;