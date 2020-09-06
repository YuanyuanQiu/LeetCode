select distinct a.*
from Accounts a
join Logins l1
using(id)
join Logins l2
on l1.id = l2.id
and datediff(l2.login_date, l1.login_date) between 0 and 4
group by a.id, a.name, l1.login_date
having count(distinct l2.login_date) = 5