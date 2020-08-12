# Method 1
select seller_id
from sales
group by seller_id
having sum(price) = (select sum(price)
					from sales
                    group by seller_id
                    order by sum(price) desc
                    limit 1)

# Method 2
select seller_id
from sales
group by seller_id
having sum(price) >= all(select sum(price)
						from sales
                        group by seller_id )