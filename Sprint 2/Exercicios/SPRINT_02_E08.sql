with vendas as(
	SELECT
		cdvdd,
		count(cdvdd) as quantidade
	from tbvendas
	group by cdvdd
)

select
	vend.cdvdd,
	nmvdd
from tbvendedor as vend
join vendas as ven
	on vend.cdvdd = ven.cdvdd
order by ven.quantidade DESC 
limit 1