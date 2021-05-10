select s.product_id as product_id, p.product_name
from Product p
join Sales s
on p.product_id = s.product_id
where s.product_id not in (select product_id
                            from Sales
                            where sale_date < '2019-01-01' or sale_date > '2019-03-31')
group by s.product_id