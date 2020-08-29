select activity
from Friends
group by activity
having count(id) != (select count(id)
					from Friends
                    group by activity
                    order by count(id) desc
                    limit 1)
and count(id) != (select count(id)
					from Friends
                    group by activity
                    order by count(id)
                    limit 1)