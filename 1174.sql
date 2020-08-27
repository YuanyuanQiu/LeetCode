select round(sum(order_date = customer_pref_delivery_date)
            / count(*) * 100,2) as immediate_percentage
from
	(select *
    from Delivery
    where order_date = min(order_date)
    group by customer_id
    ) t