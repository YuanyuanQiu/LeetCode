-- SELECT d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
-- FROM Employee e1
-- JOIN Department d
-- ON e1.DepartmentId = d.Id
-- WHERE (SELECT COUNT(DISTINCT e2.Salary)
--         FROM Employee e2
--         WHERE e2.Salary > e1.Salary
--         AND e1.DepartmentId = e2.DepartmentId) < 3


select d.Name as Department, e.Name as Employee, e.Salary
From
    (select
        *,
        dense_rank() over(partition by DepartmentId order by Salary desc) as rk
    from Employee) e
join Department d
on e.DepartmentId = d.Id
where rk <= 3