-- Option 1
# Write your MySQL query statement below
WITH categories AS (
    SELECT "Low Salary" AS category
    UNION ALL
    SELECT "Average Salary" AS category
    UNION ALL
    SELECT "High Salary" AS category
),
acct_cat AS (
    SELECT
        account_id,
        CASE
            WHEN income < 20000 THEN "Low Salary"
            WHEN income > 50000 THEN "High Salary"
        ELSE "Average Salary" END AS category
    FROM Accounts
)
SELECT
    c.category,
    IFNULL(COUNT(DISTINCT account_id), 0) AS accounts_count
FROM categories c
LEFT JOIN acct_cat ac
ON c.category = ac.category
GROUP BY c.category

-- Option 2
SELECT 'Low Salary' AS category, SUM(income < 20000) AS accounts_count FROM Accounts
UNION
SELECT 'Average Salary', SUM(income BETWEEN 20000 AND 50000) FROM Accounts
UNION
SELECT 'High Salary', SUM(income > 50000) FROM Accounts;
-- Note: SUM(condition) is a MySQL-specific shorthand.
-- In standard SQL, you would use COUNT(CASE WHEN ...)