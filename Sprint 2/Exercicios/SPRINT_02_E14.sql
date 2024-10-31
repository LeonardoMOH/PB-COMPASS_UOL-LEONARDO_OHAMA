select
	estado,
	round(sum(qtd*vrunt)/((1.0)*count(estado)),2) as gastomedio
from tbvendas
where status = 'Concluído'
group by estado
order by gastomedio desc