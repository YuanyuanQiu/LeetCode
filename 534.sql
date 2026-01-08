-- Option 1
SELECT 
    t1.player_id, 
    t1.event_date, 
    SUM(t2.games_played) AS games_played_so_far
FROM Activity t1
JOIN Activity t2 
    ON t1.player_id = t2.player_id 
    AND t1.event_date >= t2.event_date
GROUP BY t1.player_id, t1.event_date
ORDER BY t1.player_id, t1.event_date;

-- Option 2
SELECT
    player_id,
    event_date,
    SUM(games_played) OVER (PARTITION BY player_id ORDER BY event_date) AS games_played_so_far
FROM Activity
ORDER BY player_id, event_date;