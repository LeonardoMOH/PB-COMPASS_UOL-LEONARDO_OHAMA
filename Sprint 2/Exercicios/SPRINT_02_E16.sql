SELECT
	estado,
	nmpro,
	round(sum(qtd)/((1.0)*count(estado)),4) as quantidade_media
from tbvendas
where status = 'Concluído'
group by estado, nmpro
order by estado, nmpro