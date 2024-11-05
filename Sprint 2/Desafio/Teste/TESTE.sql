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
	idCarro  		int,
	FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
	FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor),
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
	modeloCarro     varchar(80),
	anoCarro        int,
	idcombustivel   int,
	FOREIGN KEY (idcombustivel) REFERENCES tb_combustivel(idcombustivel),
	FOREIGN KEY (modeloCarro) REFERENCES tb_marca(modeloCarro)
);

CREATE TABLE tb_marca (
	modeloCarro     varchar(80) primary key,
	marcaCarro      varchar(80)
);

-- Inserindo os dados da tabela antiga nas novas criadas

INSERT INTO tb_locacao_atual (idLocacao, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCliente, idVendedor, idCarro) 
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

INSERT INTO tb_carro (idCarro, classiCarro, modeloCarro, anoCarro, idcombustivel) 
SELECT DISTINCT
	idCarro,
	classiCarro,
	modeloCarro,
	anoCarro,
	idcombustivel
FROM tb_locacao
ORDER BY idCarro;

INSERT INTO tb_marca (modeloCarro, marcaCarro) 
SELECT DISTINCT
	modeloCarro,
	marcaCarro
FROM tb_locacao
ORDER BY modeloCarro;

-- Verificacao se as tabelas tiveram os seus valores inseridos (tirar o comentario para executar o SELECT)

--SELECT * FROM tb_locacao_atual;

--SELECT * FROM tb_cliente;

--SELECT * FROM tb_vendedor;

--SELECT * FROM tb_combustivel;

--SELECT * FROM tb_carro;

--SELECT * FROM tb_locacao;

--SELECT * FROM tb_marca;

-- Comando para deletar alguma tabela desejada (tirar o comentario para deletar a tabela respectiva)

--DROP TABLE tb_locacao_atual;

--DROP TABLE tb_cliente;

--DROP TABLE tb_vendedor;

--DROP TABLE tb_combustivel;

--DROP TABLE tb_carro;

--DROP TABLE tb_marca;

-- Criacao do modelo dimensional por meio de Views
