WITH RECURSIVE Months AS (
    -- 1. Generate months 1 to 12 to ensure we have data for the forward lookups
    SELECT 1 as month
    UNION ALL
    SELECT month + 1
    FROM Months
    WHERE month < 12
),
MonthlyTotals AS (
    -- 2. Calculate the SUM for each specific month
    SELECT
        m.month,
        IFNULL(SUM(ar.ride_distance), 0) AS mon_dist,
        IFNULL(SUM(ar.ride_duration), 0) AS mon_dur
    FROM Months m
    LEFT JOIN Rides r
        ON m.month = MONTH(r.requested_at)
        AND YEAR(r.requested_at) = 2020 -- Filter inside ON clause to preserve empty months
    LEFT JOIN AcceptedRides ar
        ON r.ride_id = ar.ride_id
    GROUP BY m.month
),
Calculations AS (
    -- 3. Calculate the rolling sum of the monthly totals / 3
    SELECT
        month,
        ROUND(SUM(mon_dist) OVER (ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING) / 3, 2) AS average_ride_distance,
        ROUND(SUM(mon_dur) OVER (ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING) / 3, 2) AS average_ride_duration
    FROM MonthlyTotals
)
-- 4. Filter for the requested output range
SELECT *
FROM Calculations
WHERE month <= 10;