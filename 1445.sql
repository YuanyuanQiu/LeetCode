select
	sale_date,
    sum(case fruit
			when 'apples' then sold_num
            when 'oranges' then -1 * sold_num
		end) as diff
from Sales
group by sale_date
order by sale_date