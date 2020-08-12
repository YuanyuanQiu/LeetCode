# Method 1
select distinct buyer_id
from sales
where buyer_id in (select product_id
					from product
                    where product_name = 'S8')
		and buyer_id not in (select product_id
								from product
                                where product_name = 'iPhone')

# Method 2
select distinct buyer_id
from sales as s
left join product as p
on s.product_id=p.product_id 
where p.product_name='S8' and buyer_id not in (select buyer_id
												from sales as s
                                                left join product as p
                                                on s.product_id=p.product_id
                                                where product_name ='iPhone')