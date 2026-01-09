WITH SalaryStats AS (
    SELECT 
        -- Format date to YYYY-MM immediately
        DATE_FORMAT(pay_date, '%Y-%m') as pay_month,
        e.department_id,
        s.amount,
        -- Calculate Company Average for that Month
        AVG(amount) OVER (PARTITION BY DATE_FORMAT(pay_date, '%Y-%m')) as company_avg,
        -- Calculate Department Average for that Month
        AVG(amount) OVER (PARTITION BY DATE_FORMAT(pay_date, '%Y-%m'), e.department_id) as dept_avg
    FROM Salary s
    JOIN Employee e ON s.employee_id = e.employee_id
)
SELECT DISTINCT -- CTE returns one row per salary record
    pay_month, 
    department_id,
    CASE 
        WHEN dept_avg > company_avg THEN 'higher'
        WHEN dept_avg < company_avg THEN 'lower'
        ELSE 'same'
    END as comparison
FROM SalaryStats;