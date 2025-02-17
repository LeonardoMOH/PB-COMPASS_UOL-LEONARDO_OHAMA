CREATE TABLE fato_filme (
    id_filme VARCHAR(255) PRIMARY KEY,
    id_titulo INTEGER,
    id_tempo INTEGER,
    id_bridge_genero INTEGER,
    tempo_minutos INTEGER,
    popularidade FLOAT,
    orcamento INTEGER,
    receita INTEGER,
    media_votos FLOAT,
    total_votos INTEGER,
    FOREIGN KEY (id_titulo) REFERENCES dim_titulo(id_titulo),
    FOREIGN KEY (id_tempo) REFERENCES dim_tempo(id_tempo),
    FOREIGN KEY (id_bridge_genero) REFERENCES bridge_genero(id_bridge_genero)
);

CREATE TABLE dim_titulo (
    id_titulo INTEGER PRIMARY KEY,
    titulo_original TEXT
);

CREATE TABLE dim_tempo (
    id_tempo INTEGER PRIMARY KEY,
    data_lancamento DATE,
    ano INTEGER,
    mes INTEGER,
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
