with dependente as (
	select
		cddep,
		nmdep,
		dtnasc,
		cdvdd
	from tbdependente
)

SELECT
	dep.cddep,
	dep.nmdep,
	dep.dtnasc,
	sum(qtd*vrunt) as valor_total_vendas
from tbvendas as ven
join dependente as dep
	on ven.cdvdd = dep.cdvdd
where status = 'Concluído'
group by dep.nmdep
order by valor_total_vendas
limit 1