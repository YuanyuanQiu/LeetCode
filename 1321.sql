select
    c1.visited_on,
    sum(c2.amount) as amount,
    round(sum(c2.amount)/7,2) as average_amount
from
    (select visited_on, sum(amount) as amount
    From Customer
    group by visited_on) c1,
    (select visited_on, sum(amount) as amount
    From Customer
    group by visited_on) c2
where datediff(c1.visited_on, c2.visited_on) <= 6
    and datediff(c1.visited_on, c2.visited_on) >= 0
group by c1.visited_on
having count(c2.visited_on) = 7
order by c1.visited_on