WITH EmployeeStats AS (
    SELECT 
        id, 
        month, 
        salary,
        -- Calculate sum based on Value Range (handles gaps automatically)
        SUM(salary) OVER (
            PARTITION BY id 
            ORDER BY month 
            RANGE BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS accumulated_salary,
        -- Identify the last month to filter it out later
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY month DESC) as rn_desc
    FROM Employee
)
SELECT 
    id, 
    month, 
    accumulated_salary as Salary
FROM EmployeeStats
WHERE rn_desc > 1 -- Exclude the most recent month (Rank 1)
ORDER BY id ASC, month DESC;