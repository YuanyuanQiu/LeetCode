select avg(number) median
from
    (select 
		number,
        sum(frequency) over(order by number) asc_accumu,
        sum(frequency) over(order by number desc) desc_accumu
	from numbers) t1, 
    (select sum(frequency) total from numbers) t2
where asc_accumu >= total/2 and desc_accumu >=total/2