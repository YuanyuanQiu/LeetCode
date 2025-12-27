WITH Ranked AS (
    SELECT
        id,
        company,
        salary,
        ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary, id) AS rn,
        COUNT(*) OVER (PARTITION BY company) AS cnt
    FROM Employee
)
SELECT
    id,
    company,
    salary
FROM Ranked
WHERE rn >= cnt/2 AND rn <= cnt/2 + 1
ORDER BY company, salary;