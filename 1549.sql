# https://blog.csdn.net/qq_21201267/article/details/107996931?ops_request_misc=%25257B%252522request%25255Fid%252522%25253A%252522161213166116780271543371%252522%25252C%252522scm%252522%25253A%25252220140713.130102334.pc%25255Fall.%252522%25257D&request_id=161213166116780271543371&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-1-107996931.pc_search_result_cache&utm_term=leetcode+1549

select p.product_name, o.product_id, o.order_id, o.order_date
from orders o
left join products p
on o.product_id = p.product_id
where (o.product_id, o.order_date) in (select product_id, max(order_date)
										from orders
                                        group by product_id)
order by p.product_name, o.product_id, o.order_id