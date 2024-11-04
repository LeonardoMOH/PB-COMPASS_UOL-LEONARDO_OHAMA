WITH tabela_ed AS (
select codeditora, nome, codendereco, estado, cidade, ed.nome
from endereco as end
join editora as ed
	on end.codendereco = ed.endereco
)

select 
	ed_novo.codeditora as CodEditora,
	ed_novo.nome as NomeEditora,
	count(editora) AS QuantidadeLivros
from livro AS liv
JOIN tabela_ed AS ed_novo
	ON liv.editora = ed_novo.codeditora
group by editora
ORDER BY QuantidadeLivros desc
LIMIT 5