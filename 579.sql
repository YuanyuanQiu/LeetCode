-- Option 1 Window Function
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

-- Option 2 Self-Join
SELECT 
    E1.id, 
    E1.month, 
    SUM(E2.salary) AS Salary
FROM Employee E1
JOIN Employee E2 
    ON E1.id = E2.id 
    -- The Core Logic: Match rows where E2 is E1 or up to 2 months prior
    AND E2.month BETWEEN E1.month - 2 AND E1.month
WHERE E1.month < (SELECT MAX(month) FROM Employee WHERE id = E1.id)
GROUP BY E1.id, E1.month
ORDER BY E1.id ASC, E1.month DESC;