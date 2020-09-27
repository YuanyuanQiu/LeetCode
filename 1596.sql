select b.customer_id, b.product_id, product_name
from
    (select
        customer_id,
        product_id, 
        dense_rank() over (partition by customer_id order by counts desc) as ranking
    from (select *, count(order_id) as counts
            from orders 
            group by customer_id, product_id) a
    ) b
join customers
on b.customer_id = customers.customer_id
join products
on b.product_id = products.product_id
where ranking = 1