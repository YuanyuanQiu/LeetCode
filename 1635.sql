-- Option 1
with recursive f(n) as (select 1 as n
                        union
                        select n + 1 as n
                        from f
                        where n < 12),

a as (select month, sum(cnt) as active_drivers
        from
            (select 1 as month, count(driver_id) as cnt
            from Drivers
            where join_date < '2020-01-01'
            union all
            select month(join_date) as month, count(driver_id) as cnt
            from Drivers
            where join_date >= '2020-01-01' and join_date < '2021-01-01'
            group by month) t
        group by month
        order by month),
b as (select
        month(r.requested_at) as month,
        count(r.ride_id) as accepted_rides
    from Rides r
    join AcceptedRides a
    on r.ride_id = a.ride_id
    where requested_at between '2020-01-01' and '2020-12-31'
    group by month),
c as
(select
    f.n as month,
    ifnull(a.active_drivers, 0) as active_drivers,
    ifnull(b.accepted_rides, 0) as accepted_rides
from f
left join a on f.n = a.month
left join b on f.n = b.month
order by month)

select month, sum(active_drivers) over(order by month) as active_drivers, accepted_rides
from c
group by month

-- Option 2
WITH RECURSIVE Months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1 FROM Months WHERE month < 12
),
-- 1. 算出每个月 2020 年新加入的司机数
NewDrivers AS (
    SELECT 
        MONTH(join_date) AS month, 
        COUNT(driver_id) AS new_cnt
    FROM Drivers
    WHERE YEAR(join_date) = 2020
    GROUP BY MONTH(join_date)
),
-- 2. 算出 2020 年之前的存量司机数 (Base)
InitialDrivers AS (
    SELECT COUNT(driver_id) AS base_cnt
    FROM Drivers
    WHERE join_date < '2020-01-01'
),
-- 3. 算出每个月的接单数
MonthlyRides AS (
    SELECT 
        MONTH(r.requested_at) AS month,
        COUNT(a.ride_id) AS accepted_cnt
    FROM AcceptedRides a
    JOIN Rides r ON a.ride_id = r.ride_id
    WHERE YEAR(r.requested_at) = 2020
    GROUP BY MONTH(r.requested_at)
)

SELECT 
    m.month,
    -- 核心逻辑：累积司机 = (初始司机 + 截止到本月的累计新增司机)
    (SELECT base_cnt FROM InitialDrivers) + 
    IFNULL(SUM(nd.new_cnt) OVER (ORDER BY m.month), 0) AS active_drivers,
    IFNULL(mr.accepted_cnt, 0) AS accepted_rides
FROM Months m
LEFT JOIN NewDrivers nd ON m.month = nd.month
LEFT JOIN MonthlyRides mr ON m.month = mr.month
ORDER BY m.month;