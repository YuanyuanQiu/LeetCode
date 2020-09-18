select c.name customer_name, c.customer_id, t.order_id, t.order_date
from
	(select
		customer_id,
        order_id,
        order_date, 
		dense_rank() over (partition by customer_id order by order_date desc) rnk
    from Orders) t
join Customers c
on t.customer_id = c.customer_id
where rnk <= 3
order by c.name, c.customer_id, t.order_date desc