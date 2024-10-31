SELECT
	cdcli,
	nmcli,
	sum(qtd*vrunt) as gasto
from tbvendas
group by nmcli
order by gasto DESC
limit 1