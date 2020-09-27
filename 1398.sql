select distinct c.customer_id, c.customer_name
from Customers c
join Orders o
on c.customer_id = o.customer_id
where c.customer_id not in (select customer_id
                            from Orders
                            where product_name = 'C')
    and c.customer_id in (select customer_id
                            from Orders
                            where product_name = 'A')
    and c.customer_id in (select customer_id
                            from Orders
                            where product_name = 'B')

SELECT
    c.customer_id, c.customer_name
FROM
    Orders o LEFT JOIN Customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id
HAVING
    SUM(product_name = 'A') * SUM(product_name = 'B') > 0
    AND SUM(product_name = 'C') = 0
ORDER BY c.customer_id