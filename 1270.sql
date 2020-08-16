select employee_id
from Employees
where manager_id = 1 and manager_id != 1
union
select e1.employee_id
from Employees e1, (select employee_id
					from Employees
					where manager_id = 1 and manager_id != 1) a
where e1.manager_id = a.employee_id
union
select e2.employee_id
from Employees e2, (select e1.employee_id
					from Employees e1, (select employee_id
										from Employees
										where manager_id = 1 and manager_id != 1) a
					where e1.manager_id = a.employee_id) a1
where e2.manager_id = a1.employee_id
order by employee_id