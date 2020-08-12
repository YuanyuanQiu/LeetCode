select project_id
from project
group by project_id
having count(*) = (select count(*)
					from project
					group by project_id
					order by count(*) desc
					limit 1)