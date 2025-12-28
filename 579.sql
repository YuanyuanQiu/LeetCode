SELECT Id, Month, Salary
FROM
    (SELECT
        Id,
        Month,
        -- 修改点：将 ROWS 改为 RANGE。这会根据 Month 的数值来圈定范围，而不是行数
        SUM(Salary) OVER (
            PARTITION BY Id 
            ORDER BY Month 
            RANGE BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS Salary,
        RANK() OVER (PARTITION BY Id ORDER BY Month DESC) AS r
    FROM Employee) t
WHERE r > 1
ORDER BY Id, Month DESC;