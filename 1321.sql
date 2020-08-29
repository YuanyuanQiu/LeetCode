select
	visit_on,
    sum(c2.amount) as amount,
    round(sum(c2.amount)/7,2) as average_amount
from 
	(select customer_id,name,visited_on,sum(amount) amount
    from Customer
    group by visited_on) c1,
	(select customer_id,name,visited_on,sum(amount) amount
    from Customer
    group by visited_on) c2
where datediff(c1.visit_on, c2.visit_on) <= 6
	and datediff(c1.visit_on, c2.visit_on) >= 0
group by c1.visit_on
order by c1.visit_on