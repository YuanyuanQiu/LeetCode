select d.name as Department, e.name as Employee, e.Salary
from Employee e
join Department d
on e.DepartmentId = d.Id
where (e.DepartmentId, e.Salary) in (select DepartmentId, max(Salary)
                                    from Employee
                                    group by DepartmentId)