select num
from my_numbers
group by num
having count(num) = 1
order by num DESC
limit 1