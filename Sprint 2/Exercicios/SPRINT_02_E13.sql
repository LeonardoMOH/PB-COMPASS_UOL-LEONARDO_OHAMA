SELECT
	cdpro,
	nmcanalvendas,
	nmpro,
	sum(qtd) as quantidade_vendas
from tbvendas
where status = 'Concluído'and nmcanalvendas in ('Matriz', 'Ecommerce')
group by cdpro, nmcanalvendas 
order by quantidade_vendas
limit 10