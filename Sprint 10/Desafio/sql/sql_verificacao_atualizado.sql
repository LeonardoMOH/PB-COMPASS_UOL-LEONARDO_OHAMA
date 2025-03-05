-- Carregar os arquivos parquet e criar tabelas baseados nelas

CREATE TABLE fato_filme AS 
SELECT * FROM read_parquet('C:\GitHub\PB-COMPASS_UOL-LEONARDO_OHAMA\Sprint 9\Desafio\parquet\GLUE\fato_filme\*.parquet');

CREATE TABLE bridge_genero AS
SELECT * FROM read_parquet('C:\GitHub\PB-COMPASS_UOL-LEONARDO_OHAMA\Sprint 9\Desafio\parquet\GLUE\bridge_genero\*.parquet');

CREATE TABLE dim_titulo AS
SELECT * FROM read_parquet('C:\GitHub\PB-COMPASS_UOL-LEONARDO_OHAMA\Sprint 9\Desafio\parquet\GLUE\dim_titulo\*.parquet');

CREATE TABLE dim_genero AS
SELECT * FROM read_parquet('C:\GitHub\PB-COMPASS_UOL-LEONARDO_OHAMA\Sprint 9\Desafio\parquet\GLUE\dim_genero\*.parquet')

CREATE TABLE dim_tempo AS
SELECT * FROM read_parquet('C:\GitHub\PB-COMPASS_UOL-LEONARDO_OHAMA\Sprint 9\Desafio\parquet\GLUE\dim_tempo\*.parquet')

-- Junção entre todas as tabelas (filmes, dim_titulo, dim_tempo, bridge_genero e dim_genero)
SELECT 
    f.id_filme,
    t.id_titulo,
    t.titulo_original,
    tempo.id_tempo,
    bg.id_genero,
    dg.genero,
    f.tempo_minutos,
    f.popularidade,
    f.orcamento,
    f.receita,
    f.media_votos,
    f.total_votos,
    tempo.data_lancamento
FROM fato_filme f
JOIN dim_titulo t ON f.id_titulo = t.id_titulo
JOIN dim_tempo tempo ON f.id_tempo = tempo.id_tempo
JOIN bridge_genero bg ON f.id_bridge_genero = bg.id_bridge_genero
JOIN dim_genero dg ON bg.id_genero = dg.id_genero;

-- Verificação dos filmes presentes na análises

SELECT 
    titulo_original
FROM dim_titulo
WHERE titulo_original IN (
    'Psycho',
    'The Exorcist',
    'The Shining',
    'The Blair Witch Project',
    'Saw',
    'Get Out',
    'The Invisible Man'
);

SELECT 
    categoria, 
    COUNT(*) AS total
FROM (
    SELECT 
        bg.id_bridge_genero, 
        CASE 
            WHEN COUNT(DISTINCT bg.id_genero) = 1 THEN 'Somente Horror'
            ELSE 'Multigênero'
        END AS categoria
    FROM bridge_genero bg
    GROUP BY bg.id_bridge_genero
) AS subquery
GROUP BY categoria;
