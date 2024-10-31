WITH tabela_livro AS (
select autor, count(*) as quantidade
from livro
group by autor
)

select
	nome,	
	codautor,
	nascimento,
	ifnull(liv.quantidade,0) as quantidade
from autor as aut
left join tabela_livro as liv
	on aut.codautor = liv.autor
order by nome