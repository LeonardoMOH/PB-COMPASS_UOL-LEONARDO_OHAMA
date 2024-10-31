WITH tabela_ed AS (
select codeditora, nome, codendereco, estado, cidade, ed.nome
from endereco as end
join editora as ed
	on end.codendereco = ed.endereco
)

select 
	count(editora) AS quantidade,
	ed_novo.nome,
	ed_novo.estado,
	ed_novo.cidade
from livro AS liv
JOIN tabela_ed AS ed_novo
	ON liv.editora = ed_novo.codeditora
group by editora
ORDER BY quantidade desc
LIMIT 5