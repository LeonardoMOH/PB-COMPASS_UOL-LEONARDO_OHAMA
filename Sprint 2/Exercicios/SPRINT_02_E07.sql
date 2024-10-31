WITH tabela_livro AS (
select autor, count(*) as quantidade
from livro
group by autor
)

select
	nome
from autor as aut
left join tabela_livro as liv
	on aut.codautor = liv.autor
where liv.quantidade is null
order by nome