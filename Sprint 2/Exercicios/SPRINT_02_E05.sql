with 
	tabela_estado as (
select 
	estado,
	codendereco
from endereco
where estado not in ('RIO GRANDE DO SUL', 'PARANÁ')
),

	tabela_editora as (
select 
	codeditora,
	est.estado as estado
from editora as ed
right join tabela_estado as est
	on ed.endereco = est.codendereco
),

	tabela_livro as (
select 
	autor,
	editora,
	ed.estado
from livro as liv
right join tabela_editora as ed
	on liv.editora = ed.codeditora
)

select distinct nome
from autor as aut
right join tabela_livro as tab_liv
	on aut.codautor = tab_liv.autor
where aut.nome is not null
order by nome