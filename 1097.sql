WITH FirstLogin AS (
    SELECT
        player_id,
        MIN(event_date) AS install_dt
    FROM Activity
    GROUP BY player_id
)
SELECT 
    f.install_dt,
    -- 1. 明确指定表名，统计安装总人数
    COUNT(f.player_id) AS installs,
    -- 2. 计算留存率
    ROUND(
        COUNT(a.player_id) / COUNT(f.player_id)
    , 2) AS Day1_retention
FROM FirstLogin f
LEFT JOIN Activity a
    ON f.player_id = a.player_id
    -- 3. 使用 DATEDIFF 或者 DATE_ADD 确保跨月计算正确
    AND DATEDIFF(a.event_date, f.install_dt) = 1
GROUP BY f.install_dt;