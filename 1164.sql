SELECT * 
FROM 
	(SELECT product_id, new_price AS price
	 FROM Products
	 WHERE (product_id, change_date) IN (SELECT product_id, MAX(change_date)
										 FROM Products
										 WHERE change_date <= '2019-08-16'
										 GROUP BY product_id)
	 
	 UNION
	 
	 SELECT DISTINCT product_id, 10 AS price
	 FROM Products
	 WHERE product_id NOT IN (SELECT product_id FROM Products WHERE change_date <= '2019-08-16')
	) tmp
ORDER BY price DESC

# method 2
select
    t1.product_id,
    (case
        when change_date is null then 10
        else new_price
    end) as price
from (select distinct product_id
        from Products) t1
left join (select product_id, new_price, change_date
            from Products
            where (product_id, change_date) in (select product_id, max(change_date)
                                                from Products
                                                where change_date <= '2019-08-16'
                                                group by product_id)) t2
on t1. product_id = t2.product_id