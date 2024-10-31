WITH tabela_livro AS (
select autor, count(*) as quantidade
from livro
group by autor
)

select
	codautor,
	nome,
	liv.quantidade as quantidade_publicacoes
from autor as aut
join tabela_livro as liv
	on aut.codautor = liv.autor
order by liv.quantidade desc
limit 1