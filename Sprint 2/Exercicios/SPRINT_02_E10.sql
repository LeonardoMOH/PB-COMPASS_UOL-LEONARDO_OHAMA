SELECT
	vendedor.nmvdd as vendedor,
	round(sum((qtd*vrunt)),2) as valor_total_vendas,
	round((sum((qtd*vrunt)) * (1.0/100)) * vendedor.perccomissao,2) as comissao
from tbvendas as vendas
join tbvendedor as vendedor
	on vendas.cdvdd = vendedor.cdvdd
where status = 'Concluído'
group by nmvdd
order by comissao desc