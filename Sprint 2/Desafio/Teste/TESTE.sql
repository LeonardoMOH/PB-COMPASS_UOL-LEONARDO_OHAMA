DROP TABLE tb_locacao_atual, tb_cliente, tb_vendedor, tb_combustivel, tb_carro

-- Criacao de tabelas 

-- Tabela que contem as informacoes de locacao com o idlocacao como primary key (PK) e os outros IDs como chaves estrangeiras (FK)

CREATE TABLE tb_locacao_atual (
	idLocacao int primary key,
	kmCarro         int,
	dataLocacao     datetime,
 	horaLocacao     time,
	qtdDiaria       int,
	vlrDiaria       decimal(18,2),
 	dataEntrega     date,
	horaEntrega     time,
	idCliente 		int,
	idVendedor      int,
	idcombustivel   int,
	idCarro  		int,
	FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
	FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor),
	FOREIGN KEY (idcombustivel) REFERENCES tb_combustivel(idcombustivel),
	FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro)
);

-- Tabela cliente com as informacoes relacionadas ao cliente

CREATE TABLE tb_cliente (
	idCliente int primary key,
	nomeCliente varchar(100),
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
	anoCarro        int
);

-- Inserindo os dados da tabela antiga nas novas criadas

INSERT INTO tb_locacao_atual (idLocacao, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCliente, idVendedor, idcombustivel,idCarro) 
SELECT DISTINCT
	idLocacao,
	kmCarro,
	dataLocacao,
	horaLocacao,
	qtdDiaria,
	vlrDiaria,
	dataEntrega,
	horaEntrega,
	idCliente,
	idVendedor,
	idcombustivel,
	idCarro
FROM tb_locacao
ORDER BY idLocacao;

INSERT INTO tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) 
SELECT DISTINCT
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
	paisCliente
FROM tb_locacao
ORDER BY idCliente;

INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) 
SELECT DISTINCT
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
FROM tb_locacao
ORDER BY idVendedor;

INSERT INTO tb_combustivel (idcombustivel, tipoCombustivel) 
SELECT DISTINCT
	idcombustivel,
	tipoCombustivel
FROM tb_locacao
ORDER BY idcombustivel;

INSERT INTO tb_carro (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro) 
SELECT DISTINCT
	idCarro,
	classiCarro,
	marcaCarro,
	modeloCarro,
	anoCarro
FROM tb_locacao
ORDER BY idCarro;

-- Verificacao se as tabelas tiveram os seus valores inseridos

SELECT * FROM tb_locacao_atual

SELECT * FROM tb_cliente

SELECT * FROM tb_vendedor

SELECT * FROM tb_combustivel

SELECT * FROM tb_carro

SELECT * FROM tb_locacao

-- Criacao do modelo dimensional por meio de Views
