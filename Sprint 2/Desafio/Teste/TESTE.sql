DROP TABLE tb_locacao_atual

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

CREATE TABLE tb_cliente (
	idCliente int primary key,
	nomeCliente varchar(100),
	cidadeCliente   varchar(40),
  	estadoCliente   varchar(40),
 	paisCliente     varchar(40)
);


CREATE TABLE tb_vendedor (
	idVendedor      int primary key,
	nomeVendedor    varchar(15),
	sexoVendedor    smallint,
	estadoVendedor  varchar(40)
);

CREATE TABLE tb_combustivel (
 	idcombustivel   int primary key,
 	tipoCombustivel varchar(20)
);

CREATE TABLE tb_carro (
 	idCarro  		int primary key,
 	classiCarro     varchar(50),
	marcaCarro      varchar(80),
	modeloCarro     varchar(80),
	anoCarro        int
);

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

SELECT idCliente, COUNT(*) 
FROM tb_locacao tl 
GROUP BY idCliente
HAVING COUNT(*) > 1;

SELECT * FROM tb_cliente

SELECT * FROM tb_locacao
