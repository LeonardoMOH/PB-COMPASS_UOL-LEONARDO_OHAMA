CREATE TABLE fato_filme (
    id_filme VARCHAR(255) PRIMARY KEY,
    id_titulo INTEGER,
    id_ano INTEGER,
    id_mes INTEGER,
    id_dia INTEGER,
    id_bridge_genero INTEGER,
    tempo_minutos INTEGER,
    popularidade FLOAT,
    orcamento INTEGER,
    receita INTEGER,
    media_votos FLOAT,
    total_votos INTEGER,
    FOREIGN KEY (id_titulo) REFERENCES dim_titulo(id_titulo),
    FOREIGN KEY (id_ano) REFERENCES dim_ano(id_ano),
    FOREIGN KEY (id_mes) REFERENCES dim_mes(id_mes),
    FOREIGN KEY (id_dia) REFERENCES dim_dia(id_dia),
    FOREIGN KEY (id_bridge_genero) REFERENCES bridge_genero(id_bridge_genero)
);

CREATE TABLE dim_titulo (
    id_titulo INTEGER PRIMARY KEY,
    titulo_original TEXT
);

CREATE TABLE dim_ano (
    id_ano INTEGER PRIMARY KEY,
    ano INTEGER
);

CREATE TABLE dim_mes (
    id_mes INTEGER PRIMARY KEY,
    mes INTEGER
);

CREATE TABLE dim_dia (
    id_dia INTEGER PRIMARY KEY,
    dia INTEGER
);

CREATE TABLE dim_genero (
    id_genero INTEGER PRIMARY KEY,
    genero TEXT
);

CREATE TABLE bridge_genero (
    id_bridge_genero INTEGER PRIMARY KEY,
    id_genero INTEGER,
    FOREIGN KEY (id_genero) REFERENCES dim_genero(id_genero)
);
