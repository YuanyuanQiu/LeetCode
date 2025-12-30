WITH AllScores AS (
    -- 1. 先把两列分数解压成一列，不用在里面聚合，直接 UNION ALL 即可
    SELECT first_player AS player_id, first_score AS score FROM Matches
    UNION ALL
    SELECT second_player AS player_id, second_score AS score FROM Matches
),
Stats AS (
    -- 2. 算出每个人的总分，并关联 Group ID
    SELECT 
        p.group_id, 
        p.player_id, 
        SUM(s.score) AS total_score
    FROM Players p
    JOIN AllScores s ON p.player_id = s.player_id
    GROUP BY p.group_id, p.player_id
),
Ranked AS (
    -- 3. 核心步骤：打排名
    -- 规则：按分数由高到低排，分数一样按 ID 由小到大排
    SELECT 
        group_id, 
        player_id,
        ROW_NUMBER() OVER (
            PARTITION BY group_id 
            ORDER BY total_score DESC, player_id ASC
        ) as rn
    FROM Stats
)
-- 4. 取出第一名
SELECT group_id, player_id
FROM Ranked
WHERE rn = 1;