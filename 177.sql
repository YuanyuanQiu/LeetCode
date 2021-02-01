CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    set n := n-1;
    RETURN (
        select Salary
        from Employee
        group by Salary
        order by Salary desc
        limit 1 offset n
    );
END