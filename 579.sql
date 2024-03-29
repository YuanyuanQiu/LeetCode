-- SELECT
--     E1.id,
--     E1.month,
--     (IFNULL(E1.salary, 0) + IFNULL(E2.salary, 0) + IFNULL(E3.salary, 0)) AS Salary
-- FROM
--     (SELECT id, MAX(month) AS month
--     FROM Employee
--     GROUP BY id
--     HAVING COUNT(*) > 1) AS maxmonth
--     LEFT JOIN Employee E1
--     ON maxmonth.id = E1.id AND maxmonth.month > E1.month
--     LEFT JOIN Employee E2
--     ON E2.id = E1.id AND E2.month = E1.month - 1
--     LEFT JOIN Employee E3
--     ON E3.id = E1.id AND E3.month = E1.month - 2
-- ORDER BY id, month DESC

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