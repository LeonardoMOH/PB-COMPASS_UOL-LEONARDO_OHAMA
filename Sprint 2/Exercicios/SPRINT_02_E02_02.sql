with
	editora_livro as (
	select distinct		
		ed.codeditora,
		ed.nome,
		liv.editora,
		liv.autor,
		liv.titulo,
		liv.cod,
		liv.valor
	from editora as ed
	join livro as liv
		on ed.codeditora = liv.editora
),

	autor_livro as (
	select distinct		
		aut.codautor,
		aut.nome,
		liv.editora,
		liv.autor
	from autor as aut
	join livro as liv
		on aut.codautor = liv.autor
)

select distinct
	cod as CodLivro,
	titulo as Titulo,
	aut_liv.codautor as CodAutor,
	aut_liv.nome as NomeAutor,
	valor as Valor,
	ed_liv.codeditora as CodEditora,
	ed_liv.nome	as NomeEditora
from editora_livro as ed_liv
join autor_livro as aut_liv
	on ed_liv.autor = aut_liv.autor
order by valor DESC
limit 10