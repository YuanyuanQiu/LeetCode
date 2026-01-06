WITH Ranked AS (
    SELECT 
        username, 
        activity, 
        startDate, 
        endDate,
        ROW_NUMBER() OVER (PARTITION BY username ORDER BY startDate DESC) AS rn,
        COUNT(*) OVER (PARTITION BY username) AS total_cnt
    FROM UserActivity
)
SELECT 
    username, activity, startDate, endDate
FROM Ranked
WHERE rn = 2 OR total_cnt = 1;