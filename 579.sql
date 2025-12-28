SELECT Id, Month, Salary
FROM
    (SELECT
        Id,
        Month,
        SUM(Salary) OVER (PARTITION BY Id ORDER BY Month ROWS 2 PRECEDING) AS Salary,
        rank() OVER (PARTITION BY Id ORDER BY Month DESC) AS r
    FROM Employee) t
WHERE r > 1
ORDER BY Id, Month DESC;