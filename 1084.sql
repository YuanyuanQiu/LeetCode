select s.product_id, p.product_name
from sales s
join product p
on s.product_id = p.product_id
where sale_date between '2019-01-01' and '2019-03-01'
	and s.product_id not in (select product_id
							from sales
                            where sale_date not between '2019-01-01' and '2019-03-01')