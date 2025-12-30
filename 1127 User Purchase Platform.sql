-- 1. 打标：计算每个 User 在每一天的归属 (Mobile/Desktop/Both)
WITH UserCategory AS (
    SELECT 
        spend_date,
        user_id,
        -- 核心逻辑：如果平台数是2，就是both；否则就是那个唯一的平台
        CASE 
            WHEN COUNT(DISTINCT platform) = 2 THEN 'both'
            ELSE MAX(platform) 
        END AS derived_platform,
        SUM(amount) AS total_amount
    FROM Spending
    GROUP BY spend_date, user_id
),
-- 2. 骨架：我们需要 3 种平台硬编码，去匹配所有的日期
AllPlatforms AS (
    SELECT 'desktop' AS platform UNION ALL
    SELECT 'mobile' UNION ALL
    SELECT 'both'
),
-- 算出所有出现的日期 (或者直接 SELECT DISTINCT spend_date FROM Spending)
AllDates AS (
    SELECT DISTINCT spend_date FROM Spending
),
-- 生成 (日期 x 平台) 的笛卡尔积，确保即使没有销量也有这一行
Skeleton AS (
    SELECT d.spend_date, p.platform
    FROM AllDates d
    CROSS JOIN AllPlatforms p
)

-- 3. 合并：Skeleton LEFT JOIN 打标后的数据
SELECT 
    s.spend_date,
    s.platform,
    IFNULL(SUM(u.total_amount), 0) AS total_amount,
    IFNULL(COUNT(u.user_id), 0) AS total_users
FROM Skeleton s
LEFT JOIN UserCategory u 
    ON s.spend_date = u.spend_date 
    AND s.platform = u.derived_platform
GROUP BY s.spend_date, s.platform;