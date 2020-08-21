select p.project_id, e.employee_id
from Project p, Employee e
where p.employee_id = e.employee_id
	and p.project_id, e.experience_years in (SELECT p2.project_id, max(experience_years) as max_year
											from project as p2
											join employee as e2
											ON p2.employee_id = e2.employee_id
											GROUP BY p2.project_id)