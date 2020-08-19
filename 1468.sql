select
	s.company_id,
	s.employee_id,
    s.employee_name,
    round((case  
		when ms.max_salary < 1000 then s.salary
        when ms.max_salary >= 1000 and ms.max_salary <= 10000 then s.salary * (1-0.24)
        when ms.max_salary > 10000 then s.salary * (1-0.49)
        ),2) as salary
from
	Salaries s, 
	(select company_id, max(salary) as max_salary
	from Salaries
	group by company_id) ms
where s.company_id = ms.company_id