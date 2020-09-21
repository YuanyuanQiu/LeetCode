select round(avg(immediate) * 100,2) as immediate_percentage
from (select
        (case
            when order_date = customer_pref_delivery_date then 1 else 0
        end)as immediate
    from Delivery
    where (customer_id, order_date) in (select customer_id, min(order_date)
                                        from Delivery
                                        group by customer_id)
    ) t